from neural import handler


def main():
    try:
        N = int(input('Введите количество нейронов: '))
        a = int(input('Введите начало операционного отрезка: '))
        b = int(input('Введите конец операционного отрезка: '))
        point = float(input('Введите координату X искомой точки: '))

        handler.N = N  # Количество нейронов
        handler.configure(a=a, b=b)
        result_parser(handler.calculate(point=point))
    except ValueError:
        print('[X] Некорректные данные!')
        main()


def result_parser(result: list):
    """
    Обрабатывает результат, полученный от нейронной сети и выводит в консоль нужную информацию
    """

    for i in result:
        if i != 0:
            print(f'{i:.2f}')
            break


if __name__ == '__main__':
    main()
