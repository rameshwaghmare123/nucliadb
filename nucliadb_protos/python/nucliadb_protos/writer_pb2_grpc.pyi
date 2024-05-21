"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import nucliadb_protos.knowledgebox_pb2
import nucliadb_protos.writer_pb2
import typing
from nucliadb_protos.audit_pb2 import (
    API as API,
    AuditField as AuditField,
    AuditKBCounter as AuditKBCounter,
    AuditRequest as AuditRequest,
    CHROME_EXTENSION as CHROME_EXTENSION,
    ChatAudit as ChatAudit,
    ChatContext as ChatContext,
    ClientType as ClientType,
    DASHBOARD as DASHBOARD,
    DESKTOP as DESKTOP,
    WEB as WEB,
    WIDGET as WIDGET,
)
from nucliadb_protos.knowledgebox_pb2 import (
    CONFLICT as CONFLICT,
    DeleteKnowledgeBoxResponse as DeleteKnowledgeBoxResponse,
    DeletedEntitiesGroups as DeletedEntitiesGroups,
    ERROR as ERROR,
    EntitiesGroup as EntitiesGroup,
    EntitiesGroupSummary as EntitiesGroupSummary,
    EntitiesGroups as EntitiesGroups,
    Entity as Entity,
    EntityGroupDuplicateIndex as EntityGroupDuplicateIndex,
    GCKnowledgeBoxResponse as GCKnowledgeBoxResponse,
    KBConfiguration as KBConfiguration,
    KnowledgeBoxConfig as KnowledgeBoxConfig,
    KnowledgeBoxID as KnowledgeBoxID,
    KnowledgeBoxNew as KnowledgeBoxNew,
    KnowledgeBoxResponseStatus as KnowledgeBoxResponseStatus,
    KnowledgeBoxUpdate as KnowledgeBoxUpdate,
    Label as Label,
    LabelSet as LabelSet,
    Labels as Labels,
    NOTFOUND as NOTFOUND,
    NewKnowledgeBoxResponse as NewKnowledgeBoxResponse,
    OK as OK,
    SemanticModelMetadata as SemanticModelMetadata,
    Synonyms as Synonyms,
    TermSynonyms as TermSynonyms,
    UpdateKnowledgeBoxResponse as UpdateKnowledgeBoxResponse,
    VectorSet as VectorSet,
    VectorSets as VectorSets,
)
from nucliadb_protos.noderesources_pb2 import (
    EmptyQuery as EmptyQuery,
    EmptyResponse as EmptyResponse,
    IndexMetadata as IndexMetadata,
    IndexParagraph as IndexParagraph,
    IndexParagraphs as IndexParagraphs,
    NodeMetadata as NodeMetadata,
    ParagraphMetadata as ParagraphMetadata,
    Position as Position,
    Representation as Representation,
    Resource as Resource,
    ResourceID as ResourceID,
    SentenceMetadata as SentenceMetadata,
    Shard as Shard,
    ShardCreated as ShardCreated,
    ShardId as ShardId,
    ShardIds as ShardIds,
    ShardMetadata as ShardMetadata,
    TextInformation as TextInformation,
    VectorSentence as VectorSentence,
    VectorSetID as VectorSetID,
    VectorSetList as VectorSetList,
    VectorsetSentences as VectorsetSentences,
)
from nucliadb_protos.resources_pb2 import (
    AllFieldIDs as AllFieldIDs,
    Answers as Answers,
    Basic as Basic,
    Block as Block,
    CONVERSATION as CONVERSATION,
    Classification as Classification,
    CloudFile as CloudFile,
    ComputedMetadata as ComputedMetadata,
    Conversation as Conversation,
    DATETIME as DATETIME,
    Entity as Entity,
    Extra as Extra,
    ExtractedTextWrapper as ExtractedTextWrapper,
    ExtractedVectorsWrapper as ExtractedVectorsWrapper,
    FILE as FILE,
    FieldClassifications as FieldClassifications,
    FieldComputedMetadata as FieldComputedMetadata,
    FieldComputedMetadataWrapper as FieldComputedMetadataWrapper,
    FieldConversation as FieldConversation,
    FieldDatetime as FieldDatetime,
    FieldFile as FieldFile,
    FieldID as FieldID,
    FieldKeywordset as FieldKeywordset,
    FieldLargeMetadata as FieldLargeMetadata,
    FieldLayout as FieldLayout,
    FieldLink as FieldLink,
    FieldMetadata as FieldMetadata,
    FieldQuestionAnswerWrapper as FieldQuestionAnswerWrapper,
    FieldText as FieldText,
    FieldType as FieldType,
    FileExtractedData as FileExtractedData,
    FilePages as FilePages,
    GENERIC as GENERIC,
    KEYWORDSET as KEYWORDSET,
    Keyword as Keyword,
    LAYOUT as LAYOUT,
    LINK as LINK,
    LargeComputedMetadata as LargeComputedMetadata,
    LargeComputedMetadataWrapper as LargeComputedMetadataWrapper,
    LayoutContent as LayoutContent,
    LinkExtractedData as LinkExtractedData,
    Message as Message,
    MessageContent as MessageContent,
    Metadata as Metadata,
    NestedListPosition as NestedListPosition,
    NestedPosition as NestedPosition,
    Origin as Origin,
    PageInformation as PageInformation,
    PagePositions as PagePositions,
    PageSelections as PageSelections,
    PageStructure as PageStructure,
    PageStructurePage as PageStructurePage,
    PageStructureToken as PageStructureToken,
    Paragraph as Paragraph,
    ParagraphAnnotation as ParagraphAnnotation,
    ParagraphRelations as ParagraphRelations,
    Position as Position,
    Positions as Positions,
    Question as Question,
    QuestionAnswer as QuestionAnswer,
    QuestionAnswerAnnotation as QuestionAnswerAnnotation,
    QuestionAnswers as QuestionAnswers,
    Relations as Relations,
    Representation as Representation,
    RowsPreview as RowsPreview,
    Sentence as Sentence,
    TEXT as TEXT,
    TokenSplit as TokenSplit,
    UserFieldMetadata as UserFieldMetadata,
    UserMetadata as UserMetadata,
    UserVectorsWrapper as UserVectorsWrapper,
    VisualSelection as VisualSelection,
)

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class WriterStub:
    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    NewKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxNew,
        nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse,
    ]

    DeleteKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse,
    ]

    UpdateKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxUpdate,
        nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse,
    ]

    GCKnowledgeBox: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        nucliadb_protos.knowledgebox_pb2.GCKnowledgeBoxResponse,
    ]

    SetVectors: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetVectorsRequest,
        nucliadb_protos.writer_pb2.SetVectorsResponse,
    ]

    ProcessMessage: grpc.StreamUnaryMultiCallable[
        nucliadb_protos.writer_pb2.BrokerMessage,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    GetLabels: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetLabelsRequest,
        nucliadb_protos.writer_pb2.GetLabelsResponse,
    ]
    """Labels"""

    GetLabelSet: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetLabelSetRequest,
        nucliadb_protos.writer_pb2.GetLabelSetResponse,
    ]

    SetLabels: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetLabelsRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    DelLabels: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelLabelsRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    NewEntitiesGroup: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.NewEntitiesGroupResponse,
    ]
    """Entities"""

    GetEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesRequest,
        nucliadb_protos.writer_pb2.GetEntitiesResponse,
    ]

    GetEntitiesGroup: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.GetEntitiesGroupResponse,
    ]

    ListEntitiesGroups: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListEntitiesGroupsRequest,
        nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse,
    ]

    SetEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    UpdateEntitiesGroup: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse,
    ]

    DelEntities: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    Status: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.WriterStatusRequest,
        nucliadb_protos.writer_pb2.WriterStatusResponse,
    ]

    ListMembers: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListMembersRequest,
        nucliadb_protos.writer_pb2.ListMembersResponse,
    ]

    Index: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    ReIndex: grpc.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    DownloadFile: grpc.UnaryStreamMultiCallable[
        nucliadb_protos.writer_pb2.FileRequest,
        nucliadb_protos.writer_pb2.BinaryData,
    ]

    UploadFile: grpc.StreamUnaryMultiCallable[
        nucliadb_protos.writer_pb2.UploadBinaryData,
        nucliadb_protos.writer_pb2.FileUploaded,
    ]

