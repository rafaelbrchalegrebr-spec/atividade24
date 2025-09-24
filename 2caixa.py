total = 0.0  # Total da compra

while True:
    try:
        preco = float(input("Digite o preço do produto (ou 0 para finalizar): "))

        if preco == 0:
            break  # Finaliza a entrada de produtos
        elif preco < 0:
            print("Preço inválido. Não é permitido valor negativo.")
        else:
            total += preco
    except ValueError:
        print("Entrada inválida. Digite um número válido.")

print(f"Total da compra: R$ {total:.2f}")
