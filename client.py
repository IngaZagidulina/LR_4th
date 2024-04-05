import socket
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> fa0ac8d (HW)
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('10.38.165.12', 9090))

#msg = input()
msg = "Hi!"
sock.send(msg.encode())

data = sock.recv(1024)

sock.close()

print(data.decode())
<<<<<<< HEAD
=======
=======
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
    # Получаем данные от пользователя: IP-адрес и порт сервера, а также его имя
    host = input("Введите IP-адрес сервера: ")
    port = int(input("Введите порт сервера: "))
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
>>>>>>> f3fd106 (HW)
>>>>>>> fa0ac8d (HW)