class WriterAsyncStub:
    NewKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxNew,
        nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse,
    ]

    DeleteKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse,
    ]

    UpdateKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxUpdate,
        nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse,
    ]

    GCKnowledgeBox: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        nucliadb_protos.knowledgebox_pb2.GCKnowledgeBoxResponse,
    ]

    SetVectors: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetVectorsRequest,
        nucliadb_protos.writer_pb2.SetVectorsResponse,
    ]

    ProcessMessage: grpc.aio.StreamUnaryMultiCallable[
        nucliadb_protos.writer_pb2.BrokerMessage,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    GetLabels: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetLabelsRequest,
        nucliadb_protos.writer_pb2.GetLabelsResponse,
    ]
    """Labels"""

    GetLabelSet: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetLabelSetRequest,
        nucliadb_protos.writer_pb2.GetLabelSetResponse,
    ]

    SetLabels: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetLabelsRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    DelLabels: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelLabelsRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    NewEntitiesGroup: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.NewEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.NewEntitiesGroupResponse,
    ]
    """Entities"""

    GetEntities: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesRequest,
        nucliadb_protos.writer_pb2.GetEntitiesResponse,
    ]

    GetEntitiesGroup: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.GetEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.GetEntitiesGroupResponse,
    ]

    ListEntitiesGroups: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListEntitiesGroupsRequest,
        nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse,
    ]

    SetEntities: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.SetEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    UpdateEntitiesGroup: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupRequest,
        nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse,
    ]

    DelEntities: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.DelEntitiesRequest,
        nucliadb_protos.writer_pb2.OpStatusWriter,
    ]

    Status: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.WriterStatusRequest,
        nucliadb_protos.writer_pb2.WriterStatusResponse,
    ]

    ListMembers: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.ListMembersRequest,
        nucliadb_protos.writer_pb2.ListMembersResponse,
    ]

    Index: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    ReIndex: grpc.aio.UnaryUnaryMultiCallable[
        nucliadb_protos.writer_pb2.IndexResource,
        nucliadb_protos.writer_pb2.IndexStatus,
    ]

    DownloadFile: grpc.aio.UnaryStreamMultiCallable[
        nucliadb_protos.writer_pb2.FileRequest,
        nucliadb_protos.writer_pb2.BinaryData,
    ]

    UploadFile: grpc.aio.StreamUnaryMultiCallable[
        nucliadb_protos.writer_pb2.UploadBinaryData,
        nucliadb_protos.writer_pb2.FileUploaded,
    ]

class WriterServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def NewKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxNew,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.NewKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def DeleteKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.DeleteKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def UpdateKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxUpdate,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.UpdateKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def GCKnowledgeBox(
        self,
        request: nucliadb_protos.knowledgebox_pb2.KnowledgeBoxID,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.knowledgebox_pb2.GCKnowledgeBoxResponse, collections.abc.Awaitable[nucliadb_protos.knowledgebox_pb2.GCKnowledgeBoxResponse]]: ...

    @abc.abstractmethod
    def SetVectors(
        self,
        request: nucliadb_protos.writer_pb2.SetVectorsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.SetVectorsResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.SetVectorsResponse]]: ...

    @abc.abstractmethod
    def ProcessMessage(
        self,
        request_iterator: _MaybeAsyncIterator[nucliadb_protos.writer_pb2.BrokerMessage],
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def GetLabels(
        self,
        request: nucliadb_protos.writer_pb2.GetLabelsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.GetLabelsResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.GetLabelsResponse]]:
        """Labels"""

    @abc.abstractmethod
    def GetLabelSet(
        self,
        request: nucliadb_protos.writer_pb2.GetLabelSetRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.GetLabelSetResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.GetLabelSetResponse]]: ...

    @abc.abstractmethod
    def SetLabels(
        self,
        request: nucliadb_protos.writer_pb2.SetLabelsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def DelLabels(
        self,
        request: nucliadb_protos.writer_pb2.DelLabelsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def NewEntitiesGroup(
        self,
        request: nucliadb_protos.writer_pb2.NewEntitiesGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.NewEntitiesGroupResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.NewEntitiesGroupResponse]]:
        """Entities"""

    @abc.abstractmethod
    def GetEntities(
        self,
        request: nucliadb_protos.writer_pb2.GetEntitiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.GetEntitiesResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.GetEntitiesResponse]]: ...

    @abc.abstractmethod
    def GetEntitiesGroup(
        self,
        request: nucliadb_protos.writer_pb2.GetEntitiesGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.GetEntitiesGroupResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.GetEntitiesGroupResponse]]: ...

    @abc.abstractmethod
    def ListEntitiesGroups(
        self,
        request: nucliadb_protos.writer_pb2.ListEntitiesGroupsRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.ListEntitiesGroupsResponse]]: ...

    @abc.abstractmethod
    def SetEntities(
        self,
        request: nucliadb_protos.writer_pb2.SetEntitiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def UpdateEntitiesGroup(
        self,
        request: nucliadb_protos.writer_pb2.UpdateEntitiesGroupRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.UpdateEntitiesGroupResponse]]: ...

    @abc.abstractmethod
    def DelEntities(
        self,
        request: nucliadb_protos.writer_pb2.DelEntitiesRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.OpStatusWriter, collections.abc.Awaitable[nucliadb_protos.writer_pb2.OpStatusWriter]]: ...

    @abc.abstractmethod
    def Status(
        self,
        request: nucliadb_protos.writer_pb2.WriterStatusRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.WriterStatusResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.WriterStatusResponse]]: ...

    @abc.abstractmethod
    def ListMembers(
        self,
        request: nucliadb_protos.writer_pb2.ListMembersRequest,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.ListMembersResponse, collections.abc.Awaitable[nucliadb_protos.writer_pb2.ListMembersResponse]]: ...

    @abc.abstractmethod
    def Index(
        self,
        request: nucliadb_protos.writer_pb2.IndexResource,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.IndexStatus, collections.abc.Awaitable[nucliadb_protos.writer_pb2.IndexStatus]]: ...

    @abc.abstractmethod
    def ReIndex(
        self,
        request: nucliadb_protos.writer_pb2.IndexResource,
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.IndexStatus, collections.abc.Awaitable[nucliadb_protos.writer_pb2.IndexStatus]]: ...

    @abc.abstractmethod
    def DownloadFile(
        self,
        request: nucliadb_protos.writer_pb2.FileRequest,
        context: _ServicerContext,
    ) -> typing.Union[collections.abc.Iterator[nucliadb_protos.writer_pb2.BinaryData], collections.abc.AsyncIterator[nucliadb_protos.writer_pb2.BinaryData]]: ...

    @abc.abstractmethod
    def UploadFile(
        self,
        request_iterator: _MaybeAsyncIterator[nucliadb_protos.writer_pb2.UploadBinaryData],
        context: _ServicerContext,
    ) -> typing.Union[nucliadb_protos.writer_pb2.FileUploaded, collections.abc.Awaitable[nucliadb_protos.writer_pb2.FileUploaded]]: ...

def add_WriterServicer_to_server(servicer: WriterServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
