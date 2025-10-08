class Knjiga:
    def __init__(self,naslov, autor, godina):
        self.naslov = naslov
        self.autor = autor
        self.godina_izdanja = godina

        print(self.naslov)
        print(self.autor)
        print(self.godina_izdanja)


Knjiga1 = Knjiga("RedRising", "Pierce_Brown", "2014")
Knjiga2 = Knjiga("Hunger games","Suzanne_Collins", "2008")

