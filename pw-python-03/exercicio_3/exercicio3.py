import os

def pede_pasta():
    while True:
        pasta = input("Insira o caminho para uma pasta: ")
        if not os.path.isdir(pasta):
            print("A pasta selecionada não existe")
            continue
        else:
            return pasta

def calcula_tamanho_pasta(pasta):
    tamanho = 0    

    for ficheiros in os.listdir(pasta):
        if os.path.isdir(os.path.join(pasta,ficheiros)):
            tamanho += calcula_tamanho_pasta(os.path.join(pasta,ficheiros))            

        elif os.path.isfile(os.path.join(pasta,ficheiros)):
            tamanho += os.path.getsize(os.path.join(pasta,ficheiros)) / 1024            
        
    print("O tamanho total da pasta", pasta, "é: ", "{:.2f}".format(tamanho / 1024), "MBytes\n")
    return tamanho 

calcula_tamanho_pasta(pede_pasta()) / 1024