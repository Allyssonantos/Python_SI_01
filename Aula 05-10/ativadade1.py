#faça um progrma que leia um nome e peso de várias pessoas, 
# guardando tudo em uma lista. No final, mostre:

#A) Quantas pessoas foram cadastradas
#B) Uma listagem com as pessoas mais pesadas
#C) Uma listagem com as pessoas mais leves

pessoas = [] # guardará os dados das pessoas
while True:
    nome = input("Digite o nome da pessoa: ") #perfuntar o nome da pessoa
    peso = float(input("Digite o peso da pessoa: ")) #perguntar o peso da pessoa
    pessoas.append((nome, peso)) # append adiciona uma tupla com o nome e peso na lista pessoas
    print(f"{nome} com {peso}kg foi cadastrado com sucesso!") #mensagem de sucesso
    continuar = input("Deseja continuar? (S/N): ").strip().upper() #perguntar se deseja continuar cadastrando pessoas
    if continuar == 'N':
        break # se a resposta for N, o loop é interrompido 
    
    

