from task1 import INGR
class R:
    def __init__(self, tit, ing):
        self.tit = tit
        self.ing = ing
    def add(self, prod):
        for i in self.ing:
            if i.name == prod.name and i.un == prod.un:
                i.qu = i.qu + prod.qu
                return
        self.ing.append(prod)
    @staticmethod
    def valid(r):
        if r>0:
            return True
        else:
            return False
    def scale(self, r):
        res = []
        for j in self.ing:
            nqu = j.qu * r
            ningr = INGR(j.name,nqu, j.un)
            res.append(ningr)
        return R(self.tit, res)
    def __len__(self):
        return len(self.ing)
    def __str__(self):
        anss = ', '.join([str(i) for i in self.ing])
        return f'{self.tit}: {anss}'