# Estado inicial da luz
luz_acesa = False

# Loop principal
while True:
    print("\nO que fazer?")
    print("1 - Apertar interruptor")
    print("0 - Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        # Inverte o estado da luz
        luz_acesa = not luz_acesa

        # Mostra o estado atual
        if luz_acesa:
            print("💡 A luz está acesa.")
        else:
            print("💤 A luz está apagada.")
    
    elif escolha == '0':
        print("\n🔚 Programa encerrado.")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
