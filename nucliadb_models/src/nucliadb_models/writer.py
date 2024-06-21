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
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field, field_validator

from nucliadb_models.common import File, UserClassification
from nucliadb_models.conversation import (
    InputConversationField,
    InputMessage,
    InputMessageContent,
    MessageType,
)
from nucliadb_models.file import FileField
from nucliadb_models.link import LinkField
from nucliadb_models.metadata import (
    Extra,
    InputMetadata,
    InputOrigin,
    Origin,
    UserFieldMetadata,
    UserMetadata,
)
from nucliadb_models.processing import PushProcessingOptions
from nucliadb_models.security import ResourceSecurity
from nucliadb_models.text import TextField, TextFormat
from nucliadb_models.utils import FieldIdPattern, FieldIdString, SlugPattern, SlugString

GENERIC_MIME_TYPE = "application/generic"


class FieldDefaults:
    title = Field(
        default=None,
        title="Title",
        description="Title of the resource",
        examples=["Spaghetti Carbonara recipe"],
    )
    summary = Field(
        default=None,
        title="Summary",
        description="Summary of the resource",
        examples=[
            "This is a recipe for spaghetti carbonara. Includes the ingredients and the steps to prepare it, along with a picture of the final dish."
        ],
    )  # noqa
    slug = Field(
        default=None,
        title="Slug",
        description=f"The slug is the user-defined id for the resource. It must comply with the regex: {SlugPattern}",  # noqa
        examples=["spaghetti-carbonara-recipe"],
    )
    created = Field(
        default=None,
        title="Created timestamp",
        description="Timestamp when the resource was created in ISO 8601 format",
        examples=["2021-06-29T12:00:00Z"],
    )
    modified = Field(
        default=None,
        title="Modified timestamp",
        description="Timestamp when the resource was last modified in ISO 8601 format",
        examples=["2021-06-29T12:00:00Z"],
    )
    icon = Field(
        None,
        title="Icon",
        description="The icon should be a media type string: https://www.iana.org/assignments/media-types/media-types.xhtml",  # noqa
        examples=["image/png", "text/plain", "application/pdf"],
    )
    thumbnail = Field(
        default=None,
        title="Resource thumbnail URL",
        description="Internal URL to download the thumbnail of the resource",
        examples=["https://en.wikipedia.org/wiki/Carbonara#/media/File:Espaguetis_carbonara.jpg"],
    )
    origin_create_or_update = Field(
        default=None,
        title="Origin",
        description="Origin metadata for the resource. Use it to store information of the resource at the origin, like the creation date, the tags, the collaborators, etc.",  # noqa
        examples=[
            InputOrigin(
                url="https://en.wikipedia.org/wiki/Carbonara",
                created=datetime.fromisoformat("1850-01-01T00:00:00Z"),
                tags=["pasta", "italian"],
                collaborators=["Jane Doe"],
            ),
        ],
    )
    extra_create_or_update = Field(
        default=None,
        title="Extra",
        description="Extra metadata for the resource. Use it to store any other arbitrary metadata. The size of the serialized JSON must be less than 400KB and the metadata will not be used for searching or filtering.",  # noqa
        examples=[
            Extra(metadata={"foo": "bar"}),
        ],
    )
    files = Field(
        {},
        title="Files",
        description=f"Dictionary of file fields to be added to the resource. The keys correspond to the field id, and must comply with the regex: {FieldIdPattern}",  # noqa
        examples=[
            {
                "picture": FileField(
                    language="en",
                    file=File(
                        filename="carbonara.jpg",
                        content_type="image/jpeg",
                        payload="<base64_encoded_image>",
                    ),
                )
            }
        ],
    )
    links = Field(
        {},
        title="Links",
        description=f"Dictionary of link fields to be added to the resource. The keys correspond to the field id, and must comply with the regex: {FieldIdPattern}",  # noqa
        examples=[
            {"source": LinkField(uri="https://en.wikipedia.org/wiki/Carbonara", language="en")},
        ],
    )
    texts = Field(
        {},
        title="Texts",
        description=f"Dictionary of text fields to be added to the resource. The keys correspond to the field id, and must comply with the regex: {FieldIdPattern}",  # noqa
        examples=[
            {
                "recipe": TextField(
                    body="Spaghetti Carbonara recipe. Ingredients: eggs, bacon, spaghetti. Directions: ...",
                    format=TextFormat.PLAIN,
                )
            }
        ],
    )
    conversations = Field(
        {},
        title="Conversations",
        description=f"Dictionary of conversation fields to be added to the resource. The keys correspond to the field id, and must comply with the regex: {FieldIdPattern}",  # noqa
        examples=[
            {
                "comments": InputConversationField(
                    messages=[
                        InputMessage(
                            type=MessageType.UNSET,
                            timestamp=datetime.now(),
                            who="John Doe",
                            content=InputMessageContent(text="I love this recipe!"),
                            ident="1234",
                        )
                    ]
                )
            }
        ],
    )
    usermetadata_create_or_update = Field(
        default=None,
        title="User metadata",
        description="User-provided metadata for the resource that applies to all fields of the resource, such as classifications.",
        examples=[
            UserMetadata(classifications=[UserClassification(labelset="cuisine", label="italian")])
        ],
    )
    processing_options = Field(
        default=PushProcessingOptions(),
        title="Processing options",
        description="Options to enable or disable at resource processing time",
    )
    metadata_create_or_update = Field(
        default=None,
        title="Metadata",
        description="Metadata for the resource, such as language, or arbitrary metadata.",  # noqa
        examples=[
            InputMetadata(
                metadata={"foo": "bar"},
                language="en",
                languages=[
                    "en",
                ],
            )
        ],
    )
    fieldmetadata_create_or_update = Field(
        default=None,
        title="Field metadata",
        description="Field-specific metadata input by the user",
        deprecated=True,
    )
    security = Field(
        default=None,
        title="Security",
        description="Security metadata for the resource. It can be used to have fine-grained control over who can access the resource.",  # noqa
    )


