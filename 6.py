pares = []
impares = []

for i in range(1, 11):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)

todos = pares + impares

print("Números pares:", pares)
print("Números ímpares:", impares)
print("Lista combinada:", todos)