#Leia uma string e conte vogais usando for e if.
string = input("Digite uma string: ")
contador_vogais = 0
for char in string:
    if char.lower() in 'aeiou':
        contador_vogais += 1
print("A string contém", contador_vogais, "vogais.")

