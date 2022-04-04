import sys

X = []  # Точки по оси 0X
A = []  # -----------------------
B = []  # Необходимые данные для
C = []  # работы нейронной сети
D = []  # -----------------------
N = 0   # Количество нейронов


def configure(a: float, b: float):
    """
    Инициализация значений, необходимых для нейронной сети

    :param a: Начало обрабатываемого отрезка
    :param b: Конец обрабатываемого отрезка
    :param N: Количество нейронов
    """

    # Инициализация точек по оси 0X
    i = 0
    step = b / N
    while i < N + 1:
        X.append(a + i * step)
        i += 1

    # Подготовка значений для вычисления нейронной сети
    for i in range(N):
        A.append((X[i] ** 2 - X[i + 1] ** 2) / (X[i] - X[i + 1]))
        B.append(-X[i]*X[i + 1])
        C.append(1 / (X[i + 1] - X[i]))
        D.append(-(X[i] / (X[i + 1] - X[i])))


def calculate(point: float):
    """
    Запуск нейронной сети для обработки функции

    :param point: 0X координата точки, которую нужно найти
    :return: Список отрезков, в котором ненулевое значение - подходящая точка на оси 0Y
    """
    def layer_1_solution():
        """ Обработка 1-го слоя нейронной сети """
        y = []
        for i in range(N):
            y.append(point * A[i] + B[i])
        return y

    def layer_2_solution():
        """ Обработка 2-го слоя нейронной сети """
        y = []
        for i in range(N):
            y.append(1 if 0.0 <= (point * C[i] + D[i]) < 1.0 else 0)
        return y

    def layer_3_solution(l1: list, l2: list):
        """ Обработка 3-го слоя нейронной сети """
        y = []
        for i in range(N):
            y.append(l1[i] * l2[i])
        return y

    layer1 = layer_1_solution()
    layer2 = layer_2_solution()

    return layer_3_solution(layer1, layer2)


if __name__ == "__main__":
    N = sys.argv[1]
    configure(float(sys.argv[2]), float(sys.argv[3]))
    calculate(float(sys.argv[4]))
