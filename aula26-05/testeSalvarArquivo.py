nome = input("Nome: ")
idade = input("Idade: ")

arquivo = open("aula26-05/cadastro.txt", "a")
arquivo.write(nome + "\n")
arquivo.write(idade + "\n")

arquivo.close()


