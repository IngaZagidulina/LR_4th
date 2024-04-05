import socket
import threading
import time

# Словарь для хранения пользователей и их соответствующих сокетов
users = {}

# Список для хранения истории сообщений
messages = []
logsSpisok = []

# Функция для обработки подключения нового пользователя
def handle_client(client_socket, username):
    while True:
        try:
            # Получаем сообщение от пользователя
            message = client_socket.recv(1024).decode()
            if message:       
                 # Добавляем сообщение в историю
                messages.append(f"{username}: {message}")
                logsSpisok.append(f"{username}: {message}")
                # Проверяем специальные команды
                if message == "stop":
                    stop_server()
                elif message == "pause":
                    pause_server(server_socket)
                elif message == "logs":
                    show_logs(username)
                elif message == "clear_logs":
                    clear_logs()
                elif message == "clear_identification_file":
                    clear_identification_file()
            else:
                # Если сообщение пустое, закрываем соединение
                client_socket.close()
                del users[username]
                break
        except Exception as e:
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

# Функция для остановки сервера
def stop_server():
    print("Server stopped")
    time.sleep(1)
    exit()

# Функция для остановки прослушивания портов
def pause_server(server_socket):
    print("Server paused")
    server_socket.close()

# Функция для вывода логов
def show_logs(username):
    for message in logsSpisok:
        for user, user_socket in users.items():
             if user == username:
                 user_socket.send(f"{message}".encode())
        print(message)

# Функция для очистки логов
def clear_logs():
    logsSpisok.clear()

# Функция для очистки файла идентификации
def clear_identification_file():
    try:
        # Открываем файл идентификации пользователей в режиме записи
        with open("users.txt", "w") as file:
            # Очищаем содержимое файла
            file.truncate(0)
        print("Identification file cleared successfully.")
    except Exception as e:
        print(f"Error while clearing identification file: {e}")


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

    # Создаем управляющий поток
    while True:
        command = input("Enter command: ")
        if command == "stop":
            stop_server()
        elif command == "pause":
            pause_server(server_socket)
        elif command == "logs":
            show_logs()
        elif command == "clear_logs":
            clear_logs()
        elif command == "clear_identification_file":
            clear_identification_file()
