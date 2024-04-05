import multiprocessing
from multiprocessing.managers import BaseManager
import numpy as np

# Функция для перемножения матриц и записи результатов в файл
def multiply_matrices(matrix1, matrix2, result_filename):
    result_matrix = np.dot(matrix1, matrix2)
    np.savetxt(result_filename, result_matrix, fmt='%d')
    return result_matrix

# Функция для завершения процесса
def stop_process():
    print("Stopping matrix multiplication process...")
    multiprocessing.current_process().terminate()

# Определяем класс для сервера
class MatrixServer(BaseManager):
    pass

# Регистрируем функции в менеджере
MatrixServer.register('multiply_matrices', multiply_matrices)
MatrixServer.register('stop_process', stop_process)

if name == 'main':
    # Создаем объект менеджера
    manager = MatrixServer(address=('localhost', 5000), authkey=b'secret')
    # Запускаем сервер
    server = manager.get_server()
    print("Server started...")
    server.serve_forever()