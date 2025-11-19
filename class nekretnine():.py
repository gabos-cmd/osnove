class nekretnine():
    def __init__(self, adresa, kvadratura, bazna_cijena):
        self.adresa = adresa
        self.kvadratura = kvadratura
        self.bazna_cijena = bazna_cijena

    def izracunaj_cijenu(self):
        return self.bazna_cijena * self.kvadratura

    def ispisi_info(self):
        return f"Adresa: {self.adresa}, Kvadratura: {self.kvadratura}m², Cijena: {self.izracunaj_cijenu()} EUR"
    
class stan(nekretnine):
    def __init__(self, adresa, kvadratura, bazna_cijena, kat, ima_lift):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.kat = kat
        self.ima_lift = ima_lift

    def izracunaj_cijenu(self):
        cijena = super().izracunaj_cijenu()
        if self.ima_lift:
            cijena *= 1.05
        elif self.kat > 2:
            cijena *= 0.9
        return cijena

    def ispisi_info(self):
        return f"Stan je na katu {self.kat} - " + super().ispisi_info() + (", ima lift." if self.ima_lift else ", nema lift.")
    
class kuca(nekretnine):
    def __init__(self, adresa, kvadratura, bazna_cijena, povrsina_okucnice):
        super().__init__(adresa, kvadratura, bazna_cijena)
        self.povrsina_okucnice = povrsina_okucnice

    def izracunaj_cijenu(self):
        cijena = super().izracunaj_cijenu()
        cijena += self.povrsina_okucnice * 100
        return cijena

    def ispisi_info(self):
        return f"Kuća sa površinom okućnice {self.povrsina_okucnice}m² - " + super().ispisi_info()
    
def ispisi_izbornik():
    print("Izbornik:")
    print("1. Unesi stan")
    print("2. Unesi kuću")
    print("3. Prikaži sve nekretnine")
    print("4. Prodaja nekretnine")
    print("5. Izlaz")

nekretnine = []
while True:
    ispisi_izbornik()
    try:
        izbor = input("Unesite izbor (0/1/2/3/4/5): ")
        if izbor == "1":
            adresa = input("Unesite adresu stana: ")
            kvadratura = float(input("Unesite kvadraturu stana (m²): "))
            bazna_cijena = float(input("Unesite baznu cijenu po m² (EUR): "))
            kat = int(input("Unesite kat na kojem se stan nalazi: "))
            ima_lift = input("Ima li lift (da/ne): ").lower() == "da"
            novi_stan = stan(adresa, kvadratura, bazna_cijena, kat, ima_lift)
            nekretnine.append(novi_stan)
            print("Stan uspješno unesen.")
        elif izbor == "2":
            adresa = input("Unesite adresu kuće: ")
            kvadratura = float(input("Unesite kvadraturu kuće (m²): "))
            bazna_cijena = float(input("Unesite baznu cijenu po m² (EUR): "))
            povrsina_okucnice = float(input("Unesite površinu okućnice (m²): "))
            nova_kuca = kuca(adresa, kvadratura, bazna_cijena, povrsina_okucnice)
            nekretnine.append(nova_kuca)
            print("Kuća uspješno unesena.")
        elif izbor == "3":
            if not nekretnine:
                print("Nema unesenih nekretnina.")
            for nekretnina in nekretnine:
                print(nekretnina.ispisi_info())
        elif izbor == "4":
            adresa = input("Unesite adresu nekretnine za prodaju: ")
            for nekretnina in nekretnine:
                if nekretnina.adresa == adresa:
                    nekretnine.remove(nekretnina)
                    print("Nekretnina uspješno prodana.")
                    break
            else:
                print("Neispravan izbor.")
        elif izbor == "5":
            print("Izlaz iz programa.")
            break
        else:
            print("Neispravan izbor, pokušajte ponovno.")

    except ValueError:
        print("Pogrešan unos! Molimo unesite broj.")
