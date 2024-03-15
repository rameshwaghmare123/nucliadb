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
import asyncio
import logging
from typing import Optional
import logging

from nucliadb.common.context import ApplicationContext
from nucliadb.migrator.utils import get_migrations
from nucliadb_telemetry import errors, metrics

logger = logging.getLogger(__name__)


async def run(context: ApplicationContext) -> None:
    async with context.maybe_distributed_lock("rebalance"):
        # go through each kb and see if shards need to be reduced in size
        ...


async def run_forever(context: ApplicationContext) -> None:
    """
    Most of the time this will be a noop but allows
    retrying failures until everything is done.
    """
    while True:
        try:
            await run(context)
        except Exception:
            logger.exception("Failed to run rebalancing. Will retry again in 5 minutes")
        await asyncio.sleep(5 * 60)
