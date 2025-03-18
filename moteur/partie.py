from ..utils import récupérer_combinaison_aléatoire

class Partie:
    def __init__(self):
        self.combinaison = récupérer_combinaison_aléatoire()
        self.progrès = [0, 0, 0, 0]

    def tester_combinaison(self, combinaison):
        if combinaison == self.combinaison:
            return True
        else:
            for i in range(4):
                if combinaison[i] == self.combinaison[i]:
                    self.progrès[i] = 2
                elif combinaison[i] in self.combinaison:
                    self.progrès[i] = 1
                else:
                    self.progrès[i] = 0
            return False
