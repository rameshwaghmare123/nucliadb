# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from nucliadb_protos import knowledgebox_pb2 as nucliadb__protos_dot_knowledgebox__pb2
from nucliadb_protos import writer_pb2 as nucliadb__protos_dot_writer__pb2


class WriterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.NewKnowledgeBox = channel.unary_unary(
                '/fdbwriter.Writer/NewKnowledgeBox',
                request_serializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxNew.SerializeToString,
                response_deserializer=nucliadb__protos_dot_knowledgebox__pb2.NewKnowledgeBoxResponse.FromString,
                )
        self.DeleteKnowledgeBox = channel.unary_unary(
                '/fdbwriter.Writer/DeleteKnowledgeBox',
                request_serializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxID.SerializeToString,
                response_deserializer=nucliadb__protos_dot_knowledgebox__pb2.DeleteKnowledgeBoxResponse.FromString,
                )
        self.UpdateKnowledgeBox = channel.unary_unary(
                '/fdbwriter.Writer/UpdateKnowledgeBox',
                request_serializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxUpdate.SerializeToString,
                response_deserializer=nucliadb__protos_dot_knowledgebox__pb2.UpdateKnowledgeBoxResponse.FromString,
                )
        self.GCKnowledgeBox = channel.unary_unary(
                '/fdbwriter.Writer/GCKnowledgeBox',
                request_serializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxID.SerializeToString,
                response_deserializer=nucliadb__protos_dot_knowledgebox__pb2.GCKnowledgeBoxResponse.FromString,
                )
        self.SetVectors = channel.unary_unary(
                '/fdbwriter.Writer/SetVectors',
                request_serializer=nucliadb__protos_dot_writer__pb2.SetVectorsRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.SetVectorsResponse.FromString,
                )
        self.ProcessMessage = channel.stream_unary(
                '/fdbwriter.Writer/ProcessMessage',
                request_serializer=nucliadb__protos_dot_writer__pb2.BrokerMessage.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
                )
        self.GetLabels = channel.unary_unary(
                '/fdbwriter.Writer/GetLabels',
                request_serializer=nucliadb__protos_dot_writer__pb2.GetLabelsRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.GetLabelsResponse.FromString,
                )
        self.GetLabelSet = channel.unary_unary(
                '/fdbwriter.Writer/GetLabelSet',
                request_serializer=nucliadb__protos_dot_writer__pb2.GetLabelSetRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.GetLabelSetResponse.FromString,
                )
        self.SetLabels = channel.unary_unary(
                '/fdbwriter.Writer/SetLabels',
                request_serializer=nucliadb__protos_dot_writer__pb2.SetLabelsRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
                )
        self.DelLabels = channel.unary_unary(
                '/fdbwriter.Writer/DelLabels',
                request_serializer=nucliadb__protos_dot_writer__pb2.DelLabelsRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
                )
        self.NewEntitiesGroup = channel.unary_unary(
                '/fdbwriter.Writer/NewEntitiesGroup',
                request_serializer=nucliadb__protos_dot_writer__pb2.NewEntitiesGroupRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.NewEntitiesGroupResponse.FromString,
                )
        self.GetEntities = channel.unary_unary(
                '/fdbwriter.Writer/GetEntities',
                request_serializer=nucliadb__protos_dot_writer__pb2.GetEntitiesRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.GetEntitiesResponse.FromString,
                )
        self.GetEntitiesGroup = channel.unary_unary(
                '/fdbwriter.Writer/GetEntitiesGroup',
                request_serializer=nucliadb__protos_dot_writer__pb2.GetEntitiesGroupRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.GetEntitiesGroupResponse.FromString,
                )
        self.ListEntitiesGroups = channel.unary_unary(
                '/fdbwriter.Writer/ListEntitiesGroups',
                request_serializer=nucliadb__protos_dot_writer__pb2.ListEntitiesGroupsRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.ListEntitiesGroupsResponse.FromString,
                )
        self.SetEntities = channel.unary_unary(
                '/fdbwriter.Writer/SetEntities',
                request_serializer=nucliadb__protos_dot_writer__pb2.SetEntitiesRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
                )
        self.UpdateEntitiesGroup = channel.unary_unary(
                '/fdbwriter.Writer/UpdateEntitiesGroup',
                request_serializer=nucliadb__protos_dot_writer__pb2.UpdateEntitiesGroupRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.UpdateEntitiesGroupResponse.FromString,
                )
        self.DelEntities = channel.unary_unary(
                '/fdbwriter.Writer/DelEntities',
                request_serializer=nucliadb__protos_dot_writer__pb2.DelEntitiesRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
                )
        self.Status = channel.unary_unary(
                '/fdbwriter.Writer/Status',
                request_serializer=nucliadb__protos_dot_writer__pb2.WriterStatusRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.WriterStatusResponse.FromString,
                )
        self.ListMembers = channel.unary_unary(
                '/fdbwriter.Writer/ListMembers',
                request_serializer=nucliadb__protos_dot_writer__pb2.ListMembersRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.ListMembersResponse.FromString,
                )
        self.Index = channel.unary_unary(
                '/fdbwriter.Writer/Index',
                request_serializer=nucliadb__protos_dot_writer__pb2.IndexResource.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.IndexStatus.FromString,
                )
        self.ReIndex = channel.unary_unary(
                '/fdbwriter.Writer/ReIndex',
                request_serializer=nucliadb__protos_dot_writer__pb2.IndexResource.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.IndexStatus.FromString,
                )
        self.DownloadFile = channel.unary_stream(
                '/fdbwriter.Writer/DownloadFile',
                request_serializer=nucliadb__protos_dot_writer__pb2.FileRequest.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.BinaryData.FromString,
                )
        self.UploadFile = channel.stream_unary(
                '/fdbwriter.Writer/UploadFile',
                request_serializer=nucliadb__protos_dot_writer__pb2.UploadBinaryData.SerializeToString,
                response_deserializer=nucliadb__protos_dot_writer__pb2.FileUploaded.FromString,
                )


class WriterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def NewKnowledgeBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteKnowledgeBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateKnowledgeBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GCKnowledgeBox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetVectors(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessMessage(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLabels(self, request, context):
        """Labels
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLabelSet(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetLabels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelLabels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NewEntitiesGroup(self, request, context):
        """Entities
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetEntitiesGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListEntitiesGroups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetEntities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateEntitiesGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DelEntities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Status(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMembers(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UploadFile(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WriterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'NewKnowledgeBox': grpc.unary_unary_rpc_method_handler(
                    servicer.NewKnowledgeBox,
                    request_deserializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxNew.FromString,
                    response_serializer=nucliadb__protos_dot_knowledgebox__pb2.NewKnowledgeBoxResponse.SerializeToString,
            ),
            'DeleteKnowledgeBox': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteKnowledgeBox,
                    request_deserializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxID.FromString,
                    response_serializer=nucliadb__protos_dot_knowledgebox__pb2.DeleteKnowledgeBoxResponse.SerializeToString,
            ),
            'UpdateKnowledgeBox': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateKnowledgeBox,
                    request_deserializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxUpdate.FromString,
                    response_serializer=nucliadb__protos_dot_knowledgebox__pb2.UpdateKnowledgeBoxResponse.SerializeToString,
            ),
            'GCKnowledgeBox': grpc.unary_unary_rpc_method_handler(
                    servicer.GCKnowledgeBox,
                    request_deserializer=nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxID.FromString,
                    response_serializer=nucliadb__protos_dot_knowledgebox__pb2.GCKnowledgeBoxResponse.SerializeToString,
            ),
            'SetVectors': grpc.unary_unary_rpc_method_handler(
                    servicer.SetVectors,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.SetVectorsRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.SetVectorsResponse.SerializeToString,
            ),
            'ProcessMessage': grpc.stream_unary_rpc_method_handler(
                    servicer.ProcessMessage,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.BrokerMessage.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.SerializeToString,
            ),
            'GetLabels': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLabels,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.GetLabelsRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.GetLabelsResponse.SerializeToString,
            ),
            'GetLabelSet': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLabelSet,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.GetLabelSetRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.GetLabelSetResponse.SerializeToString,
            ),
            'SetLabels': grpc.unary_unary_rpc_method_handler(
                    servicer.SetLabels,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.SetLabelsRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.SerializeToString,
            ),
            'DelLabels': grpc.unary_unary_rpc_method_handler(
                    servicer.DelLabels,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.DelLabelsRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.SerializeToString,
            ),
            'NewEntitiesGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.NewEntitiesGroup,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.NewEntitiesGroupRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.NewEntitiesGroupResponse.SerializeToString,
            ),
            'GetEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntities,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.GetEntitiesRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.GetEntitiesResponse.SerializeToString,
            ),
            'GetEntitiesGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntitiesGroup,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.GetEntitiesGroupRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.GetEntitiesGroupResponse.SerializeToString,
            ),
            'ListEntitiesGroups': grpc.unary_unary_rpc_method_handler(
                    servicer.ListEntitiesGroups,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.ListEntitiesGroupsRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.ListEntitiesGroupsResponse.SerializeToString,
            ),
            'SetEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.SetEntities,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.SetEntitiesRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.SerializeToString,
            ),
            'UpdateEntitiesGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateEntitiesGroup,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.UpdateEntitiesGroupRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.UpdateEntitiesGroupResponse.SerializeToString,
            ),
            'DelEntities': grpc.unary_unary_rpc_method_handler(
                    servicer.DelEntities,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.DelEntitiesRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.OpStatusWriter.SerializeToString,
            ),
            'Status': grpc.unary_unary_rpc_method_handler(
                    servicer.Status,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.WriterStatusRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.WriterStatusResponse.SerializeToString,
            ),
            'ListMembers': grpc.unary_unary_rpc_method_handler(
                    servicer.ListMembers,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.ListMembersRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.ListMembersResponse.SerializeToString,
            ),
            'Index': grpc.unary_unary_rpc_method_handler(
                    servicer.Index,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.IndexResource.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.IndexStatus.SerializeToString,
            ),
            'ReIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.ReIndex,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.IndexResource.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.IndexStatus.SerializeToString,
            ),
            'DownloadFile': grpc.unary_stream_rpc_method_handler(
                    servicer.DownloadFile,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.FileRequest.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.BinaryData.SerializeToString,
            ),
            'UploadFile': grpc.stream_unary_rpc_method_handler(
                    servicer.UploadFile,
                    request_deserializer=nucliadb__protos_dot_writer__pb2.UploadBinaryData.FromString,
                    response_serializer=nucliadb__protos_dot_writer__pb2.FileUploaded.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'fdbwriter.Writer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Writer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def NewKnowledgeBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/NewKnowledgeBox',
            nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxNew.SerializeToString,
            nucliadb__protos_dot_knowledgebox__pb2.NewKnowledgeBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteKnowledgeBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/DeleteKnowledgeBox',
            nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxID.SerializeToString,
            nucliadb__protos_dot_knowledgebox__pb2.DeleteKnowledgeBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateKnowledgeBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/UpdateKnowledgeBox',
            nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxUpdate.SerializeToString,
            nucliadb__protos_dot_knowledgebox__pb2.UpdateKnowledgeBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GCKnowledgeBox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/GCKnowledgeBox',
            nucliadb__protos_dot_knowledgebox__pb2.KnowledgeBoxID.SerializeToString,
            nucliadb__protos_dot_knowledgebox__pb2.GCKnowledgeBoxResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetVectors(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/SetVectors',
            nucliadb__protos_dot_writer__pb2.SetVectorsRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.SetVectorsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessMessage(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/fdbwriter.Writer/ProcessMessage',
            nucliadb__protos_dot_writer__pb2.BrokerMessage.SerializeToString,
            nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLabels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/GetLabels',
            nucliadb__protos_dot_writer__pb2.GetLabelsRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.GetLabelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLabelSet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/GetLabelSet',
            nucliadb__protos_dot_writer__pb2.GetLabelSetRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.GetLabelSetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetLabels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/SetLabels',
            nucliadb__protos_dot_writer__pb2.SetLabelsRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelLabels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/DelLabels',
            nucliadb__protos_dot_writer__pb2.DelLabelsRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NewEntitiesGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/NewEntitiesGroup',
            nucliadb__protos_dot_writer__pb2.NewEntitiesGroupRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.NewEntitiesGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEntities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/GetEntities',
            nucliadb__protos_dot_writer__pb2.GetEntitiesRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.GetEntitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetEntitiesGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/GetEntitiesGroup',
            nucliadb__protos_dot_writer__pb2.GetEntitiesGroupRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.GetEntitiesGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListEntitiesGroups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/ListEntitiesGroups',
            nucliadb__protos_dot_writer__pb2.ListEntitiesGroupsRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.ListEntitiesGroupsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetEntities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/SetEntities',
            nucliadb__protos_dot_writer__pb2.SetEntitiesRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateEntitiesGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/UpdateEntitiesGroup',
            nucliadb__protos_dot_writer__pb2.UpdateEntitiesGroupRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.UpdateEntitiesGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DelEntities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/DelEntities',
            nucliadb__protos_dot_writer__pb2.DelEntitiesRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.OpStatusWriter.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Status(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/Status',
            nucliadb__protos_dot_writer__pb2.WriterStatusRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.WriterStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListMembers(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/ListMembers',
            nucliadb__protos_dot_writer__pb2.ListMembersRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.ListMembersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/Index',
            nucliadb__protos_dot_writer__pb2.IndexResource.SerializeToString,
            nucliadb__protos_dot_writer__pb2.IndexStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/fdbwriter.Writer/ReIndex',
            nucliadb__protos_dot_writer__pb2.IndexResource.SerializeToString,
            nucliadb__protos_dot_writer__pb2.IndexStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DownloadFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/fdbwriter.Writer/DownloadFile',
            nucliadb__protos_dot_writer__pb2.FileRequest.SerializeToString,
            nucliadb__protos_dot_writer__pb2.BinaryData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UploadFile(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/fdbwriter.Writer/UploadFile',
            nucliadb__protos_dot_writer__pb2.UploadBinaryData.SerializeToString,
            nucliadb__protos_dot_writer__pb2.FileUploaded.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
