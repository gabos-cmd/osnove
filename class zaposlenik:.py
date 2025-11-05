class zaposlenik:
    def _innit_(self, ime, prezime, placa):
        self.ime = ime
        self.prezime = prezime
        self.placa = placa

    def info(self):
        return f"{self.ime} {self.prezime} zarađuje {self.placa} kuna mjesečno."
    
class programmer(zaposlenik):
    def _init_(self, ime, prezime, placa, programski_jezik):
        super()._init_(ime,prezime,placa)
        self.programski_jezik = programski_jezik

    def prikazi_info(self):
        super().prikazi_info()
        print(f"Programski jezik: {self.programski_jezik}")


class menadzer(zaposlenik):
    def _init_(self, ime, prezime, placa, tim):
        super()._init_(ime, prezime, placa)
        self.tim = tim

    def prikazi_info(self):
        super().prikazi_info()
        print(f"Tim: {self.tim}")

# Kreiranje objekata
z1 = Zaposlenik("Ana", "Anić", 1200)
p1 = Programer("Petar", "Perić", 1800, ["Python", "JavaScript"])
m1 = Menadzer("Iva", "Ivić", 2500, ["Ana Anić", "Petar Perić"])

# Pozivanje metoda
print("--- Podaci o zaposleniku ---")
z1.prikazi_info()

print("\n--- Podaci o programeru ---")
p1.prikazi_info()

print("\n--- Podaci o menadžeru ---")
m1.prikazi_info()