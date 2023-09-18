"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import nucliadb_protos.utils_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
from nucliadb_protos.utils_pb2 import (
    COSINE as COSINE,
    DOT as DOT,
    ExtractedText as ExtractedText,
    JoinGraph as JoinGraph,
    JoinGraphEdge as JoinGraphEdge,
    Relation as Relation,
    RelationMetadata as RelationMetadata,
    RelationNode as RelationNode,
    UserVector as UserVector,
    UserVectorSet as UserVectorSet,
    UserVectors as UserVectors,
    UserVectorsList as UserVectorsList,
    Vector as Vector,
    VectorObject as VectorObject,
    VectorSimilarity as VectorSimilarity,
    Vectors as Vectors,
)

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _KnowledgeBoxResponseStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _KnowledgeBoxResponseStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KnowledgeBoxResponseStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _KnowledgeBoxResponseStatus.ValueType  # 0
    CONFLICT: _KnowledgeBoxResponseStatus.ValueType  # 1
    NOTFOUND: _KnowledgeBoxResponseStatus.ValueType  # 2
    ERROR: _KnowledgeBoxResponseStatus.ValueType  # 3

class KnowledgeBoxResponseStatus(_KnowledgeBoxResponseStatus, metaclass=_KnowledgeBoxResponseStatusEnumTypeWrapper): ...

OK: KnowledgeBoxResponseStatus.ValueType  # 0
CONFLICT: KnowledgeBoxResponseStatus.ValueType  # 1
NOTFOUND: KnowledgeBoxResponseStatus.ValueType  # 2
ERROR: KnowledgeBoxResponseStatus.ValueType  # 3
global___KnowledgeBoxResponseStatus = KnowledgeBoxResponseStatus

@typing_extensions.final
class KnowledgeBoxID(google.protobuf.message.Message):
    """ID"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    slug: builtins.str
    uuid: builtins.str
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["slug", b"slug", "uuid", b"uuid"]) -> None: ...

global___KnowledgeBoxID = KnowledgeBoxID

@typing_extensions.final
class KnowledgeBox(google.protobuf.message.Message):
    """GET"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    slug: builtins.str
    uuid: builtins.str
    status: global___KnowledgeBoxResponseStatus.ValueType
    @property
    def config(self) -> global___KnowledgeBoxConfig: ...
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        uuid: builtins.str = ...,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
        config: global___KnowledgeBoxConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "slug", b"slug", "status", b"status", "uuid", b"uuid"]) -> None: ...

global___KnowledgeBox = KnowledgeBox

