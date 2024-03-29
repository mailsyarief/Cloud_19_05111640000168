# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import phonebook_pb2 as phonebook__pb2


class PhonebookStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetDataById = channel.unary_unary(
        '/Phonebook/GetDataById',
        request_serializer=phonebook__pb2.Request.SerializeToString,
        response_deserializer=phonebook__pb2.Response.FromString,
        )
    self.GetDataAll = channel.unary_stream(
        '/Phonebook/GetDataAll',
        request_serializer=phonebook__pb2.Request.SerializeToString,
        response_deserializer=phonebook__pb2.Response.FromString,
        )


class PhonebookServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetDataById(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetDataAll(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PhonebookServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetDataById': grpc.unary_unary_rpc_method_handler(
          servicer.GetDataById,
          request_deserializer=phonebook__pb2.Request.FromString,
          response_serializer=phonebook__pb2.Response.SerializeToString,
      ),
      'GetDataAll': grpc.unary_stream_rpc_method_handler(
          servicer.GetDataAll,
          request_deserializer=phonebook__pb2.Request.FromString,
          response_serializer=phonebook__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Phonebook', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
