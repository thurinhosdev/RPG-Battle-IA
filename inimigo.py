import random
from personagem import Personagem

class Inimigo(Personagem):
    def decidir_acao(self, jogador):
        if self.vida < 20:
            return "defender"
        elif jogador.vida < 30:
            return "atacar"
        else:
            return random.choice(["atacar", "defender"])
        