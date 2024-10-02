'''
Задача "История строительства":
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".

В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.

Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса
используя ссылку на сам класс - cls.
Дополните метод __new__ так, чтобы:
Название объекта добавлялось в список cls.houses_history.
Название строения можно взять из args по индексу.

Также переопределите метод __del__(self) в котором будет выводиться строка:
"<название> снесён, но он останется в истории"

Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
а также значение атрибута houses_history.
'''

############   Код предыдущего урока
'''
Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов":

class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Метод сравнения на равенство
    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    # Метод сравнения <
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    # Метод сравнения <=
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    # Метод сравнения >
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    # Метод сравнения >=
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    # Метод сравнения !=
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    # Метод для сложения (увеличения этажей)
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    # Метод для правостороннего сложения
    def __radd__(self, value):
        return self.__add__(value)

    # Метод для +=
    def __iadd__(self, value):
        return self.__add__(value)
'''

# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
class House:
    houses_history = []  # История всех зданий

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        if len(args) > 0:
            # Дополните метод __new__ так, чтобы:
            # Название объекта добавлялось в список cls.houses_history.
            # Название строения можно взять из args по индексу.
            cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли такой этаж
        if 1 <= new_floor <= self.number_of_floors:
            # Вывод всех этажей от 1 до нового этажа
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        # Сообщение при удалении объекта
        # Также переопределите метод __del__(self) в котором будет выводиться строка:
        # "<название> снесён, но он останется в истории"
        print(f"{self.name} снесён, но он останется в истории")

# Тестирование
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2  # ЖК Акация снесён, но он останется в истории
del h3  # ЖК Матрёшки снесён, но он останется в истории

print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']