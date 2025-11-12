class Recept:

    def __init__(self, ime):
        self.ime = ime
        self.lista_sastojaka = []

    def dodaj_sastojak(self, sastojak, količina):
        self.lista_sastojaka.append({sastojak : količina})
        print(f'Sastojak {sastojak} je dodan.')

    def prikaz(self):
        print(f'Naziv: {self.ime}')
        print(f'Sastojci: {self.lista_sastojaka}')
    

class Kuharica:

    def __init__(self, ime):
        self.ime = ime
        self.lista_recepata = []
    
    def dodaj_recept(self, recept_objekt):
        self.lista_recepata.append(recept_objekt)
        print(f'Recept {recept_objekt.ime} je dodan.')

    def pronadi_recept(self, recept_objekt):
        pronasao = False
        for recept in self.lista_recepata:
            if recept_objekt == recept:
                recept.prikaz()
                pronasao = True
                break
        if not pronasao:
            print(f'{recept_objekt.ime} nije pronađen!')
            
        

recept1 = Recept('medenjaci')
recept1.dodaj_sastojak('med', '5tbsp')

kuharica1 = Kuharica('gabriel')
kuharica1.dodaj_recept(recept1)
kuharica1.pronadi_recept(recept1)