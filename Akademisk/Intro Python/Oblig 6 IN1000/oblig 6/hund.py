'''Oppgave3:Hund'''


class Hund:  ##Oppretter klasse hund
    def __init__(self,alder,vekt):  ##opretter kontruktøren
        self.alder=alder    ##definerer kontruktøren til klassen
        self.vekt=vekt
        self.metthet=10



    def skrivUt(self):   ##metode som skal printe ut alderen og vekten på hunden
        print("Alderen på hunden er :",self.alder," år gammel\nVekten er:",self.vekt,"kg")

    def spring(self): ##metode som skal minke vekten hvis mettheten er mindre enn 5
        self.metthet-=1   ##minker mettheten med 1
        if self.metthet<5:  ##sjekker om mettheten er mindre enn 5
            self.vekt-=1
            print("Nå er vekten: ", self.vekt)      ##printer ut vekten
        else:
            print("Nå er vekten" ,self.vekt)



    def spis(self,mat):  ##metode som skal øke vekten hvis mettheten er større enn 7
        self.mat=mat     ##heltaltt som skal definere hvor mye den spiser
        self.metthet+self.mat  ##legger til hvor mye den spiser

        if self.metthet>7:  ##sjekker om mettheten er større en 7
            self.vekt+=1
            print("Nå er vekten: ",self.vekt)   ##printer vektene
        else:
            print("Nå er vekten:" ,self.vekt)
