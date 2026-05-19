import random

frutas = [
    "abacaxi", "abacate", "acerola", "ameixa", "amora",
    "banana", "caju", "carambola", "cereja", "coco",
    "damasco", "figo", "framboesa", "goiaba", "graviola",
    "jabuticaba", "jaca", "kiwi", "laranja", "limão",
    "maçã", "mamão", "manga", "maracujá", "melancia",
    "melão", "morango", "nectarina", "pera", "pêssego",
    "pitanga", "pitaya", "romã", "tangerina", "uva",
    "umbu", "cabeludinha", "physalis", "cupuaçu", "bacaba",
    "buriti", "cajá", "cambuci", "seriguela", "taperebá",
    "uvaia", "pequi", "jenipapo", "murici", "araticum"]


def boneco(erro):
    if (erro == 0):
        print(" ______    ")
        print("|/   (   ) ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif (erro == 1):         
        print(" ______")
        print("|/   ( O ) ")
        print("|          ")
        print("|          ")
        print("|          ")
    elif (erro == 2):
        print(" ______")
        print("|/   ( O ) ")   
        print("|      |   ")
        print("|      |   ")
        print("|          ")
    elif (erro == 3):
        print(" ______")
        print("|/   ( O ) ")  
        print("|     \|   ")
        print("|      |   ")
        print("|          ")
    elif (erro == 4):
        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|          ")
    elif (erro == 5):
        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|     /    ")
    elif (erro == 6):
        print(" ______")
        print("|/   ( O ) ")   
        print("|     \|/  ")
        print("|      |   ")
        print("|     / \  ")
    elif (erro == 7):
        print(" ______")
        print("|/    (+)  Você foi enforcado")   
        print("|     \|/  Tente novamente!!!")
        print("|      |   ")
        print("|     / \  ")
    elif (erro == 8):
        print("      XX      Parabens!!")
        print("     XXXX     Você conseguiu.")
        print("    XXXXXX")
        print("   XXXXXXXX")
        print("      ||   ")

def cab():
    print("-"*30)
    print("      Joguinho da Forca")
    print("-"*30)

def painel(l):
    for x in l:
        print(x, end=" ")
    print()

acertou = False
palavra = random.choice(frutas).upper()
linha = list("_" * len(palavra))
usadas = ""
err = 0

while not acertou:

    cab()
    print(f"Fruta com {len(palavra)} letras")
    print()
    boneco(err)
    print()    
    painel(linha)
    print()
    print(f"{7-err} chances restantes - Letras ja usadas:{usadas} ")
    print()
    chute = input("Uma Letra: ").upper()

    usadas = usadas + chute + " "
    
    if (palavra.find(chute) > -1):
        for x in range(len(palavra)):
            if (palavra[x] == chute):
                linha[x]=chute
        if (not "_" in linha):
            painel(linha)
            print()
            boneco(8)
            
            acertou = True
    else:
        err = err + 1     
        if (err > 6):
            boneco(7)
            break    
        boneco(err)                       
    print()
    print()  
    print("Fim do programa")