def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas"""
    return sum(notas) / len(notas)


def situacao(media):
    """Retorna a situação do aluno baseado na média"""
    if media >= 7:
        return "✅ Aprovado"
    elif media >= 5:
        return "⚠️ Recuperação"
    else:
        return "❌ Reprovado"


def menu():
    notas = []

    while True:
        print("\n=== CALCULADORA DE MÉDIA ===")
        print("1. Adicionar nota")
        print("2. Calcular média")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                nota = float(input("Digite a nota (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    print("Nota adicionada com sucesso!")
                else:
                    print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Digite um número válido.")
        
        elif opcao == "2":
            if notas:
                media = calcular_media(notas)
                print(f"\nMédia: {media:.2f}")
                print("Situação:", situacao(media))
            else:
                print("Nenhuma nota cadastrada ainda.")

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
