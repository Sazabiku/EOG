import grpc
import API_pb2
import API_pb2_grpc
import bot_handler


import time

class EOGServicer(API_pb2_grpc.EOGServicer):
    def GET_BY_NAME(self, request, context):
        return super().GET(request, context)
    
    
    def GET_BY_NUM(self, request, context):
        return super().GET(request, context)
    
    
    def GET_BY_CAR(self, request, context):
        return super().GET(request, context)
    
    
    def GET_BY_SM(self, request, context):
        return super().GET_BY_SM(request, context)
    
    
    def GET_BY_ADR(self, request, context):
        return super().GET_BY_ADR(request, context)
    
    
    def GET_BY_CAD(self, request, context):
        return super().GET_BY_CAD(request, context)
    
    
    def GET_BY_EMAIL(self, request, context):
        return super().GET_BY_EMAIL(request, context)
    
    
    def GET_BY_CPNY(self, request, context):
        return super().GET_BY_CPNY(request, context)
    
    
    def GET_BY_INN(self, request, context):
        return super().GET_BY_INN(request, context)
    
    
    def GET_BY_SNILS(self, request, context):
        return super().GET_BY_SNILS(request, context)
    
    
    def LOGIN(self, request, context):
        return super().LOGIN(request, context)
    
    
    def SEND_CODE(self, request, context):
        return super().SEND_CODE(request, context)
    
def serve():
    server = grpc.server()
    API_pb2_grpc.add_EOGServicer_to_server(EOGServicer(), server)
    server.add_insecure_port('localhost:3130')
    server.start()
    server.wait_for_termination()
    
def get_info_from_handler():
    pass

def start_handler():
    bot_handler.main()
    
if __name__ == "__main__":
    serve();