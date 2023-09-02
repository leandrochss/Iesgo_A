#Conversor de Moeda:
###Desenvolva um aplicativo que converte uma quantidade de uma moeda para outra, utilizando taxas de câmbio predefinidas.
### Bônus: faça o programa solicitar ao usuário a moeda de origem e a moeda de destino e a taxa de câmbio.

taxas_cambio = {
    ('USD', 'EUR'): 0.95,
    ('EUR', 'USD'): 1.18,
    ('USD', 'BRL'): 130.0,
    ('BRL', 'USD'): 0.0050,
    ('EUR', 'BRL'): 169.0,
    ('BRL', 'EUR'): 0.0030,
    
    # Adiciona mais taxas de câmbios quando for necessário

}

# Solicitar a moeda de origem, a moeda de destino e quantidade
moeda_origem = input("Digite a moeda de origem (USD, EUR, BRL):").upper()
moeda_destino = input("Digite a moeda de destino (USD, EUR, BRL):").upper()
quantidade = float(input("Digite a quantidade para ser convertida: "))

# Verificar se as moedas e a taxa de câmbio estão definadas
if (moeda_origem, moeda_destino) in taxas_cambio:
    taxas_cambio = taxas_cambio[(moeda_origem, moeda_destino)]
    valor_convertido = quantidade * taxas_cambio
    print(f"{quantidade} {moeda_origem} equivalem a {valor_convertido} {moeda_destino}")
else:
    print("As moedas ou a taxa de câmbio não está definida.")
