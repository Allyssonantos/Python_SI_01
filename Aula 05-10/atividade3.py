# Crie um programa que cria uma matriz de valores de dimensão 3x3,
# preenche com valores lidos pelo usuário e, ao final, mostra a matriz
# na tela com formatação correta.

matriz = []

for linha_atual in range(3):
    linha = []
    for coluna_atual in range(3):
        valor = int(input(f"Digite o valor para a posição [{linha_atual}][{coluna_atual}]: "))
        linha.append(valor)
    matriz.append(linha)

print("\nMatriz 3x3:")
for linha in matriz:
    print(" | ".join(f"{valor:>4}" for valor in linha))

