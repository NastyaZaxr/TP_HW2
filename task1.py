class INGR:

    def __init__(self, name, qu, un):
        self.name = name
        self.qu = qu
        self.un = un

    @property
    def qu(self):
        return self.__qu

    @qu.setter
    def qu(self, ans):
        ans = float(ans)
        if ans <= 0:
            raise ValueError('Количество должно быть положительным')
        self.__qu = ans

    def __str__(self):
        return f'{self.name}: {self.qu} {self.un}'
    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.qu}', '{self.un}')"
    def __eq__(self, other):
        return self.name == other.name and self.un == other.un




