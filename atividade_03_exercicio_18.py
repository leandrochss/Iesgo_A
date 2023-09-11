# Menu interativo
### Crie um aplicativo que exibe um menu interativo no console do usuário. Nesse menu, o usuário pode escolher entre as seguintes opções:
## 1. Calcular a sua idade em meses
## 2. Calcular a sua idade em dias
## 3. Calcular a sua idade em horas
## 4. Calcular a sua idade em minutos
## 5. Calcular a sua idade em segundos
## 6. Sair do programa
### Bônus: permita que o usuário insira a data atual e a data de seu nascimento.

from datetime import datetime

def calcular_idade():
    print("Menu interativo")
    print("1. Calcular a sua idade em meses")
    print("2. Calcular a sua idade em dias")
    print("3. Calcular a sua idade em horas")
    print("4. Calcular a sua idade em minutos")
    print("5. Calcular a sua idade em segundos")
    print("6. Sair do programa")

    while True:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 6:
            break

        data_nascimento = input("Digite a sua data de nascimento (dd/mm/yyyy): ")
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

        data_atual = input("Digite a data atual (dd/mm/yyyy): ")
        data_atual = datetime.strptime(data_atual, "%d/%m/%Y")

        idade = (data_atual - data_nascimento).days // 365

        if opcao == 1:
            print(f"Sua idade em meses é: {idade * 12}")
        elif opcao == 2:
            print(f"Sua idade em dias é: {idade * 365}")
        elif opcao == 3:
            print(f"Sua idade em horas é: {idade * 365 * 24}")
        elif opcao == 4:
            print(f"Sua idade em minutos é: {idade * 365 * 24 * 60}")
        elif opcao == 5:
            print(f"Sua idade em segundos é: {idade * 365 * 24 * 60 * 60}")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    calcular_idade()
