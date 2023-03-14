""" Садовник и помидоры

Классовая структура
Предлагаем создать следующую классовую структуру:

Есть Помидор со следующими характеристиками:
Индекс Стадия зрелости
(стадии: Отсутствует, Цветение, Зеленый, Красный)
Помидор может:
Расти (переходить на следующую стадию созревания)
Предоставлять информацию о своей зрелости

Есть Куст с помидорами, который:
Содержит список томатов, которые на нем растут
И может:
Расти вместе с томатами
Предоставлять информацию о зрелости всех томатов
Предоставлять урожай

И также есть Садовник, который имеет:
Имя
Растение, за которым он ухаживает
И может:
Ухаживать за растением
Собирать с него урожай


Тесты:
Вызовите справку по садоводству
Создайте объекты классов TomatoBush и Gardener
Используя объект класса Gardener, поухаживайте за кустом с помидорами
Попробуйте собрать урожай
Если томаты еще не дозрели, продолжайте ухаживать за ними
Соберите урожай"""


class Tomato:

    # значения по умолчанию при создании объекта класса Tomato
    default_index = 1
    default_state = 'нет ничего'
    default_n = 1

    def __init__(self, _index=default_index, _state=default_state):
        self._index = _index
        self._state = _state

    # информация о состоянии помидора
    def set_state(self, n=default_n):
        if n == 1:
            self._state = 'нет ничего'
            return self._state
        elif n == 2:
            self._state = 'цветение'
            return self._state
        elif n == 3:
            self._state = 'зеленый'
            return self._state
        elif n == 4:
            self._state = 'красный'
            return self._state

    # проверка помидора на спелость
    def is_red(self, _state):
        if self._state == 'красный':
            print('Проверка на спелость: помидор спелый')
            return True
        else:
            print('Проверка на спелость: помидор еще не созрел')
            return False

    # информация о состоянии помидора в данный момент
    def get_index_state(self):
        print(f'Помидор №{self._index}: {self._state}')


# tom1 = Tomato()
"""tom1_state = tom1.set_state()
tom1.is_red(tom1_state)
tom1.get_index_state()

tom1_state = tom1.set_state(2)
tom1.is_red(tom1_state)
tom1.get_index_state()

tom1_state = tom1.set_state(3)
tom1.is_red(tom1_state)
tom1.get_index_state()

tom1_state = tom1.set_state(4)
tom1.is_red(tom1_state)
tom1.get_index_state()"""


class TomatoBush:

    # значения по умолчанию при создании объекта класса TomatoBush
    default_tomatoes = 2
    default_n = 1

    def __init__(self, tomatoes=default_tomatoes):
        self.tomatoes = tomatoes

        # создание объектов - 2 помидора на кусте
        self.tom1 = Tomato(1)
        self.tom2 = Tomato(2)

    # переводит ВСЕ томаты на следующий этап созревания
    def set_state_all(self, n=default_n):
        if n == 1:
            # функция класса Tomato
            self.tom1.set_state(1)
            self.tom2.set_state(1)
            s = 'нет ничего'
            return s
        elif n == 2:
            self.tom1.set_state(2)
            self.tom2.set_state(2)
            s = 'цветение'
            return s
        elif n == 3:
            self.tom1.set_state(3)
            self.tom2.set_state(3)
            s = 'зеленые'
            return s
        elif n == 4:
            self.tom1.set_state(4)
            self.tom2.set_state(4)
            s = 'красные'
            return s

    # проверяет спелость ВСЕХ томатов
    def is_red_all(self, s):

        if s == 'красные':
            y = 1
            print('Проверка на спелость: помидоры все созрели')
            return y
        else:
            y = 0
            print('Проверка на спелость: помидоры еще не созрели')
            return y

    # меняет состояние томатов на "ничего нет" - после сбора урожая
    def take_away_all(self, y):
        if y == 1:
            # функция класса Tomato
            self.tom1.get_index_state()
            self.tom2.get_index_state()
            self.tom1.set_state(1)
            self.tom2.set_state(1)
            print('Собирать урожай: помидоры собрали')
        else:
            print('Собирать урожай: помидоры еще не собирали')

    # состояние ВСЕХ помидоров в данный момент
    def get_state_all(self):
        # функция класса Tomato
        self.tom1.get_index_state()
        self.tom2.get_index_state()


"""bush = TomatoBush()
print()
st1 = bush.set_state_all(1)
y_t = bush.is_red_all(st1)
bush.take_away_all(y_t)
bush.get_state_all()
print()
st1 = bush.set_state_all(2)
y_t = bush.is_red_all(st1)
bush.take_away_all(y_t)
bush.get_state_all()
print()
st1 = bush.set_state_all(3)
y_t = bush.is_red_all(st1)
bush.take_away_all(y_t)
bush.get_state_all()
print()
st1 = bush.set_state_all(4)
y_t = bush.is_red_all(st1)
bush.take_away_all(y_t)
bush.get_state_all()"""



class Gardener:

    # параметры по умолчанию при создании объекта класса Gardener
    default_name = 'Алекс'
    default_n_bush = 1
    default_n = 1

    def __init__(self, name=default_name, n_bush=default_n_bush):
        self.name = name
        self.bush = n_bush

        # создаются объекты - 1 куст с 2-мя помидорами
        self.bush = TomatoBush
        self.tom1 = Tomato(1)
        self.tom2 = Tomato(2)

    # выводит информацию по садовнику
    def info_about_gardener(self):
        print(f'Имя садовника: {self.name}')

    # садовник делает ВСЕ помидоры более спелыми на кусте
    def set_state_bush(self, n=default_n):
        print('Это садовник делает помидоры более спелыми...')
        # функция из class TomatoBush
        s = self.bush.set_state_all(self, n)
        return s

    # садовник проверяет на спелость ВСЕ помидоры куста
    def is_red_bush(self, s):
        print('Это садовник проверяет на спелость...')
        # функция из class TomatoBush
        y = self.bush.is_red_all(self, s)
        return y

    # садовник собирает урожай, когда все помидоры спелые
    def take_away_bush(self, y):
        print('Это садовник смотрит: можно ли собирать урожай...')
        # функция из class TomatoBush
        self.bush.take_away_all(self, y)

    # садовник информирует о спелости каждого помидора на кусте
    def get_state_bush(self):
        print('Это садовник информирует о текущем состоянии...')
        # функция из class TomatoBush
        self.bush.get_state_all(self)


men = Gardener()
print()
men.info_about_gardener()
s = men.set_state_bush(1)
y = men.is_red_bush(s)
men.take_away_bush(y)
men.get_state_bush()
print()
men.info_about_gardener()
s = men.set_state_bush(2)
y = men.is_red_bush(s)
men.take_away_bush(y)
men.get_state_bush()
print()
men.info_about_gardener()
s = men.set_state_bush(3)
y = men.is_red_bush(s)
men.take_away_bush(y)
men.get_state_bush()
print()
men.info_about_gardener()
s = men.set_state_bush(4)
y = men.is_red_bush(s)
men.take_away_bush(y)
men.get_state_bush()

