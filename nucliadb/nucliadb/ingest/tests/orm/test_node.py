# Copyright (C) 2021 Bosutech XXI S.L.
#
# nucliadb is offered under the AGPL v3.0 and as commercial software.
# For commercial licensing, contact us at info@nuclia.com.
#
# AGPL:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
import pytest
from nucliadb_protos.writer_pb2 import Member

from nucliadb.ingest.orm import NODES
from nucliadb.ingest.orm.node import ClusterMember, NodeType, chitchat_update_node


def get_cluster_member(
    node_id="foo",
    listen_addr="192.1.1.1:8080",
    type=NodeType.IO,
    online=True,
    is_self=False,
    load_score=0,
    shard_count=0,
) -> ClusterMember:
    return ClusterMember(
        node_id=node_id,
        listen_addr=listen_addr,
        type=type,
        online=online,
        is_self=is_self,
        load_score=load_score,
        shard_count=shard_count,
    )


@pytest.mark.asyncio
async def test_chitchat_update_node():
    assert NODES == {}
    await chitchat_update_node([])
    assert len(NODES) == 0

    # Check that it ignores itself
    member = get_cluster_member(is_self=True)
    await chitchat_update_node([member])
    assert len(NODES) == 0

    # Check that it ignores types other than node_type=NodeType.IO
    member = get_cluster_member(type=NodeType.INGEST)
    await chitchat_update_node([member])
    assert len(NODES) == 0

    # Check it registers new members
    member = get_cluster_member(node_id="node1")
    await chitchat_update_node([member])
    assert len(NODES) == 1
    node = NODES["node1"]
    assert node.address == member.listen_addr
    assert node.load_score == member.load_score
    assert node.shard_count == member.shard_count

    # Check that it updates loads score for registered members
    member.load_score = 30
    member.shard_count = 2
    await chitchat_update_node([member])
    assert len(NODES) == 1
    node = NODES["node1"]
    assert node.load_score == 30
    assert node.shard_count == 2

    # Check that it removes members that are no longer reported
    await chitchat_update_node([])
    assert len(NODES) == 0


def test_node_type_from_str():
    for raw_type, node_type in [
        ("Io", NodeType.IO),
        ("Train", NodeType.TRAIN),
        ("Ingest", NodeType.INGEST),
        ("Search", NodeType.SEARCH),
        ("Blablabla", NodeType.UNKNOWN),
        ("Cat is everything", NodeType.UNKNOWN),
    ]:
        assert NodeType.from_str(raw_type) == node_type


def test_node_type_pb_conversion():
    for node_type, member_type in [
        (NodeType.IO, Member.Type.IO),
        (NodeType.TRAIN, Member.Type.TRAIN),
        (NodeType.INGEST, Member.Type.INGEST),
        (NodeType.SEARCH, Member.Type.SEARCH),
        (NodeType.UNKNOWN, Member.Type.UNKNOWN),
    ]:
        assert node_type.to_pb() == member_type
        assert NodeType.from_pb(member_type) == node_type


@pytest.mark.asyncio
async def test_update_node_metrics(metrics_registry):
    node1 = "node-1"
    member1 = get_cluster_member(
        node_id=node1, type=NodeType.IO, load_score=10, shard_count=2
    )
    await chitchat_update_node([member1])

    assert metrics_registry.get_sample_value("nucliadb_nodes_available", {}) == 1
    assert (
        metrics_registry.get_sample_value("nucliadb_node_shard_count", {"node": node1})
        == 2
    )
    assert (
        metrics_registry.get_sample_value("nucliadb_node_load_score", {"node": node1})
        == 10
    )

    node2 = "node-2"
    member2 = get_cluster_member(
        node_id=node2, type=NodeType.IO, load_score=40, shard_count=1
    )
    await chitchat_update_node([member2])

    assert metrics_registry.get_sample_value("nucliadb_nodes_available", {}) == 1
    assert (
        metrics_registry.get_sample_value("nucliadb_node_shard_count", {"node": node2})
        == 1
    )
    assert (
        metrics_registry.get_sample_value("nucliadb_node_load_score", {"node": node2})
        == 40
    )

    # Check that samples of destroyed node have been removed
    assert (
        metrics_registry.get_sample_value("nucliadb_node_shard_count", {"node": node1})
        is None
    )
    assert (
        metrics_registry.get_sample_value("nucliadb_node_load_score", {"node": node1})
        is None
    )

    NODES.clear()