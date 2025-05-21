numeros = list(range(1, 101))

pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Números pares de 1 a 100:")
print(pares)