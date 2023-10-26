def criar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(conteudo)
    print(f"Seu arquivo '{nome_arquivo}' foi criado com sucesso!")

def acrescentar_conteudo(nome_arquivo, novo_conteudo):
    with open(nome_arquivo, "a") as arquivo:
        arquivo.write("\n" + novo_conteudo)  # Adicione uma quebra de linha antes do novo conteúdo
    print(f"Conteúdo adicionado ao arquivo '{nome_arquivo}'!")

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

nome_do_arquivo = "meu_arquivo.txt"

# Criar o arquivo
conteudo_inicial = "Este é o conteúdo do arquivo!"
criar_arquivo(nome_do_arquivo, conteudo_inicial)

# Acrescentar conteúdo
novo_conteudo = "Novo conteúdo do arquivo!"
acrescentar_conteudo(nome_do_arquivo, novo_conteudo)

# Ler e exibir o conteúdo
conteudo_lido = ler_arquivo(nome_do_arquivo)
print(f"Conteúdo do arquivo '{nome_do_arquivo}':")
print(conteudo_lido)
