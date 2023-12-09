import logging
import os
import argparse


class NegativeValueError(ValueError):
    pass


class Rectangle:
    logging.basicConfig(
        filename='logs/class.log',
        format='{levelname} - {asctime} - {msg}',
        style='{',
        encoding='utf-8',
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    def __init__(self, width, height=None):
        if width <= 0:
            self.logger.error(f'Ширина должна быть положительной, а не {width}')
            raise NegativeValueError(f'Ошибка, посмотрите лог в текущей директории {os.getcwd()}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                self.logger.error(f'Высота должна быть положительной, а не {height}')
                raise NegativeValueError(f'Ошибка, посмотрите лог в текущей директории {os.getcwd()}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            self.logger.error(f'Ширина должна быть положительной, а не {value}')
            raise NegativeValueError(f'Ошибка, посмотрите лог в текущей директории {os.getcwd()}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            self.logger.error(f'Высота должна быть положительной, а не {value}')
            raise NegativeValueError(f'Ошибка, посмотрите лог в текущей директории {os.getcwd()}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __str__(self):
        information = f'Ширина и высота прямоугольника "шир: {self.width}, выс: {self.height}"'
        self.logger.info(information)
        return information


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Принимаем число c шириной и высотой прямоугольника')
    parser.add_argument('-wid', metavar='W', type=int, help='Ширина прямоугольника', default=1)
    parser.add_argument('-hei', metavar='H', type=int, help='Высота прямоугольника', default=1)

    args = parser.parse_args()

    wid, hei = args.wid, args.hei

    print(Rectangle(wid, hei))
