def mostrar_menu():
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Ver saldo")
    print("2 - Fazer depósito")
    print("3 - Fazer saque")
    print("4 - Sair")
    print("0 - Encerrar programa")

# Loop principal
while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("Você escolheu 'Ver saldo'.")
    elif opcao == '2':
        print("Você escolheu 'Fazer depósito'.")
    elif opcao == '3':
        print("Você escolheu 'Fazer saque'.")
    elif opcao == '4':
        print("Você escolheu 'Sair'.")
    elif opcao == '0':
        print("\n✅ Programa encerrado. Até a próxima!")
        break
    else:
        print("❌ Opção inválida. Por favor, tente novamente.")
