from moduliai.klase_Biudzetas import Biudzetas
import pickle

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
        with open("biudzetas.pkl", "rb") as failas:
            biudzetas = pickle.load(failas)
        suma = int(input("Įveskite pajamas: "))
        siuntejas = input("Įveskite siuntėją: ")
        papildoma_informacija = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, papildoma_informacija)
        with open("biudzetas.pkl", "wb") as failas:
            pickle.dump(biudzetas, failas)

    if veiksmas == 2:
        with open("biudzetas.pkl", "rb") as failas:
            biudzetas = pickle.load(failas)
        suma = int(input("Įveskite išlaidas: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įsigyta prekė/paslauga: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        with open("biudzetas.pkl", "wb") as failas:
            pickle.dump(biudzetas, failas)

    if veiksmas == 3:
        with open("biudzetas.pkl", "rb") as failas:
            biudzetas = pickle.load(failas)
        biudzetas.gauti_balansa()
        print(f"Balansas: {biudzetas.gauti_balansa()}")

    if veiksmas == 4:
        with open("biudzetas.pkl", "rb") as failas:
            biudzetas = pickle.load(failas)
        biudzetas.parodyti_ataskaita()
    if veiksmas == 5:
        break
