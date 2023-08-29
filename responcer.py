import grpc
import API_pb2
import API_pb2_grpc
import bot_handler
import time



class EOGServicer(API_pb2_grpc.EOGServicer):
    def GET_BY_NAME(self, request, context):
        responce = API_pb2.RESPONCE()
        bot_handler.start('by_name', request.input_info, request.choice)
        bot_handler.run()
        responce.text_info = bot_handler.get_responce()
        bot_handler.stop()
        return responce
    
    
    def GET_BY_NUM(self, request, context):
        responce = API_pb2.RESPONCE()
        bot_handler.start('by_num', request.input_info)
        bot_handler.run()
        responce.text_info = bot_handler.get_responce()
        bot_handler.stop()
        return responce
    
    
    def GET_BY_CAR(self, request, context):
        responce = API_pb2.RESPONCE()
        bot_handler.start('by_car', request.input_info)
        bot_handler.run()
        responce.text_info = bot_handler.get_responce()
        bot_handler.stop()
        return responce
    
    
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
    
if __name__ == "__main__":
    serve()