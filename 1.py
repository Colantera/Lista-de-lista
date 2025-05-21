import random

lista = []

qunati = int(input("Digite a quantidade de numeros que você deseja: "))

for _ in range(qunati):
    numero = random.randint(0,100)
    lista.append(numero)

print(f"Sua lista é: {lista}")