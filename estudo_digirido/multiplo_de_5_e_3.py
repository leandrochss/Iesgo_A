# Exercício 2: Faça uma função que recebe um número e imprime no console se ele é múltiplo de 5 e de 3 ou False caso contrário


def input_numero(mensagem,tipo): 
   while True:
        try:
            num = tipo(input(mensagem+" "))
            return num
        except ValueError:
            print("Por Favor, Digite a entrada correta! \n")

def multiplo_de_5_e_3(dividendo):

    if dividendo % 5 == 0 and dividendo % 3 ==0:
        return True
    else:
        return False
    
num = input_numero("Digite um numero: ",int)
print(f"{num} e multiplo de 5 e de 3: {multiplo_de_5_e_3(num)}")