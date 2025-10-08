class Bankovni_Racun:
    def __init__(self, ime, stanje):
        self.ime_vlasnika = ime
        self.trenutno_stanje = stanje

    def uplati(self, iznos):
        self.trenutno_stanje += iznos
        print(f"Uplaćeno {iznos} kn. Novo stanje: {self.trenutno_stanje} kn.")

    def isplati(self, iznos):
        if self.trenutno_stanje >= iznos:
            self.trenutno_stanje -= iznos
            print(f"Isplaćeno {iznos} kn. Novo stanje: {self.trenutno_stanje} kn.")
        else:
            print("Nedovoljno sredstava na racunu.")

    def ispis_stanja(self):
        print(f"Stanje racuna za {self.ime_vlasnika}: {self.trenutno_stanje} kn.")

racun1 = Bankovni_Racun("Marko Marić", 1000)
racun1.ispis_stanja()
racun1.uplati(500)
racun1.isplati(200)
racun1.isplati(1500)
racun1.ispis_stanja()