try:
    qtd_alunos = int(input("Quantos alunos há na turma? "))

    if qtd_alunos <= 0:
        print("O número de alunos deve ser maior que zero.")
    else:
        soma_notas = 0.0

        for i in range(1, qtd_alunos + 1):
            while True:
                try:
                    nota = float(input(f"Digite a nota do aluno {i} (0 a 10): "))
                    if 0 <= nota <= 10:
                        soma_notas += nota
                        break  # Sai do while e passa para o próximo aluno
                    else:
                        print("Nota inválida. Digite um valor entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")

        media = soma_notas / qtd_alunos
        print(f"\nMédia da turma: {media:.2f}")
except ValueError:
    print("Entrada inválida. Digite um número inteiro para a quantidade de alunos.")
