### Crie um programa que recebe o ano de nascimento do usuário e calcula a idade atual.
### Bônus: faça o programa retornar o signo do usuário de acordo com o mês e dia do seu nascimento.
# Calculadora de Idade:

# Função para calcular o signo com base na data de nascimento
def calcular_signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gêmeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <=21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    else:
        return "Peixes" 

# Solicitar o ano de nascimento do usuário
ano_nascimento = int(input("Digite seu ano de nascimento: "))
mes_nascimento = int(input("Digite seu mês de nascimento: "))
dia_nascimento = int(input("Digite seu dia de nascimento: "))

# Obter a data atual
from datetime import datetime
data_atual = datetime.now()

# Calcular a idade
idade = data_atual.year - ano_nascimento

# Calcular o signo
signo = calcular_signo(dia_nascimento, mes_nascimento)

# Exibir a idade e o signo
print(f"A sua idade é: {idade} anos")
print(f"O seu signo é: {signo}")