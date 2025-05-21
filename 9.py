import random

letras = list("abcdefghijklmnopqrstuvwxyz")
random.shuffle(letras)

letra = random.choice(letras)

palpite = int(input(f"Qual é a posição (0 a 25) da letra '{letra}' na lista embaralhada? "))

if letras[palpite] == letra:
    print("Acertou!")
else:
    print(f"Errou! A letra está na posição {letras.index(letra)}.")