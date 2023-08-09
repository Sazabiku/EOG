import grpc
import API_pb2
import API_pb2_grpc
import time

#Позже попробовать подкрутить streamlit


def get_client_stream():
    while True:
        key_search = input('Введите данные для поиска')
        
        if key_search == '':
            break
        
        client_request = API_pb2.SearchSlice(input_info = key_search)
        yield client_request
        time.sleep(0.1)
        
        
def run():
    with grpc.insecure_channel('localhost:3129') as channel:
        stub = API_pb2_grpc.EOGStub(channel)
        print('1. Uni message')
        print('2. Stream')
        rpc_call = input ('Your choice: ')
        
        if rpc_call == 1:
            key_search = input('Введите данные для поиска')
            client_request = API_pb2.SearchSlice(input_info = key_search)
            server_responce = stub.GET(client_request)
            
        if rpc_call == 2:
            server_responces = stub.GET_BISTREAM(get_client_stream())
            
            for responce in server_responces:
                print(responce)
                
if __name__ == "__main__":
    run()