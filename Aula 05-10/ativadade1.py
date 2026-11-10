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
        break # se a resposta for N, o loop é interrompido 4

if pessoas: #verifica se a lista pessoas não está vazia
    total_pessoas = len(pessoas) #quantidade de pessoas cadastradas
    pesos = [peso for _, peso in pessoas] #cria uma lista apenas com os pesos
    max_peso = max(pesos) #encontra o maior peso
    min_peso = min(pesos) #encontra o menor peso

    mais_pesadas = [nome for nome, peso in pessoas if peso == max_peso] #lista das pessoas mais pesadas
    mais_leves = [nome for nome, peso in pessoas if peso == min_peso] #lista das pessoas mais leves

    print(f"\nTotal de pessoas cadastradas: {total_pessoas}") #mostra a quantidade de pessoas cadastradas
    print(f"Pessoas mais pesadas ({max_peso}kg): {', '.join(mais_pesadas)}") #mostra as pessoas mais pesadas
    print(f"Pessoas mais leves ({min_peso}kg): {', '.join(mais_leves)}") #mostra as pessoas mais leves
    
    

