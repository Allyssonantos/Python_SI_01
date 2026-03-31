#Solicite:
#Usuário
#Senha
#Verifique:
#Se o usuário existe (ex: "admin")
#Se existir, verificar a senha (ex: "1234")
#Se correta → "Acesso permitido"
#Senão → "Senha incorreta"
#Senão → "Usuário não encontrado"

print('='*40)
usuario = input("Digite o nome de usuário: ")
print('='*40)
senha = input("Digite a senha: ")
print('='*40)

if usuario == "admin":
    if senha == "1234":
        print("Acesso permitido")
    else:
        print("Senha incorreta")
else:
    print("Usuário não encontrado")
