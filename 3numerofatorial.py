def calcular_fatorial(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

while True:
    try:
        n = int(input("Digite um número inteiro não negativo: "))
        if n < 0:
            print("Número inválido. Digite um número inteiro não negativo.")
        else:
            resultado = calcular_fatorial(n)
            print(f"{n}! = {resultado}")
            break
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
