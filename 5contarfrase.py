frase = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

conta_vogais = 0
conta_consoantes = 0

for caractere in frase:
    if caractere in letras:
        if caractere in vogais:
            conta_vogais += 1
        else:
            conta_consoantes += 1

print(f"\nNúmero de vogais: {conta_vogais}")
print(f"Número de consoantes: {conta_consoantes}")
