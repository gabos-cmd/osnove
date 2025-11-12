class Zaposlenik:
    def __init__(self, ime, prezime, placa):
        self.ime = ime
        self.prezime = prezime
        self.placa = placa

    def prikazi_info(self):
        print(f'Ime i prezime: {self.ime} {self.prezime}: {self.placa} EUR.', end=' ')

class Programer(Zaposlenik):
    def __init__(self, ime, prezime, placa, programski_jezici):
        super().__init__(ime, prezime, placa)
        self.programski_jezici = programski_jezici
    
    def prikazi_info(self):
        super().prikazi_info()
        print(f'Programski jezici: {self.programski_jezici}')

class Menadzer(Zaposlenik):
    def __init__(self, ime, prezime, placa, tim):
        super().__init__(ime, prezime, placa)
        self.tim = tim

    def prikazi_info(self):
        super().prikazi_info()
        print(f'Članovi tima: {self.tim}')

programski_jezici = ["Python", "Java"]

z1 = Zaposlenik("Arno", "Arnić", 1200)
p1 = Programer("Brki", "Brkić", 1800, programski_jezici)
m1 = Menadzer("Suri", "Surić", 2500, ["Arno Arnić", "Brki Brkić"])

# Pozivanje metoda
print("--- Podaci o zaposleniku ---")
z1.prikazi_info()

print("\n--- Podaci o programeru ---")
p1.prikazi_info()

print("\n--- Podaci o menadžeru ---")
m1.prikazi_info()