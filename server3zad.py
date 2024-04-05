import socket
import threading

# Словарь для хранения пользователей и их соответствующих сокетов
users = {}

# Список для хранения истории сообщений
messages = []

# Функция для обработки сообщений от пользователя
def handle_client(client_socket, username):
    while True:
        try:
            # Получаем сообщение от пользователя
            message = client_socket.recv(1024).decode()
            if message:
                # Добавляем сообщение в историю
                messages.append(f"{username}: {message}")
                # Пересылаем сообщение всем остальным пользователям
                for user, user_socket in users.items():
                    if user != username:
                        user_socket.send(f"{username}: {message}".encode())
            else:
                # Если сообщение пустое, закрываем соединение
                client_socket.close()
                del users[username]
                break
        except Exception as e:
            # В случае ошибки при обработке сообщения, закрываем соединение и удаляем пользователя из словаря
            print(f"Ошибка: {e}")
            client_socket.close()
            del users[username]
            break

# Функция для обработки подключения новых пользователей
def accept_connections(server_socket):
    while True:
        client_socket, client_address = server_socket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
        # Получаем имя пользователя
        username = client_socket.recv(1024).decode()
        # Добавляем пользователя в словарь пользователей
        users[username] = client_socket
        # Создаем новый поток для обработки клиента
        client_handler = threading.Thread(target=handle_client, args=(client_socket, username))
        client_handler.start()

# Функция для вывода истории сообщений
def show_messages():
    while True:
        if messages:
            print(messages.pop(0))

if __name__ == "__main__":
    # Создаем серверный сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8083))
    server_socket.listen(5)
    print("[*] Server started")
    
    # Создаем поток для обработки подключений
    accept_thread = threading.Thread(target=accept_connections, args=(server_socket,))
    accept_thread.start()
    
    # Создаем поток для вывода истории сообщений
    show_messages_thread = threading.Thread(target=show_messages)
    show_messages_thread.start()
