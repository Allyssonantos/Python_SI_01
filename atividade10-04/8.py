#Leia uma palavra e verifique se começa com vogal.
palavra = input("Digite uma palavra: ")
if palavra[0].lower() in 'aeiou': 
    print("A palavra começa com uma vogal.")
else:
    print("A palavra não começa com uma vogal.")
    