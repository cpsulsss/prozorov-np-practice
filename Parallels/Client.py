import numpy as np
import time
from multiprocessing.managers import BaseManager, RemoteError

# Определяем класс для клиента
class MatrixClient(BaseManager):
    pass

if name == 'main':
    # Подключаемся к серверу
    MatrixClient.register('multiply_matrices')
    MatrixClient.register('stop_process')
    manager = MatrixClient(address=('localhost', 5000), authkey=b'secret')
    manager.connect()

    try:
        while True:
            # Генерируем случайные квадратные матрицы
            matrix_size = np.random.randint(2, 6)
            matrix1 = np.random.randint(0, 10, size=(matrix_size, matrix_size))
            matrix2 = np.random.randint(0, 10, size=(matrix_size, matrix_size))

            # Умножаем матрицы на сервере и получаем результат
            result_matrix = manager.multiply_matrices(matrix1, matrix2, 'result.txt')
            print("Result matrix:")
            print(result_matrix)

            # Даем время для остановки процесса
            time.sleep(1)

    except RemoteError as e:
        print("Server stopped:", e)