#Leia uma string e conte quantas letras maiúsculas existem.
string = input("Digite uma string: ")
contador_maiusculas = 0
for char in string:
    if char.isupper():
        contador_maiusculas += 1
print("A string contém", contador_maiusculas, "letras maiúsculas.")