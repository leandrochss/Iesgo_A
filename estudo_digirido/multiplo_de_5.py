# Exercício 1: Faça uma função que recebe um número e retorna True se ele é múltiplo de 5 ou False caso contrário

def input_numero(mensagem,tipo): 
   while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Por Favor, Digite uma  entrada correta! \n")


def multiplo_de_5(dividendo):

    if dividendo % 5 == 0:
        return True
    else:
        return False
    
num = input_numero("Digite um numero: ",int)
print(f"{num} e multiplo de 5: {multiplo_de_5(num)}")