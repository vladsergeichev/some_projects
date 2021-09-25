class Soda:
    """
        Задача с сайта - https://smartiqa.ru/python-workbook/class#1
    """

    def __init__(self, ingredient):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            print(f'Газировка и {self.ingredient}')
        else:
            print('Обычная газировка')


d1 = Soda('')
d2 = Soda('арбуз')
d3 = Soda(4)
d1.show_my_drink()
d2.show_my_drink()
d3.show_my_drink()
