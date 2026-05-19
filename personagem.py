class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defesa = defesa
        self.defesa_base = defesa

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        if dano < 0:
            dano = 0
        alvo.vida -= dano
        return dano
    
    def resetar_defesa(self):
        self.defesa = self.defesa_base