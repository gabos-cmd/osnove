import csv

class Ucenik:
    """
    Nacrt (klasa) za stvaranje objekata koji predstavljaju ucenike.
    Svaki ucenik ima ime, prezime, razred i listu ocjena.
    """

    def __init__(self, ime, prezime, razred):
        """Inicijalizira novi objekt Ucenik s pocetnim podacima."""
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []  # prazna lista ocjena

    def dodaj_ocjenu(self, ocjena):
        """Dodaje novu ocjenu u listu ocjena ucenika."""
        if isinstance(ocjena, int) and 1 <= ocjena <= 5:
            self.ocjene.append(ocjena)
            print(f"INFO: Uceniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.")
        else:
            print(f"GRESKA: Ocjena '{ocjena}' nije vazeca. Molimo unesite broj od 1 do 5.")

    def izracunaj_prosjek(self):
        """Vraca prosjek svih ocjena ucenika."""
        if not self.ocjene:
            return 0.0
        return sum(self.ocjene) / len(self.ocjene)

    def info(self):
        """Ispisuje sve dostupne informacije o uceniku na konzolu."""
        print("-" * 30)
        print(f"Ime i prezime: {self.ime} {self.prezime}")
        print(f"Razred: {self.razred}")
        
        if self.ocjene:
            print("Ocjene:", ", ".join(map(str, self.ocjene)))
        else:
            print("Ocjene: (nema upisanih ocjena)")
            
        prosjek = self.izracunaj_prosjek()
        print(f"Prosjek ocjena: {prosjek:.2f}")
        print("-" * 30)


# ------------------ Pomocne funkcije ------------------ #

def ispisi_izbornik():
    print('-' + '='*20 + '-')
    print('Glavni izbornik')
    print('-' + '='*20 + '-')
    print('0 - Izlaz iz programa')
    print('1 - Unos novog ucenika')
    print('2 - Unos ocjene uceniku')
    print('3 - Ispis podataka o uceniku')
    print('4 - Spremi u CSV formatu')
    print('5 - Ispisi CSV podatke')


def upisUcenika(ime, prezime, razred):
    return Ucenik(ime, prezime, razred)


def upisOcjene(ucenik, ocjena):
    ucenik.dodaj_ocjenu(ocjena)


def ispisUcenika(ucenik):
    ucenik.info()


def spremi_u_csv(lista, ime_datoteke):
    """Spremanje liste ucenika u CSV datoteku."""
    with open(ime_datoteke, mode='w', newline='', encoding='utf-8') as datoteka:
        polja = ['ime', 'prezime', 'razred', 'ocjene']
        writer = csv.DictWriter(datoteka, fieldnames=polja)
        writer.writeheader()
        for u in lista:
            ocjene_str = ",".join(map(str, u.ocjene))  # npr. "5,4,3"
            writer.writerow({
                'ime': u.ime,
                'prezime': u.prezime,
                'razred': u.razred,
                'ocjene': ocjene_str
            })
    print(f"Spremljeno u {ime_datoteke}")


def ispisi_csv(ime_datoteke):
    """Ucita ucenike iz CSV datoteke i ispise ih."""
    ucitani_ucenici = []
    with open(ime_datoteke, mode='r', encoding='utf-8') as datoteka:
        reader = csv.DictReader(datoteka)
        for red in reader:
            u = Ucenik(red['ime'], red['prezime'], red['razred'])
            ocjene_text = red.get('ocjene', '')
            if ocjene_text:
                ocjene_list = []
                for dio in ocjene_text.split(','):
                    dio = dio.strip()
                    if dio.isdigit():
                        ocjene_list.append(int(dio))
                u.ocjene = ocjene_list
            ucitani_ucenici.append(u)

    print(f"Ucitano iz {ime_datoteke}")
    for u in ucitani_ucenici:
        u.info()
    return ucitani_ucenici


# ------------------ Glavni dio programa ------------------ #

lista_ucenika = []

while True:
    ispisi_izbornik()
    try:  
        odgovor = int(input('Odaberite opciju (0/1/2/3/4/5): '))

        if odgovor == 0:
            print("Izlaz iz programa. Dovidenja!")
            break

        elif odgovor == 1:
            print('Unos novog ucenika:')
            ime = input("Unesite ime ucenika: ")
            prezime = input("Unesite prezime ucenika: ")
            razred = input("Unesite razred ucenika: ")
            ucenik = upisUcenika(ime, prezime, razred)
            lista_ucenika.append(ucenik)
            print(f"INFO: Ucenik {ime} {prezime} uspjesno unesen.")

        elif odgovor == 2:
            print('Unos ocjene uceniku:')
            ime = input("Unesite ime ucenika: ")
            pronaden = False
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    ocjena = int(input("Unesite ocjenu (1-5): "))
                    upisOcjene(ucenik, ocjena)
                    pronaden = True
                    break
            if not pronaden:
                print(f"GRESKA: Ucenik s imenom '{ime}' nije pronaden.")

        elif odgovor == 3:
            print('Ispis podataka o uceniku:')
            ime = input("Unesite ime ucenika: ")
            pronaden = False
            for ucenik in lista_ucenika:
                if ucenik.ime == ime:
                    ispisUcenika(ucenik)
                    pronaden = True
                    break
            if not pronaden:
                print(f"GRESKA: Ucenik s imenom '{ime}' nije pronaden.")

        elif odgovor == 4:
            print('Spremanje podataka u CSV')   
            ime_datoteke = input('Ime datoteke (bez .csv): ') + '.csv'   
            spremi_u_csv(lista_ucenika, ime_datoteke)
        
        elif odgovor == 5:
            print('Ispis podataka iz CSV')   
            ime_datoteke = input('Ime datoteke (bez .csv): ') + '.csv'
            ispisi_csv(ime_datoteke)
        
        else:
            print("GRESKA: Nepoznata opcija.")

    except ValueError:
        print("GRESKA: Molimo unesite brojevnu vrijednost.")
        continue