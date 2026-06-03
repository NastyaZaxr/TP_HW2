from task1 import INGR
from task2 import R
class ShopL:
    def __init__(self):
        self._items = []

    def addr(self, rec, porz):
        if porz <= 0:
            raise ValueError('Количество порций должно быть положительным')

        nporz = rec.scale(porz)
        for ing in nporz.ing:
            self._items.append((ing, rec.tit))

    def remr(self, title):
        nitem = []
        for k in self._items:
            if k[1] != title:
                nitem.append(k)
        self._items = nitem

    def f(self, otw, pr):
        for p in range(len(otw)):
            if otw[p].name == pr.name and otw[p].un == pr.un:
                return p
        return None
    def get(self):
        otw = []
        for pr, naz in self._items:
            a = self.f(otw, pr)
            if a is None:
                otw.append(INGR(pr.name, pr.qu, pr.un))
            else:
                otw[a].qu = otw[a].qu + pr.qu
        for i in range(len(otw)):
            for j in range(i+1, len(otw)):
                if otw[i].name > otw[j].name:
                    otw[i], otw[j] = otw[j], otw[i]
        return otw
    def __add__(self, other):
        nl = ShopL()
        nl._items = self._items + other._items
        return nl
