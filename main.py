import random

class Case:
    _valeur: int = 0
    _cache: bool = False
    _bombe: bool = False

    def __init__(self, bombe = False):
        self._bombe = bombe

    def est_bombe(self):
        return self._bombe

    

    def __str__(self):
        return "X" if self._cache else ("O" if self._bombe else " ")


class Plateau:
    grille: list[list[Case]] = []
    width: int = 20
    height: int = 15
    inital_bombes: int = 25

    def __init__(self):
        self.generate()
        self.pose_bombes(self.inital_bombes)

    def generate(self):
        grille = []
        for y in range(self.height):
            v = []
            for x in range(self.width):
                v.append(Case())
            grille.append(v)
        self.grille = grille

    def pose_bombes(self, nombre):
        print(self.grille)

        for i in range(nombre):
            cv = self.cases_vides()
            if len(cv) == 0:
                break
            x,y = cv[random.randint(0, len(cv))]
            self.grille[y][x] = Case(True)
            

    def cases_vides(self):
        li: list[list[int, int]]  = []
        for y in range(self.height):
            for x in range(self.width):
                if not self.grille[y][x].est_bombe():
                    li.append((x, y))
        return li

    
    def affiche(self):
        for i in self.grille:
            print(" ".join(map(str, i)))



p = Plateau()
p.affiche()




