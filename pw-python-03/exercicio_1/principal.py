import os
import json
import analisa_ficheiro


def main():

    ficheiro = analisa_ficheiro.pede_nome()

    ficheiro_open = open(analisa_ficheiro.gera_nome(ficheiro), "w")

    dicionario = {"Nr. de Linhas": analisa_ficheiro.calcula_linhas(ficheiro),
                  "Caracteres": analisa_ficheiro.calcula_carateres(ficheiro),
                  "Palavra mais comprida": analisa_ficheiro.calcula_palavra_comprida(ficheiro),
                  "Ocorrencia de letras": analisa_ficheiro.calcula_ocorrencia_de_letras(ficheiro)
                  }

    json.dump(dicionario, ficheiro_open, indent=4, sort_keys=True)

    print(json.dumps(dicionario, indent=4, sort_keys=True), "\n\nO ficheiro", analisa_ficheiro.gera_nome(ficheiro),
          "foi criado\n")


if __name__ == "__main__":
    main()
