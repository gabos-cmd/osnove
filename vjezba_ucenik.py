class Ucenik:

    def __init__(self, ime, prezime, razred):
        self.ime = ime
        self.prezime = prezime
        self.razred = razred
        self.ocjene = []


    def dodaj_ocjenu(self, ocjena):

        if isinstance (ocjena, int) and 1 <= ocjena <= 5:

            self.ocjene.append(ocjena)
            print (f'INFO: Učeniku {self.ime} {self.prezime} je upisana ocjena {ocjena}.')
        
        else:
            print (f'GREŠKA: Ocjena "{ocjena}" nije valjana. Upišite vrijednost od 1 do 5')

            
    def izracunaj_prosjek(self):

        if not self.ocjene:
            return 0.0
        
        else:

            return sum(self.ocjene) / len(self.ocjene)



    def info(self):
        print(self.ime, self.prezime, self.razred)

        prosjek = self.izracunaj_prosjek()
        print(f'Prosjek: {prosjek:.2f}')



ucenik1 = Ucenik('Mak', 'Jokić', '4.b OG')
ucenik2 = Ucenik('Antonio', 'Radović', '4.b OG')


ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)
ucenik1.dodaj_ocjenu(5)



ucenik2.dodaj_ocjenu(3)
ucenik2.dodaj_ocjenu(1)
ucenik2.dodaj_ocjenu(1)
ucenik2.dodaj_ocjenu(1)




ucenik1.info()
ucenik2.info()


