import socket
import threading

# Функция для обработки клиентских запросов
def handle_client(client_socket):
    while True:
        try:
            # Принимаем данные от клиента
            request = client_socket.recv(1024)
            if not request:
                # Если данные не получены, выходим из цикла
                break
            # Отправляем обратно клиенту те же данные
            client_socket.send(request)
        except Exception as e:
            # В случае ошибки при обработке клиента, выводим сообщение об ошибке и выходим из цикла
            print(f"Ошибка при обработке клиента: {e}")
            break
    # Закрываем соединение с клиентом
    client_socket.close()

# Функция для запуска эхо-сервера
def echo_server(host, port):
    # Создаем сокет
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Привязываем сокет к указанному хосту и порту
    server.bind((host, port))
    # Начинаем прослушивать подключения, очередь - 5
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")
    
    while True:
        # Принимаем входящее соединение
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        # Создаем новый поток для обработки клиента
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    # Задаем адрес и порт сервера
    HOST = "127.0.0.1"
    PORT = 12345
    # Запускаем сервер
    echo_server(HOST, PORT)
