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
import google.protobuf.timestamp_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _KBSource:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _KBSourceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_KBSource.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    HOSTED: _KBSource.ValueType  # 0
    ONPREM: _KBSource.ValueType  # 1

class KBSource(_KBSource, metaclass=_KBSourceEnumTypeWrapper): ...

HOSTED: KBSource.ValueType  # 0
ONPREM: KBSource.ValueType  # 1
global___KBSource = KBSource

class _Service:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ServiceEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Service.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    PREDICT: _Service.ValueType  # 0
    PROCESSING: _Service.ValueType  # 1
    NUCLIA_DB: _Service.ValueType  # 2
    TASK: _Service.ValueType  # 3

class Service(_Service, metaclass=_ServiceEnumTypeWrapper): ...

PREDICT: Service.ValueType  # 0
PROCESSING: Service.ValueType  # 1
NUCLIA_DB: Service.ValueType  # 2
TASK: Service.ValueType  # 3
global___Service = Service

class _SearchType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SearchTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SearchType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SEARCH: _SearchType.ValueType  # 0
    SUGGEST: _SearchType.ValueType  # 1

class SearchType(_SearchType, metaclass=_SearchTypeEnumTypeWrapper): ...

SEARCH: SearchType.ValueType  # 0
SUGGEST: SearchType.ValueType  # 1
global___SearchType = SearchType

class _PredictType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PredictTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PredictType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    SENTENCE: _PredictType.ValueType  # 0
    TOKEN: _PredictType.ValueType  # 1
    QUESTION_ANSWER: _PredictType.ValueType  # 2
    REPHRASE: _PredictType.ValueType  # 3
    SUMMARIZE: _PredictType.ValueType  # 4
    EXTRACT_TABLES: _PredictType.ValueType  # 5
    RERANK: _PredictType.ValueType  # 6
    RELATIONS: _PredictType.ValueType  # 7
    SPEECH: _PredictType.ValueType  # 8
    CAPTION: _PredictType.ValueType  # 9
    DA_LABELS: _PredictType.ValueType  # 10
    DA_GRAPH: _PredictType.ValueType  # 11
    DA_ASK: _PredictType.ValueType  # 12
    DA_QA: _PredictType.ValueType  # 13

class PredictType(_PredictType, metaclass=_PredictTypeEnumTypeWrapper): ...

SENTENCE: PredictType.ValueType  # 0
TOKEN: PredictType.ValueType  # 1
QUESTION_ANSWER: PredictType.ValueType  # 2
REPHRASE: PredictType.ValueType  # 3
SUMMARIZE: PredictType.ValueType  # 4
EXTRACT_TABLES: PredictType.ValueType  # 5
RERANK: PredictType.ValueType  # 6
RELATIONS: PredictType.ValueType  # 7
SPEECH: PredictType.ValueType  # 8
CAPTION: PredictType.ValueType  # 9
DA_LABELS: PredictType.ValueType  # 10
DA_GRAPH: PredictType.ValueType  # 11
DA_ASK: PredictType.ValueType  # 12
DA_QA: PredictType.ValueType  # 13
global___PredictType = PredictType

class _ClientType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ClientTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ClientType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    API: _ClientType.ValueType  # 0
    WEB: _ClientType.ValueType  # 1
    WIDGET: _ClientType.ValueType  # 2
    DESKTOP: _ClientType.ValueType  # 3
    DASHBOARD: _ClientType.ValueType  # 4
    CHROME_EXTENSION: _ClientType.ValueType  # 5
    INTERNAL: _ClientType.ValueType  # 6

class ClientType(_ClientType, metaclass=_ClientTypeEnumTypeWrapper): ...

API: ClientType.ValueType  # 0
WEB: ClientType.ValueType  # 1
WIDGET: ClientType.ValueType  # 2
DESKTOP: ClientType.ValueType  # 3
DASHBOARD: ClientType.ValueType  # 4
CHROME_EXTENSION: ClientType.ValueType  # 5
INTERNAL: ClientType.ValueType  # 6
global___ClientType = ClientType

@typing.final
class Process(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_FIELD_NUMBER: builtins.int
    SLOW_PROCESSING_TIME_FIELD_NUMBER: builtins.int
    PRE_PROCESSING_TIME_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    CHARS_FIELD_NUMBER: builtins.int
    MEDIA_SECONDS_FIELD_NUMBER: builtins.int
    PAGES_FIELD_NUMBER: builtins.int
    PARAGRAPHS_FIELD_NUMBER: builtins.int
    MEDIA_FILES_FIELD_NUMBER: builtins.int
    NUM_PROCESSED_FIELD_NUMBER: builtins.int
    client: global___ClientType.ValueType
    slow_processing_time: builtins.float
    pre_processing_time: builtins.float
    bytes: builtins.int
    chars: builtins.int
    media_seconds: builtins.int
    pages: builtins.int
    paragraphs: builtins.int
    media_files: builtins.int
    num_processed: builtins.int
    def __init__(
        self,
        *,
        client: global___ClientType.ValueType = ...,
        slow_processing_time: builtins.float = ...,
        pre_processing_time: builtins.float = ...,
        bytes: builtins.int = ...,
        chars: builtins.int = ...,
        media_seconds: builtins.int = ...,
        pages: builtins.int = ...,
        paragraphs: builtins.int = ...,
        media_files: builtins.int = ...,
        num_processed: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["bytes", b"bytes", "chars", b"chars", "client", b"client", "media_files", b"media_files", "media_seconds", b"media_seconds", "num_processed", b"num_processed", "pages", b"pages", "paragraphs", b"paragraphs", "pre_processing_time", b"pre_processing_time", "slow_processing_time", b"slow_processing_time"]) -> None: ...

global___Process = Process

@typing.final
class Storage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARAGRAPHS_FIELD_NUMBER: builtins.int
    FIELDS_FIELD_NUMBER: builtins.int
    RESOURCES_FIELD_NUMBER: builtins.int
    BYTES_FIELD_NUMBER: builtins.int
    paragraphs: builtins.int
    fields: builtins.int
    resources: builtins.int
    bytes: builtins.int
    def __init__(
        self,
        *,
        paragraphs: builtins.int | None = ...,
        fields: builtins.int | None = ...,
        resources: builtins.int | None = ...,
        bytes: builtins.int | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_bytes", b"_bytes", "_fields", b"_fields", "_paragraphs", b"_paragraphs", "_resources", b"_resources", "bytes", b"bytes", "fields", b"fields", "paragraphs", b"paragraphs", "resources", b"resources"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_bytes", b"_bytes", "_fields", b"_fields", "_paragraphs", b"_paragraphs", "_resources", b"_resources", "bytes", b"bytes", "fields", b"fields", "paragraphs", b"paragraphs", "resources", b"resources"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_bytes", b"_bytes"]) -> typing.Literal["bytes"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_fields", b"_fields"]) -> typing.Literal["fields"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_paragraphs", b"_paragraphs"]) -> typing.Literal["paragraphs"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_resources", b"_resources"]) -> typing.Literal["resources"] | None: ...

