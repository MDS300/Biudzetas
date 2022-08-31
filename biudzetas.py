class Irasas:
    def __init__(self, suma):
        self.suma = suma


class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


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


biudzetas = Biudzetas()

while True:
    veiksmas = int(input("""
    Pasirinkite norimą veiksmą:
    1. Įvesti pajamas.
    2. Įvesti išlaidas.
    3. Parodyti pajamų/išlaidų balansą.
    4. Parodyti biudžeto ataskaitą.
    5. Išeiti iš programos.
    """))
    if veiksmas == 1:
        suma = int(input("Įveskite pajamas: "))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_informacija = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)

    if veiksmas == 2:
        suma = int(input("Įveskite išlaidas: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)

    if veiksmas == 3:
        biudzetas.gauti_balansa()
        print(f"Balansas: {biudzetas.gauti_balansa()}")
    if veiksmas == 4:
        biudzetas.parodyti_ataskaita()
    if veiksmas == 5:
        break
