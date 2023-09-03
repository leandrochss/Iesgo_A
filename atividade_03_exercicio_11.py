# Gerador de Cartão de Crédito:
### Crie um gerador de cartão de crédito que gere números de cartão de crédito válidos para a empresa de cartão de crédito especificada.
### Bônus: gere um número de cartão de crédito válido aleatoriamente para cada uma das empresas de cartão de crédito suportadas pelo seu aplicativo.
import random

import random
from datetime import datetime, timedelta

def gerador_cartao():
    bandeiras = ['Visa', 'Mastercard', 'American Express']
    print("\n1: Visa. \n2: Mastercard. \n3: American Express.")
    while True:
        escolha = int(input(f"\nQual Bandeira de Cartão de Crédito? "))
        if escolha > 0 and escolha <= len(bandeiras):
            break
    bandeira = bandeiras[escolha - 1]
    if bandeira not in bandeiras:
        return 'Bandeira válida'
    empresa, numero = gerador_numero_cartao_especifico(bandeira)
    cvv = gerador_cvv(empresa)
    data_validade = gerador_data_validade()
    mensagem = f'Número do Cartão {empresa}: {numero}, Código Segurança CVV: {cvv}, Data de Validade: {data_validade}'
    return mensagem

def gerador_numero_cartao_especifico(bandeira):
    prefixos = {'Visa': '4', 'Mastercard': '5', 'American Express': '37'}
    empresa = bandeira
    prefixo = prefixos[empresa]
    comprimento = 16 if empresa != 'American Express' else 15
    numero = gerador_numero_cartao(prefixo, comprimento)
    return empresa, numero

def gerador_numero_cartao(prefixo, comprimento):
    numero = prefixo + ''.join(random.choice('0123456789') for _ in range(comprimento - len(prefixo) - 1))
    numero += digito_verificador(numero)
    return numero

def digito_verificador(numero):
    soma = sum(int(n) if i % 2 else int(n)*2 if int(n)*2 < 10 else int(n)*2 - 9
                for i, n in enumerate(reversed(numero)))
    return str((10 - soma) % 10)

def gerador_cvv(empresa):
    comprimento = 4 if empresa == 'American Express' else 3
    return ''.join(random.choice('0123456789') for _ in range(comprimento))

def gerador_data_validade():
    hoje = datetime.now()
    data_validade = hoje + timedelta(days=365 * 3) # cartão válido por 3 anos a partir da data atual
    return data_validade.strftime('%m/%y')

# Como usar:
mensagem = gerador_cartao()
print(mensagem)