@typing_extensions.final
class KnowledgeBoxConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    ENABLED_FILTERS_FIELD_NUMBER: builtins.int
    ENABLED_INSIGHTS_FIELD_NUMBER: builtins.int
    SLUG_FIELD_NUMBER: builtins.int
    DISABLE_VECTORS_FIELD_NUMBER: builtins.int
    MIGRATION_VERSION_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    @property
    def enabled_filters(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    @property
    def enabled_insights(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    slug: builtins.str
    disable_vectors: builtins.bool
    migration_version: builtins.int
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        enabled_filters: collections.abc.Iterable[builtins.str] | None = ...,
        enabled_insights: collections.abc.Iterable[builtins.str] | None = ...,
        slug: builtins.str = ...,
        disable_vectors: builtins.bool = ...,
        migration_version: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["description", b"description", "disable_vectors", b"disable_vectors", "enabled_filters", b"enabled_filters", "enabled_insights", b"enabled_insights", "migration_version", b"migration_version", "slug", b"slug", "title", b"title"]) -> None: ...

global___KnowledgeBoxConfig = KnowledgeBoxConfig

@typing_extensions.final
class KnowledgeBoxNew(google.protobuf.message.Message):
    """NEW"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    FORCEUUID_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    VECTOR_DIMENSION_FIELD_NUMBER: builtins.int
    DEFAULT_MIN_SCORE_FIELD_NUMBER: builtins.int
    slug: builtins.str
    @property
    def config(self) -> global___KnowledgeBoxConfig: ...
    forceuuid: builtins.str
    similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType
    vector_dimension: builtins.int
    default_min_score: builtins.float
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        config: global___KnowledgeBoxConfig | None = ...,
        forceuuid: builtins.str = ...,
        similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType = ...,
        vector_dimension: builtins.int | None = ...,
        default_min_score: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "config", b"config", "default_min_score", b"default_min_score", "vector_dimension", b"vector_dimension"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "config", b"config", "default_min_score", b"default_min_score", "forceuuid", b"forceuuid", "similarity", b"similarity", "slug", b"slug", "vector_dimension", b"vector_dimension"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_default_min_score", b"_default_min_score"]) -> typing_extensions.Literal["default_min_score"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_vector_dimension", b"_vector_dimension"]) -> typing_extensions.Literal["vector_dimension"] | None: ...

global___KnowledgeBoxNew = KnowledgeBoxNew

@typing_extensions.final
class NewKnowledgeBoxResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    status: global___KnowledgeBoxResponseStatus.ValueType
    uuid: builtins.str
    def __init__(
        self,
        *,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status", "uuid", b"uuid"]) -> None: ...

global___NewKnowledgeBoxResponse = NewKnowledgeBoxResponse

@typing_extensions.final
class KnowledgeBoxPrefix(google.protobuf.message.Message):
    """SEARCH / LIST"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREFIX_FIELD_NUMBER: builtins.int
    prefix: builtins.str
    def __init__(
        self,
        *,
        prefix: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["prefix", b"prefix"]) -> None: ...

global___KnowledgeBoxPrefix = KnowledgeBoxPrefix

@typing_extensions.final
class KnowledgeBoxUpdate(google.protobuf.message.Message):
    """UPDATE"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SLUG_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    slug: builtins.str
    uuid: builtins.str
    @property
    def config(self) -> global___KnowledgeBoxConfig: ...
    def __init__(
        self,
        *,
        slug: builtins.str = ...,
        uuid: builtins.str = ...,
        config: global___KnowledgeBoxConfig | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "slug", b"slug", "uuid", b"uuid"]) -> None: ...

global___KnowledgeBoxUpdate = KnowledgeBoxUpdate

@typing_extensions.final
class UpdateKnowledgeBoxResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    UUID_FIELD_NUMBER: builtins.int
    status: global___KnowledgeBoxResponseStatus.ValueType
    uuid: builtins.str
    def __init__(
        self,
        *,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
        uuid: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status", "uuid", b"uuid"]) -> None: ...

global___UpdateKnowledgeBoxResponse = UpdateKnowledgeBoxResponse

@typing_extensions.final
class GCKnowledgeBoxResponse(google.protobuf.message.Message):
    """GC"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___GCKnowledgeBoxResponse = GCKnowledgeBoxResponse

@typing_extensions.final
class DeleteKnowledgeBoxResponse(google.protobuf.message.Message):
    """DELETE"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STATUS_FIELD_NUMBER: builtins.int
    status: global___KnowledgeBoxResponseStatus.ValueType
    def __init__(
        self,
        *,
        status: global___KnowledgeBoxResponseStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["status", b"status"]) -> None: ...

global___DeleteKnowledgeBoxResponse = DeleteKnowledgeBoxResponse

@typing_extensions.final
class CleanedKnowledgeBoxResponse(google.protobuf.message.Message):
    """Clean Index"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___CleanedKnowledgeBoxResponse = CleanedKnowledgeBoxResponse

@typing_extensions.final
class Label(google.protobuf.message.Message):
    """Labels on a Knowledge Box"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    RELATED_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    URI_FIELD_NUMBER: builtins.int
    title: builtins.str
    related: builtins.str
    text: builtins.str
    uri: builtins.str
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        related: builtins.str = ...,
        text: builtins.str = ...,
        uri: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["related", b"related", "text", b"text", "title", b"title", "uri", b"uri"]) -> None: ...

global___Label = Label

@typing_extensions.final
class LabelSet(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _LabelSetKind:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _LabelSetKindEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[LabelSet._LabelSetKind.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RESOURCES: LabelSet._LabelSetKind.ValueType  # 0
        PARAGRAPHS: LabelSet._LabelSetKind.ValueType  # 1
        SENTENCES: LabelSet._LabelSetKind.ValueType  # 2
        SELECTIONS: LabelSet._LabelSetKind.ValueType  # 3

    class LabelSetKind(_LabelSetKind, metaclass=_LabelSetKindEnumTypeWrapper): ...
    RESOURCES: LabelSet.LabelSetKind.ValueType  # 0
    PARAGRAPHS: LabelSet.LabelSetKind.ValueType  # 1
    SENTENCES: LabelSet.LabelSetKind.ValueType  # 2
    SELECTIONS: LabelSet.LabelSetKind.ValueType  # 3

    TITLE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    MULTIPLE_FIELD_NUMBER: builtins.int
    KIND_FIELD_NUMBER: builtins.int
    title: builtins.str
    color: builtins.str
    @property
    def labels(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Label]: ...
    multiple: builtins.bool
    @property
    def kind(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[global___LabelSet.LabelSetKind.ValueType]: ...
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        color: builtins.str = ...,
        labels: collections.abc.Iterable[global___Label] | None = ...,
        multiple: builtins.bool = ...,
        kind: collections.abc.Iterable[global___LabelSet.LabelSetKind.ValueType] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "kind", b"kind", "labels", b"labels", "multiple", b"multiple", "title", b"title"]) -> None: ...

global___LabelSet = LabelSet

@typing_extensions.final
class Labels(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class LabelsetEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___LabelSet: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___LabelSet | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    LABELSET_FIELD_NUMBER: builtins.int
    @property
    def labelset(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___LabelSet]: ...
    def __init__(
        self,
        *,
        labelset: collections.abc.Mapping[builtins.str, global___LabelSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["labelset", b"labelset"]) -> None: ...

global___Labels = Labels

@typing_extensions.final
class Entity(google.protobuf.message.Message):
    """Entities on a Knowledge Box"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALUE_FIELD_NUMBER: builtins.int
    REPRESENTS_FIELD_NUMBER: builtins.int
    MERGED_FIELD_NUMBER: builtins.int
    DELETED_FIELD_NUMBER: builtins.int
    value: builtins.str
    @property
    def represents(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    merged: builtins.bool
    deleted: builtins.bool
    def __init__(
        self,
        *,
        value: builtins.str = ...,
        represents: collections.abc.Iterable[builtins.str] | None = ...,
        merged: builtins.bool = ...,
        deleted: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["deleted", b"deleted", "merged", b"merged", "represents", b"represents", "value", b"value"]) -> None: ...

global___Entity = Entity

@typing_extensions.final
class EntitiesGroupSummary(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_NUMBER: builtins.int
    title: builtins.str
    color: builtins.str
    custom: builtins.bool
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        color: builtins.str = ...,
        custom: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "custom", b"custom", "title", b"title"]) -> None: ...

global___EntitiesGroupSummary = EntitiesGroupSummary

@typing_extensions.final
class EntitiesGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class EntitiesEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___Entity: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___Entity | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ENTITIES_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    CUSTOM_FIELD_NUMBER: builtins.int
    @property
    def entities(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___Entity]: ...
    title: builtins.str
    color: builtins.str
    custom: builtins.bool
    def __init__(
        self,
        *,
        entities: collections.abc.Mapping[builtins.str, global___Entity] | None = ...,
        title: builtins.str = ...,
        color: builtins.str = ...,
        custom: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["color", b"color", "custom", b"custom", "entities", b"entities", "title", b"title"]) -> None: ...

global___EntitiesGroup = EntitiesGroup

@typing_extensions.final
class DeletedEntitiesGroups(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ENTITIES_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def entities_groups(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        entities_groups: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities_groups", b"entities_groups"]) -> None: ...

global___DeletedEntitiesGroups = DeletedEntitiesGroups

@typing_extensions.final
class EntitiesGroups(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class EntitiesGroupsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___EntitiesGroup: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___EntitiesGroup | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    ENTITIES_GROUPS_FIELD_NUMBER: builtins.int
    @property
    def entities_groups(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___EntitiesGroup]: ...
    def __init__(
        self,
        *,
        entities_groups: collections.abc.Mapping[builtins.str, global___EntitiesGroup] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["entities_groups", b"entities_groups"]) -> None: ...

global___EntitiesGroups = EntitiesGroups

@typing_extensions.final
class VectorSet(google.protobuf.message.Message):
    """Vectorsets"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DIMENSION_FIELD_NUMBER: builtins.int
    SIMILARITY_FIELD_NUMBER: builtins.int
    dimension: builtins.int
    similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType
    def __init__(
        self,
        *,
        dimension: builtins.int = ...,
        similarity: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dimension", b"dimension", "similarity", b"similarity"]) -> None: ...

global___VectorSet = VectorSet

@typing_extensions.final
class VectorSets(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class VectorsetsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___VectorSet: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___VectorSet | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    VECTORSETS_FIELD_NUMBER: builtins.int
    @property
    def vectorsets(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___VectorSet]: ...
    def __init__(
        self,
        *,
        vectorsets: collections.abc.Mapping[builtins.str, global___VectorSet] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["vectorsets", b"vectorsets"]) -> None: ...

global___VectorSets = VectorSets

@typing_extensions.final
class TermSynonyms(google.protobuf.message.Message):
    """Synonyms of a Knowledge Box"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SYNONYMS_FIELD_NUMBER: builtins.int
    @property
    def synonyms(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        synonyms: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["synonyms", b"synonyms"]) -> None: ...

global___TermSynonyms = TermSynonyms

@typing_extensions.final
class Synonyms(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class TermsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        @property
        def value(self) -> global___TermSynonyms: ...
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: global___TermSynonyms | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["value", b"value"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["key", b"key", "value", b"value"]) -> None: ...

    TERMS_FIELD_NUMBER: builtins.int
    @property
    def terms(self) -> google.protobuf.internal.containers.MessageMap[builtins.str, global___TermSynonyms]: ...
    def __init__(
        self,
        *,
        terms: collections.abc.Mapping[builtins.str, global___TermSynonyms] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["terms", b"terms"]) -> None: ...

global___Synonyms = Synonyms

@typing_extensions.final
class SemanticModelMetadata(google.protobuf.message.Message):
    """Metadata of the model associated to the KB"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SIMILARITY_FUNCTION_FIELD_NUMBER: builtins.int
    VECTOR_DIMENSION_FIELD_NUMBER: builtins.int
    DEFAULT_MIN_SCORE_FIELD_NUMBER: builtins.int
    similarity_function: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType
    vector_dimension: builtins.int
    default_min_score: builtins.float
    def __init__(
        self,
        *,
        similarity_function: nucliadb_protos.utils_pb2.VectorSimilarity.ValueType = ...,
        vector_dimension: builtins.int | None = ...,
        default_min_score: builtins.float | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "default_min_score", b"default_min_score", "vector_dimension", b"vector_dimension"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_default_min_score", b"_default_min_score", "_vector_dimension", b"_vector_dimension", "default_min_score", b"default_min_score", "similarity_function", b"similarity_function", "vector_dimension", b"vector_dimension"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_default_min_score", b"_default_min_score"]) -> typing_extensions.Literal["default_min_score"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_vector_dimension", b"_vector_dimension"]) -> typing_extensions.Literal["vector_dimension"] | None: ...

global___SemanticModelMetadata = SemanticModelMetadata

@typing_extensions.final
class KBConfiguration(google.protobuf.message.Message):
    """Do not update this model without confirmation of internal Learning Config API"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEMANTIC_MODEL_FIELD_NUMBER: builtins.int
    GENERATIVE_MODEL_FIELD_NUMBER: builtins.int
    NER_MODEL_FIELD_NUMBER: builtins.int
    ANONYMIZATION_MODEL_FIELD_NUMBER: builtins.int
    VISUAL_LABELING_FIELD_NUMBER: builtins.int
    semantic_model: builtins.str
    generative_model: builtins.str
    ner_model: builtins.str
    anonymization_model: builtins.str
    visual_labeling: builtins.str
    def __init__(
        self,
        *,
        semantic_model: builtins.str = ...,
        generative_model: builtins.str = ...,
        ner_model: builtins.str = ...,
        anonymization_model: builtins.str = ...,
        visual_labeling: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["anonymization_model", b"anonymization_model", "generative_model", b"generative_model", "ner_model", b"ner_model", "semantic_model", b"semantic_model", "visual_labeling", b"visual_labeling"]) -> None: ...

global___KBConfiguration = KBConfiguration
