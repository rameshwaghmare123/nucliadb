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

from typing import Optional

from pydantic import Field

from nucliadb.ingest.settings import DriverSettings


class Settings(DriverSettings):
    search_timeout: float = 10.0
    slow_find_log_threshold: float = Field(
        default=3.0,
        title="Slow query log threshold",
        description="The threshold in seconds for logging slow find queries",
    )

    slow_node_query_log_threshold: float = Field(
        default=2.0,
        title="Slow node query log threshold",
        description="The threshold in seconds for logging slow node queries",
    )
    prequeries_max_parallel: int = Field(
        default=2,
        title="Prequeries max parallel",
        description="The maximum number of prequeries to run in parallel per /ask request",
    )
    nidx_address: Optional[str] = Field(default=None)


settings = Settings()
