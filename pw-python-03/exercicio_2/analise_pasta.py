import os
import csv
import matplotlib
from matplotlib import pyplot as plt

def pede_pasta():
    while True:
        pasta = input("Este programa analisa o tipo de ficheiros presente numa pasta. Insira o caminho para uma pasta:")
        if not os.path.isdir(pasta):
            print("A pasta selecionada não existe")
            continue
        else:
            faz_calculos(pasta)
            return pasta
            
     

def faz_calculos(pasta):
    dict_info = {}
    lista = os.listdir(pasta)

    for ficheiros in lista:
        if os.path.isfile(os.path.join(pasta,ficheiros)):
            if ficheiros[ficheiros.find('.')+1:] not in dict_info:
                dict_info[ficheiros[ficheiros.find('.')+1:] ] = {"volume" : os.path.getsize(os.path.join(pasta,ficheiros)) , "quantidades" : 1}
            else:
                dict_info[ficheiros[ficheiros.find('.')+1:] ]["volume"] += os.path.getsize(os.path.join(pasta,ficheiros))
                dict_info[ficheiros[ficheiros.find('.')+1:] ]["quantidades"] += 1

    escrever_csv(dict_info)
    faz_grafico_queijos(dict_info)
    faz_grafico_barras(dict_info)
    return
    

def escrever_csv(dict_info):
    with open('resultados.csv', 'w', newline='') as ficheiro:
        campos = ['Extensao', 'Quantidade','Tamanho[kByte]']
        writer = csv.DictWriter(ficheiro, fieldnames=campos)
        writer.writeheader()
        for key in dict_info.keys():
            ficheiro.write(f"{key},{dict_info[key]['quantidades']},{dict_info[key]['volume']}\n")
    return
    

def faz_grafico_queijos(dict_info):
    listachaves =[]
    listavalores =[]

    for key,value in dict_info.items():
        if key not in listachaves:
            listachaves.append(key)
            listavalores.append(value['quantidades'])
        else:
            continue
    
    plt.pie(listavalores, labels=listachaves, autopct='%1.0f%%')
    plt.title("Quantidades de extensoes")
    plt.show()    
    return


def faz_grafico_barras(dict_info):
    listachaves =[]
    listavalores =[]

    for key,value in dict_info.items():
        if key not in listachaves:
            listachaves.append(key)
            listavalores.append(value['quantidades'])
        else:
            continue
    
    plt.bar(listachaves, listavalores)
    plt.title("Quantidades de extensoes")
    plt.show()
    return

pede_pasta()    
   



 

