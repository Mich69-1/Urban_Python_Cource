# Пользовательский класс для интроспекции

class OhmLow:
    '''Объект иллюстрирует закон Ома'''

    def __init__(self, u, r):
        '''Напряжение цепи и сопротивление нагрузки'''
        self.u = u
        self.r = r

    def get_current(self):
        '''Возвращает ток'''
        return self.u / self.r

    def power(self):
        '''Возвращает рассеиваемую мощность'''
        return self.u * self.get_current()
