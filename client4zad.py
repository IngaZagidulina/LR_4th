import socket
import threading

# Функция для приема сообщений от сервера
def receive_messages(client_socket):
    while True:
        try:
            # Получаем сообщение от сервера
            message = client_socket.recv(1024).decode()
            if message:
                # Выводим сообщение на экран
                print(message)
        except Exception as e:
            # В случае ошибки при получении сообщения, выводим сообщение об ошибке и выходим из цикла
            print(f"Ошибка при получении сообщения: {e}")
            break

# Функция для отправки сообщений на сервер
def send_messages(client_socket):
    while True:
        try:
            # Получаем сообщение от пользователя
            message = input()
            # Отправляем сообщение на сервер
            client_socket.send(message.encode())
        except Exception as e:
            # В случае ошибки при отправке сообщения, выводим сообщение об ошибке и выходим из цикла
            print(f"Ошибка при отправке сообщения: {e}")
            break

if __name__ == "__main__":
    # Устанавливаем значения по умолчанию для IP-адреса и порта сервера
    host = "127.0.0.1"
    port = 8083
    # Получаем имя пользователя от пользователя
    username = input("Введите ваше имя: ")
    
    try:
        # Создаем сокет для подключения к серверу
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Подключаемся к серверу
        client_socket.connect((host, port))
        
        # Отправляем имя пользователя на сервер
        client_socket.send(username.encode())
        
        # Создаем отдельные потоки для приема и отправки сообщений
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
        
        send_thread = threading.Thread(target=send_messages, args=(client_socket,))
        send_thread.start()
        
        # Ждем завершения потоков
        receive_thread.join()
        send_thread.join()
    except Exception as e:
        # В случае ошибки при подключении или выполнении действий, выводим сообщение об ошибке
        print(f"Ошибка при подключении к серверу: {e}")
    finally:
        # Закрываем сокет при любом исходе
        client_socket.close()
