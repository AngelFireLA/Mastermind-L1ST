from ..utils import récupérer_combinaison_aléatoire

class Partie:
    def __init__(self):
        self.combinaison = récupérer_combinaison_aléatoire()
        self.progrès = [-1, -1, -1, -1]

    def tester_combinaison(self, combinaison):
        if combinaison == self.combinaison:
            return True
        else:
            self.progrès = [-1, -1, -1, -1]
            for i in range(4):
                if combinaison[i] == self.combinaison[i]:
                    self.progrès[i] = 2
                elif combinaison[i] not in self.combinaison:
                    self.progrès[i] = 0
            for i in range(4):
                if self.progrès[i] == -1:
                    for j in range(4):
                        if i != j and combinaison[i] == self.combinaison[j] and self.progrès[j] != 2:
                            self.progrès[j] = 1
                            break
            return False
