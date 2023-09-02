#Conversor de Temperatura:
### Crie um conversor de temperatura que permita ao usuário converter entre Celsius e Fahrenheit.
### Bônus: permita que o usuário especifique o número de casas decimais que deseja exibir.

def converter_celsius_para_fahrenheit(celsius, casas_decimais):
    fahrenheit = (celsius *9/5) + 32
    return round(fahrenheit, casas_decimais)

def converter_fahrenheit_para_celsius(fahrenheit, casas_decimais):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, casas_decimais)

print("Conversor de Temperatura")
print("Opções:")
print("1. Converter de Celsius para Fahrenheit")
print("2. Converter de Fahrenheit para Celsisus")

opcao = input("Escolha uma opção (1/2): ")

if opcao == "1":
    celsius = float(input ("Digite a temperatura em Celsisus: "))
    casas_decimais = int(input("Digite o número de casas decimais desejado: "))
    fahrenheit = converter_celsius_para_fahrenheit(celsius, casas_decimais)
    print(f"{celsius}°C equivalem a {fahrenheit}°F")

elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenehit: "))
    casas_decimais = int(input("Digite o número de casas decimais desejado: "))
    celsius = converter_fahrenheit_para_celsius(fahrenheit, casas_decimais)
    print(f"{fahrenheit}°F equivalem a {celsius}°C")
else:
    print("Opção inválida. Escolha 1 ou 2.")