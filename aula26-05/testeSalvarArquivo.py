nome = input("Nome: ")
idade = input("Idade: ")

arquivo = open("cadastro.txt", "w")
arquivo.write(nome + "\n")
arquivo.writw(idade)
