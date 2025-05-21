user = input("Digite várias palavras colocando espaço entre elas: ")

palavras = user.split()

if palavras:
    palavra_mais_curta = palavras[0]
    palavra_mais_longa = palavras[0]

    for palavra in palavras:
        if len(palavra) < len(palavra_mais_curta):
            palavra_mais_curta = palavra
        if len(palavra) > len(palavra_mais_longa):
            palavra_mais_longa = palavra

    print("Palavra mais curta:", palavra_mais_curta)
    print("Palavra mais longa:", palavra_mais_longa)
else:
    print("Nenhuma palavra foi digitada.")