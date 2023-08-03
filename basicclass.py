class Bassic_word():
    """ здесь функции которые принимают ввод,считывают количесвто subwords
    """
    def __init__(self, value, subwords):
        self.value = value
        self.subwords = subwords

    def check_input(self, user_answer):
        n = False
        for name in self.subwords:
            if name == user_answer:
                n = True
        return n

    def count_subwords(self):
        return len(self.subwords)

    def __repr__(self):
        return f'{self.value} содержит {len(self.subwords)}'


class Player():
    """
    здесь список used содержит угаданные слова .класс проверяет вход, проверяет и добавляет элементы списка
    """
    def __init__(self, user_name):
        self.user_name = user_name
        self.used = []

    def count_of_used(self):
        return len(self.used)

    def add_to_used(self, word):
        self.used.append(word)

    def check_used(self, word):
        return word in self.used

    def __repr__(self):
        return f"{self.user_name} , угадал слова {', '.join(self.used)}"
