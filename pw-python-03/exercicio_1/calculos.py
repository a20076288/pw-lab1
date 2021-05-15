import os

def calcula_linhas(ficheiro):

	ficheiro = open(ficheiro, "r")
	return len(ficheiro.readlines())

def calcula_carateres(ficheiro):

	ficheiro = open(ficheiro, "r")
	return len(ficheiro.read())  

def calcula_palavra_comprida(ficheiro):

	ficheiro = open(ficheiro, "r")
	texto = ficheiro.read().split()
	ficheiro.close()

	palavra_comprida = ""

	for palavra in texto:
		if len(palavra) > len(palavra_comprida):
			palavra_comprida = palavra

	return palavra_comprida   

def calcula_ocorrencia_de_letras(ficheiro):
    ficheiro = open(ficheiro, "r")
    texto = ficheiro.read().lower()
    ficheiro.close()

    dicionario = {}

    for palavra in texto:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1
    
    return dicionario