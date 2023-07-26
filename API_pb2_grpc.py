# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import API_pb2 as API__pb2


class askEOGStub(object):
    """Отсутствует передача файлов, возможно добавить позже (подсказки: https://github.com/gooooloo/grpc-file-transfer/tree/master)

    Фукнции запроса к приложению и возращения данных клиенту
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/eog_serve.askEOG/Get',
                request_serializer=API__pb2.SearchSlice.SerializeToString,
                response_deserializer=API__pb2.SearchResults.FromString,
                )
        self.Get_UStream = channel.unary_stream(
                '/eog_serve.askEOG/Get_UStream',
                request_serializer=API__pb2.SearchSlice.SerializeToString,
                response_deserializer=API__pb2.Persona.FromString,
                )
        self.Get_BStream = channel.stream_stream(
                '/eog_serve.askEOG/Get_BStream',
                request_serializer=API__pb2.SearchSlice.SerializeToString,
                response_deserializer=API__pb2.Persona.FromString,
                )


class askEOGServicer(object):
    """Отсутствует передача файлов, возможно добавить позже (подсказки: https://github.com/gooooloo/grpc-file-transfer/tree/master)

    Фукнции запроса к приложению и возращения данных клиенту
    """

    def Get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_UStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Get_BStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_askEOGServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=API__pb2.SearchSlice.FromString,
                    response_serializer=API__pb2.SearchResults.SerializeToString,
            ),
            'Get_UStream': grpc.unary_stream_rpc_method_handler(
                    servicer.Get_UStream,
                    request_deserializer=API__pb2.SearchSlice.FromString,
                    response_serializer=API__pb2.Persona.SerializeToString,
            ),
            'Get_BStream': grpc.stream_stream_rpc_method_handler(
                    servicer.Get_BStream,
                    request_deserializer=API__pb2.SearchSlice.FromString,
                    response_serializer=API__pb2.Persona.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'eog_serve.askEOG', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class askEOG(object):
    """Отсутствует передача файлов, возможно добавить позже (подсказки: https://github.com/gooooloo/grpc-file-transfer/tree/master)

    Фукнции запроса к приложению и возращения данных клиенту
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/eog_serve.askEOG/Get',
            API__pb2.SearchSlice.SerializeToString,
            API__pb2.SearchResults.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get_UStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/eog_serve.askEOG/Get_UStream',
            API__pb2.SearchSlice.SerializeToString,
            API__pb2.Persona.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Get_BStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/eog_serve.askEOG/Get_BStream',
            API__pb2.SearchSlice.SerializeToString,
            API__pb2.Persona.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)