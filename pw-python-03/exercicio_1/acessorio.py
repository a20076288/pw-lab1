import os

def pede_nome():
	while True:
		ficheiro = input("Qual o nome do ficheiro que quer abrir?")
		if ficheiro.split(".")[-1] != "txt":
			print("O ficheiro tem de ter a extensão '.txt' ")
			continue

		elif not os.path.exists(ficheiro):
			print("O ficheiro não existe")
			continue

		else:
			return ficheiro

def gera_nome(ficheiro):
	return ficheiro.replace(".txt", ".json")