tabuleiro = [" " for _ in range(9)]

def mostrar():
    print(tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("--+---+--")
    print(tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("--+---+--")
    print(tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])

def venceu(jogador):
    vitorias = [
        [0,1,2], [3,4,5], [6,7,8],  # linhas
        [0,3,6], [1,4,7], [2,5,8],  # colunas
        [0,4,8], [2,4,6]            # diagonais
    ]
    for pos in vitorias:
        if tabuleiro[pos[0]] == tabuleiro[pos[1]] == tabuleiro[pos[2]] == jogador:
            return True
    return False

jogador = "X"
for turno in range(9):
    mostrar()
    escolha = int(input(f"Jogador {jogador}, escolha uma posição (0 a 8): "))
    
    if tabuleiro[escolha] != " ":
        print("Posição ocupada. Tente outra.")
        continue

    tabuleiro[escolha] = jogador

    if venceu(jogador):
        mostrar()
        print(f"Jogador {jogador} venceu!")
        break

    jogador = "O" if jogador == "X" else "X"
else:
    mostrar()
    print("Empate!")

#Prof não sabia muito oq fazer aqui kkkk a maior parte o chat me ajudou :)