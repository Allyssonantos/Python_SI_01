with open("aula26-05/cadastro.txt", "r") as arquivo:
    conteudo = []
    for linha in arquivo:
        conteudo.append(linha.strip()) #strip() remove os espaços em branco no início e no final da string

print(conteudo)
