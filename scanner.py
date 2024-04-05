<<<<<<< HEAD
import socket
from threading import Thread

N = 2**16 - 1

for port in range(1,100):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", i, "открыт")
    except:
        continue
    finally:
        sock.close()
=======
<<<<<<< HEAD
import socket
from threading import Thread

N = 2**16 - 1

for port in range(1,100):
    sock = socket.socket()
    try:
        print(port)
        sock.connect(('127.0.0.1', port))
        print("Порт", i, "открыт")
    except:
        continue
    finally:
        sock.close()
=======
import socket
from threading import Thread
from time import sleep

# Класс для создания потоков
class Thr(Thread):
    # Статическое поле для хранения состояний портов
    output = []

    # Конструктор класса
    def __init__(self, n, start_port, end_port, step, address):
        Thread.__init__(self, name="t" + str(n))
        self.start_port = start_port
        self.end_port = end_port
        self.step = step
        self.address = address
        self.start()

    # Метод, который выполняется при запуске потока
    def run(self):
        for port in range(self.start_port, self.end_port + 1, self.step):
            sock = socket.socket()
            try:
                # Пытаемся подключиться к порту
                sock.connect((self.address, port))
                # Если удалось подключиться, добавляем True в список состояний
                Thr.output.append(True)
            except:
                # Если не удалось подключиться, добавляем False в список состояний
                Thr.output.append(False)
            finally:
                # Закрываем сокет
                sock.close()

    # Статический метод для вывода результатов сканирования портов
    @staticmethod
    def print_result(output, start_port):
        for port, state in enumerate(output):
            print(f"Порт {port + start_port} {'открыт' if state else 'закрыт'}")

    # Статический метод для вывода прогресса выполнения сканирования
    @staticmethod
    def print_progress_bar(iteration, total, proverka='', zaver='', decimals=1, length=100, fill='█'):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{proverka} |{bar}| {percent}% {zaver}', end="")
        if iteration == total:
            print()

    # Статический метод для отображения прогресса выполнения сканирования
    @classmethod
    def progress_bar(cls, start, end):
        length = end - start + 1
        while True:
            cls.print_progress_bar(len(cls.output), length, proverka="Проверка", zaver="Завершено", length=55)
            if len(cls.output) == length:
                break
            sleep(0.1)
        cls.print_result(Thr.output, start)


# Функция для получения входных данных от пользователя
def get_input():
    start_port = input("Введите начальный порт: ") 
    if start_port == "":
        start_port=2000
    else:
        start_port=int(start_port)
    end_port = input("Введите конечный порт: ")
    if end_port == "":
        end_port = 2098
    else:
        end_port=int(end_port)
    end_port = 2098 if end_port == "" else int(end_port)
    step = input("Введите число потоков: ")
    step = 3 if step == "" else int(step)
    address = input("Введите адрес: ")
    address = "127.0.0.1" if address == "" else address
    return start_port, end_port, step, address

# Получаем входные данные от пользователя
start_port, end_port, step, address = get_input()
list_of_threads = []

# Создаем и запускаем потоки
Thr.port = start_port - 1
for i in range(step):
    list_of_threads.append(Thr(i, start_port + i, end_port, step, address))

# Создаем поток для отображения прогресса выполнения
thread = Thread(target=Thr.progress_bar(start_port, end_port), name="result")
thread.start()
>>>>>>> f3fd106 (HW)
>>>>>>> fa0ac8d (HW)
