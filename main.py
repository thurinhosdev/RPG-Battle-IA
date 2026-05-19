from personagem import Personagem
from inimigo import Inimigo
from combate import turno

jogador = Personagem("Herói", 100, 15, 5)
inimigo = Inimigo("Goblin", 80, 12, 4)

while jogador.vida > 0 and inimigo.vida > 0:
    print("\n" + "="*30)
    print(f"{jogador.nome}: {jogador.vida}/{jogador.vida_max} HP")
    print(f"{inimigo.nome}: {inimigo.vida}/{inimigo.vida_max} HP")
    print("="*30)

    turno(jogador, inimigo)

if jogador.vida > 0:
    print("\n🏆 Você venceu!")
else:
    print("\n💀 Você perdeu!")