import grpc
import API_pb2
import API_pb2_grpc
import bot_handler


import time
from concurrent import futures

class EOGServicer(API_pb2_grpc.EOGServicer):
    def GET(self, request, context):
        return super().GET(request, context)
    
    
    def GET_BISTREAM(self, request_iterator, context):
        return super().GET_BISTREAM(request_iterator, context)
    
    
    def GET_RESSTREAM(self, request, context):
        return super().GET_RESSTREAM(request, context)
    #should use generator to make a data stream
    
    
    def LOGIN(self, request, context):
        return super().LOGIN(request, context)
    
    
    def SEND_CODE(self, request, context):
        return super().SEND_CODE(request, context)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    API_pb2_grpc.add_EOGServicer_to_server(EOGServicer(), server)
    server.add_insecure_port('localhost:3129')
    server.start()
    server.wait_for_termination()
    
def get_info_from_handler():
    pass

def start_handler():
    bot_handler.main()
    
if __name__ == "__main__":
    serve();