import grpc
import API_pb2
import API_pb2_grpc
import time
        
        

def run():
    with grpc.insecure_channel('localhost:3129') as channel:
        stub = API_pb2_grpc.EOGStub(channel)
        print('1. Поиск по ФИО')
        print('2. Поиск по номеру телефона')
        print('3. Поиск по социальным сетям')
        print('4. Поиск по E-mail')
        print('5. Поиск по VIN/рег. номеру автомобиля')
        print('6. Поиск по кадастровому номеру')
        print('7. Поиск по ИНН')
        print('8. Поиск по СНИЛС')
        print('9. Поиск по юр. лицу')
        print('10. Поиск по адресу')
        rpc_call = input ('Your choice: ')
        
        if rpc_call == 1:
            key_search = input('Введите ФИО:')
            country_flag = input('Производить поиск по России? Y/N: ')
            if country_flag == 'N' or country_flag == 'n':
                choice = input('Введите название страны по которой требуется провести поиск: ')
            client_request = API_pb2.SearchInput(input_info = key_search, choice = choice)
            server_responce = stub.GET_BY_NAME(client_request)
            print(server_responce)
        elif rpc_call == 2:
            key_search = input('Введите номер телефона: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_NUM(client_request)
            print(server_responce)
        elif rpc_call == 3:
            key_search = input('Введите тэг в социальной сети или ссылку на аккаунт: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_SM(client_request)
            print(server_responce)
        elif rpc_call == 4:
            key_search = input('Введите E-mail: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_EMAIL(client_request)
            print(server_responce)
        elif rpc_call == 5:
            key_search = input('Введите VIN/регистрационный номер авто: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_CAR(client_request)
            print(server_responce)
        elif rpc_call == 6:
            key_search = input('Введите кадастровый номер: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_CAD(client_request)
            print(server_responce)
        elif rpc_call == 7:
            key_search = input('Введите ИНН: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_INN(client_request)
            print(server_responce)
        elif rpc_call == 8:
            key_search = input('Введите СНИЛС: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_SNILS(client_request)
            print(server_responce)
        elif rpc_call == 9:
            key_search = input('Введите наименование юридического лица: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_CPNY(client_request)
            print(server_responce)
        elif rpc_call == 10:
            key_search = input('Введите адрес: ')
            client_request = API_pb2.SearchInput(input_info = key_search)
            server_responce = stub.GET_BY_ADR(client_request)
            print(server_responce)
                
if __name__ == "__main__":
    run()