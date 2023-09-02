#Calculadora de IMC (Índice de Massa Corporal):
### Crie uma calculadora que permite ao usuário calcular seu IMC com base em seu peso e altura.
### Bônus: responda se o usuário está acima, abaixo ou dentro do peso ideal.

def calcular_imc(peso, altura):
    # Fórmula do IMC: IMC = peso / (altura * altura)
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso ideal"
    elif 18.5 <= imc < 24.9:
        return "Dentro do peso ideal"
    elif 27.9 <= imc < 39.9:
        return "Acima do peso ideal"
    else:
        return "Obeso"

def main():
    print("Calculadora de IMC (Índice de Massa Corporal)")
    peso = float(input("Digite seu peso em quilogramas: "))
    altura = float(input("Digite sua altura em metros: "))
    
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    
    print(f"Seu IMC é {imc:.2f}")
    print(f"Você está classificado como: {classificacao}")

if __name__ == "__main__":
    main()