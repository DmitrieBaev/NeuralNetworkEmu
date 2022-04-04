import sys

X = []  # Точки по оси 0X
A = []  # -----------------------
B = []  # Необходимые данные для
C = []  # работы нейронной сети
D = []  # -----------------------


def configure(a: float, b: float, N: int):
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
        B.append(X[i] ** 2 + X[i + 1] ** 2)
        C.append(1 / (X[i + 1] - X[i]))
        D.append(-(X[i] / (X[i + 1] - X[i])))


def calculate(point: float):
    """
    Запуск нейронной сети для обработки функции

    :param point: 0X координата точки, которую нужно найти

    :return:
    """

    pass


if __name__ == "__main__":
    configure(float(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]))
    calculate(float(sys.argv[4]))
