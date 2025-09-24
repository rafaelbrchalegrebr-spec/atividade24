# Dicionário com os votos válidos
votos_validos = {
    10: "Candidato A",
    20: "Candidato B",
    30: "Candidato C",
    98: "Voto Nulo",
    99: "Voto em Branco"
}

while True:
    try:
        voto = int(input("Digite o código do seu voto (10, 20, 30, 98, 99): "))
        if voto in votos_validos:
            print(f"Voto registrado: {votos_validos[voto]}")
            break
        else:
            print("Código inválido. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
