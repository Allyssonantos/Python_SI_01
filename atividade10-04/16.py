#Leia uma string e mostre os 3 primeiros caracteres.


string = input("Digite uma string: ")
if len(string) >= 3:
    print("Os 3 primeiros caracteres são:", string[:3])
else:
    print("A string tem menos de 3 caracteres.")
    