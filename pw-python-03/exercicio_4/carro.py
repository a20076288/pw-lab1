class Automovel():
    def __init__(self, cap_dep, quant_comb, consumo):
        self.cap_dep = cap_dep
        self.quant_comb = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return self.quant_comb

    def autonomia(self):
        return int(self.quant_comb * 100 / self.consumo)

    def abastece(self, litros):
        if self.quant_comb + litros > self.cap_dep:
            return -1
        else:
            self.quant_comb += litros
            self.quant_comb = int((self.quant_comb *100 / self.consumo))
            return self.quant_comb

    def percorre(self, distancia):
        if distancia > self.autonomia():
            return -1
        else:
            self.quant_comb -= distancia
            return self.quant_comb


def main():

    carro = Automovel(60,10,15)

    print(carro.autonomia())
    print(carro.abastece(45))
    print(carro.percorre(150))
    print(carro.percorre(250))


if __name__ == "__main__":
    main()
