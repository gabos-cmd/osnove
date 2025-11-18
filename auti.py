class Vozilo:

    def __init__(self, marka, model, godina_proizvodnje, cijena):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.cijena = cijena

    def info(self):
        print(f"Marka: {self.marka}, Model: {self.model}, Godina: {self.godina_proizvodnje}, Cijena: {self.cijena} EUR")
    
    def promijeni_cijenu(self, nova_cijena):
        self.cijena = nova_cijena
        print(f"Cijena vozila {self.marka} {self.model} je promijenjena na {self.cijena} EUR")

vozilo1 = Vozilo("Volkswagen", "Bully", 1992, 7000)

class ElektricnoVozilo(Vozilo):

    def __init__(self, marka, model, godina_proizvodnje, cijena, domet_baterije):
        super().__init__(marka, model, godina_proizvodnje, cijena)
        self.domet_baterije = domet_baterije

    def info(self):
        super().info()
        print(f"Domet baterije: {self.domet_baterije} km")


def unos_vozila(marka, model, godina_proizvodnje, cijena):
    novo_vozilo = Vozilo(marka, model, godina_proizvodnje, cijena)
    autosalon.append(novo_vozilo)
    print(f"Novo vozilo {novo_vozilo.marka} {novo_vozilo.model} je uspjesno dodano.")


def unos_elektricnog_vozila(marka, model, godina_proizvodnje, cijena, domet_baterije):
    novo_elektricno_vozilo = ElektricnoVozilo(marka, model, godina_proizvodnje, cijena, domet_baterije)
    autosalon.append(novo_elektricno_vozilo)
    print(f"Novo elektricno vozilo {novo_elektricno_vozilo.marka} {novo_elektricno_vozilo.model} je uspjesno dodano.")


def pronadji_vozilo(marka, model):
    for vozilo in autosalon:
        if vozilo.marka == marka and vozilo.model == model:
            return vozilo
    return None
    

def ispisi_izbornik():
    print("-" * 30)
    print("------------- IZBORNIK --------------")
    print("--- 1. Dodaj novo (obicno) vozilo ---")
    print("- 2. Dodaj novo (elektricno) vozilo -")
    print("3. Ispisi podatke o odredenom vozilu")
    print("4. --- Promijeni cijenu vozilu -----")
    print("5. ------ Ispisi sva vozila --------")
    print("0. ----------- Izlaz ---------------")
    print("-" * 30)


autosalon = []

while True:
    ispisi_izbornik()

    try:
        izbor = int(input("Unesite broj opcije: "))
        
        if izbor == 0:
            print("Izlaz iz programa.")
            break

        elif izbor == 1:
            print("Unos novog vozila:")
            marka = input("Unesi marku vozila: ")
            model = input("Unesi model vozila: ")
            godina_proizvodnje = int(input("Unesi godinu proizvodnje: "))
            cijena = float(input("Unesi cijenu vozila (EUR): "))
            unos_vozila(marka, model, godina_proizvodnje, cijena)
        
        elif izbor == 2:
            print("Unos novog elektricnog vozila:")
            marka = input("Unesi marku elektricnog vozila: ")
            model = input("Unesi model elektricnog vozila: ")
            godina_proizvodnje = int(input("Unesi godinu proizvodnje: "))
            cijena = float(input("Unesi cijenu elektricnog vozila (EUR): "))
            domet_baterije = int(input("Unesi domet baterije (km): "))
            unos_elektricnog_vozila(marka, model, godina_proizvodnje, cijena, domet_baterije)
        
        elif izbor == 3:
            print("Pronalazak vozila:")
            marka = input("Unesi marku vozila: ")
            model = input("Unesi model vozila: ")
            vozilo = pronadji_vozilo(marka, model)
            if vozilo:
                vozilo.info()
            else:
                print("Vozilo nije u autosalonu.")

        elif izbor == 4:
            print("Promjena cijene vozila:")
            marka = input("Unesi marku vozila: ")
            model = input("Unesi model vozila: ")
            vozilo = pronadji_vozilo(marka, model)
            if vozilo:
                nova_cijena = float(input("Unesi novu cijenu (EUR): "))
                vozilo.promijeni_cijenu(nova_cijena)
            else:
                print("Vozilo nije u autosalonu.")

        elif izbor == 5:
            print("Ispis svih vozila u autosalonu:")
            if autosalon:
                for vozilo in autosalon:
                    vozilo.info()
            else:
                print("Nema vozila u autosalonu.")

        else:
            print("Unesite broj od 0 do 5 za pravilan odabir.")
    
    except ValueError:
        print("Unesite broj od 0 do 5 za pravilan odabir.")
        continue