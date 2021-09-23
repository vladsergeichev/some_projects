class TriangleChecker:
    """
    Задача с сайта - https://smartiqa.ru/python-workbook/class#2
    """
    def __init__(self, digits):
        self.digits = digits

    def is_triangle(self):
        if all(isinstance(digit, (float, int)) for digit in self.digits):
            if all(digit > 0 for digit in self.digits):
                digits_sort = sorted(self.digits)
                if digits_sort[0] + digits_sort[1] > digits_sort[2]:
                    print('Ура, можно построить треугольник!')
                    return
                print('Треугольник не сделать')
                return
            print('Отрицательные числа не подходят')
            return
        print('Введите числа')
        return


TriangleChecker([1, 2, 3]).is_triangle()
TriangleChecker([3, 3, 5]).is_triangle()
TriangleChecker([-3, 3, 5]).is_triangle()
TriangleChecker(['abc', 3, 3]).is_triangle()
