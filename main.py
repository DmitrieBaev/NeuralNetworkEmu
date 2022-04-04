from neural import handler


def main():
    try:
        # a = int(input('Введите начало операционного отрезка: '))
        # b = int(input('Введите конец операционного отрезка: '))
        # N = int(input('Введите количество нейронов: '))
        # pointX = float(input('Введите координату X искомой точки: '))
        # pointY = float(input('Введите координату Y искомой точки: '))

        handler.configure(a=0, b=10, N=10)
        handler.calculate(point=8.0)
    except ValueError:
        print('[X] Некорректные данные!')
        main()


if __name__ == '__main__':
    main()
