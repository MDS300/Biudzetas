from moduliai.klase_irasas import Irasas
from moduliai.klase_PajamuIrasas import PajamuIrasas
from moduliai.klase_IslaiduIrasas import IslaiduIrasas


class Biudzetas:
    def __init__(self):
        self.zurnalas = []


    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(pajamos)


    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(islaidos)


    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            if isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                print(f"Pajamos: {irasas.suma}, {irasas.siuntejas}, {irasas.papildoma_informacija}")
            if isinstance(irasas, IslaiduIrasas):
                print(f"Išlaidos: {irasas.suma}, {irasas.atsiskaitymo_budas}, {irasas.isigyta_preke_paslauga}")