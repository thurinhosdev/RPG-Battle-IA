def turno(jogador, inimigo):
    jogador.resetar_defesa()
    inimigo.resetar_defesa()

    print("\nSeu turno:")
    acao = input("Escolha (atacar/defender): ").lower()

    if acao == "atacar":
        dano = jogador.atacar(inimigo)
        print(f"Você causou {dano} de dano!")
    elif acao == "defender":
        jogador.defesa += 5
        print("Você aumentou sua defesa!")
    else:
        print("Ação inválida! Você perdeu o turno.")

    print("\nTurno do inimigo:")
    acao_inimigo = inimigo.decidir_acao(jogador)

    if acao_inimigo == "atacar":
        dano = inimigo.atacar(jogador)
        print(f"Inimigo causou {dano} de dano!")
    else:
        inimigo.defesa += 5
        print("Inimigo aumentou a defesa!")