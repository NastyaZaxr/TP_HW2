from task2 import R
from task1 import INGR
class Dieta(R):
    def __init__(self, t, diet, ingred=None):
        if ingred is None:
            ingred = []
        super().__init__(t, ingred)
        self.diet = diet
    def scale(self, r):
        b = super().scale(r)
        return Dieta(b.tit, self.diet, b.ing)
    def __str__(self):
        return '[' + self.diet + '] ' + super().__str__()

