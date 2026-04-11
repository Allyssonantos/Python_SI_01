#Leia uma string e verifique se ela contém apenas letras (sem números ou símbolos).

string = input("Digite uma string: ")
if string.isalpha():
    print("A string contém apenas letras.")
else:
    print("A string contém caracteres que não são letras.")

    