global___Storage = Storage

@typing.final
class Search(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    TOKENS_FIELD_NUMBER: builtins.int
    NUM_SEARCHES_FIELD_NUMBER: builtins.int
    client: global___ClientType.ValueType
    type: global___SearchType.ValueType
    tokens: builtins.int
    num_searches: builtins.int
    def __init__(
        self,
        *,
        client: global___ClientType.ValueType = ...,
        type: global___SearchType.ValueType = ...,
        tokens: builtins.int = ...,
        num_searches: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client", b"client", "num_searches", b"num_searches", "tokens", b"tokens", "type", b"type"]) -> None: ...

global___Search = Search

@typing.final
class Predict(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLIENT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    MODEL_FIELD_NUMBER: builtins.int
    INPUT_FIELD_NUMBER: builtins.int
    OUTPUT_FIELD_NUMBER: builtins.int
    IMAGE_FIELD_NUMBER: builtins.int
    NUM_PREDICTS_FIELD_NUMBER: builtins.int
    client: global___ClientType.ValueType
    type: global___PredictType.ValueType
    model: builtins.str
    input: builtins.int
    output: builtins.int
    image: builtins.int
    num_predicts: builtins.int
    def __init__(
        self,
        *,
        client: global___ClientType.ValueType = ...,
        type: global___PredictType.ValueType = ...,
        model: builtins.str = ...,
        input: builtins.int = ...,
        output: builtins.int = ...,
        image: builtins.int = ...,
        num_predicts: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["client", b"client", "image", b"image", "input", b"input", "model", b"model", "num_predicts", b"num_predicts", "output", b"output", "type", b"type"]) -> None: ...

global___Predict = Predict

@typing.final
class KbUsage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERVICE_FIELD_NUMBER: builtins.int
    TIMESTAMP_FIELD_NUMBER: builtins.int
    ACCOUNT_ID_FIELD_NUMBER: builtins.int
    KB_ID_FIELD_NUMBER: builtins.int
    KB_SOURCE_FIELD_NUMBER: builtins.int
    PROCESSES_FIELD_NUMBER: builtins.int
    PREDICTS_FIELD_NUMBER: builtins.int
    SEARCHES_FIELD_NUMBER: builtins.int
    STORAGE_FIELD_NUMBER: builtins.int
    service: global___Service.ValueType
    """Identifiers"""
    account_id: builtins.str
    kb_id: builtins.str
    kb_source: global___KBSource.ValueType
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def processes(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Process]:
        """Data"""

    @property
    def predicts(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Predict]: ...
    @property
    def searches(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Search]: ...
    @property
    def storage(self) -> global___Storage: ...
    def __init__(
        self,
        *,
        service: global___Service.ValueType = ...,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        account_id: builtins.str | None = ...,
        kb_id: builtins.str | None = ...,
        kb_source: global___KBSource.ValueType = ...,
        processes: collections.abc.Iterable[global___Process] | None = ...,
        predicts: collections.abc.Iterable[global___Predict] | None = ...,
        searches: collections.abc.Iterable[global___Search] | None = ...,
        storage: global___Storage | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_account_id", b"_account_id", "_kb_id", b"_kb_id", "_storage", b"_storage", "account_id", b"account_id", "kb_id", b"kb_id", "storage", b"storage", "timestamp", b"timestamp"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_account_id", b"_account_id", "_kb_id", b"_kb_id", "_storage", b"_storage", "account_id", b"account_id", "kb_id", b"kb_id", "kb_source", b"kb_source", "predicts", b"predicts", "processes", b"processes", "searches", b"searches", "service", b"service", "storage", b"storage", "timestamp", b"timestamp"]) -> None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_account_id", b"_account_id"]) -> typing.Literal["account_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_kb_id", b"_kb_id"]) -> typing.Literal["kb_id"] | None: ...
    @typing.overload
    def WhichOneof(self, oneof_group: typing.Literal["_storage", b"_storage"]) -> typing.Literal["storage"] | None: ...

global___KbUsage = KbUsage

@typing.final
class KbUsageAggregated(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    KB_USAGES_FIELD_NUMBER: builtins.int
    @property
    def kb_usages(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___KbUsage]: ...
    def __init__(
        self,
        *,
        kb_usages: collections.abc.Iterable[global___KbUsage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["kb_usages", b"kb_usages"]) -> None: ...

global___KbUsageAggregated = KbUsageAggregated
