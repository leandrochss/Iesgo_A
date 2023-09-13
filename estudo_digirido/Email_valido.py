# Exercício 8: Faça um programa que solicita ao usuario inserir um email e retorna se ele é válido ou não.

import re

def verifica_email():
    email = input("Digite um email: ")
    padrao = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(padrao, email)):
        print("O email é válido.")
    else:
        print("O email não é válido.")

verifica_email()