class CreateResourcePayload(BaseModel):
    title: Optional[str] = FieldDefaults.title
    summary: Optional[str] = FieldDefaults.summary
    slug: Optional[SlugString] = FieldDefaults.slug
    icon: Optional[str] = FieldDefaults.icon
    thumbnail: Optional[str] = FieldDefaults.thumbnail
    metadata: Optional[InputMetadata] = FieldDefaults.metadata_create_or_update
    usermetadata: Optional[UserMetadata] = FieldDefaults.usermetadata_create_or_update
    fieldmetadata: Optional[List[UserFieldMetadata]] = FieldDefaults.fieldmetadata_create_or_update
    origin: Optional[Origin] = FieldDefaults.origin_create_or_update
    extra: Optional[Extra] = FieldDefaults.extra_create_or_update
    files: Dict[FieldIdString, FileField] = FieldDefaults.files
    links: Dict[FieldIdString, LinkField] = FieldDefaults.links
    texts: Dict[FieldIdString, TextField] = FieldDefaults.texts
    conversations: Dict[FieldIdString, InputConversationField] = FieldDefaults.conversations
    processing_options: Optional[PushProcessingOptions] = FieldDefaults.processing_options
    security: Optional[ResourceSecurity] = FieldDefaults.security

    @field_validator("icon")
    @classmethod
    def icon_check(cls, v):
        if v is None:
            return v

        if "/" not in v:
            raise ValueError("Icon should be a MIME string")

        if len(v.split("/")) != 2:
            raise ValueError("Icon needs two parts of MIME string")

        return v

    @field_validator("extra")
    @classmethod
    def extra_check(cls, value):
        limit = 400_000
        if value and value.metadata and len(json.dumps(value.metadata)) > limit:
            raise ValueError(f"metadata should be less than {limit} bytes when serialized to JSON")
        return value


class UpdateResourcePayload(BaseModel):
    title: Optional[str] = FieldDefaults.title
    summary: Optional[str] = FieldDefaults.summary
    slug: Optional[SlugString] = FieldDefaults.slug
    thumbnail: Optional[str] = FieldDefaults.thumbnail
    metadata: Optional[InputMetadata] = None
    usermetadata: Optional[UserMetadata] = FieldDefaults.usermetadata_create_or_update
    fieldmetadata: Optional[List[UserFieldMetadata]] = FieldDefaults.fieldmetadata_create_or_update
    origin: Optional[Origin] = FieldDefaults.origin_create_or_update
    extra: Optional[Extra] = FieldDefaults.extra_create_or_update
    files: Dict[FieldIdString, FileField] = FieldDefaults.files
    links: Dict[FieldIdString, LinkField] = FieldDefaults.links
    texts: Dict[FieldIdString, TextField] = FieldDefaults.texts
    conversations: Dict[FieldIdString, InputConversationField] = FieldDefaults.conversations
    processing_options: Optional[PushProcessingOptions] = FieldDefaults.processing_options
    security: Optional[ResourceSecurity] = FieldDefaults.security


class ResourceCreated(BaseModel):
    uuid: str
    elapsed: Optional[float] = None
    seqid: Optional[int] = None


class ResourceUpdated(BaseModel):
    seqid: Optional[int] = None


class ResourceFieldAdded(BaseModel):
    seqid: Optional[int] = None


class ResourceDeleted(BaseModel):
    seqid: Optional[int] = None


ComingResourcePayload = Union[CreateResourcePayload, UpdateResourcePayload]


class ResourceFileUploaded(BaseModel):
    seqid: Optional[int] = None
    uuid: Optional[str] = None
    field_id: Optional[FieldIdString] = None
