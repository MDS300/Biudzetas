from moduliai.klase_Biudzetas import Biudzetas

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
