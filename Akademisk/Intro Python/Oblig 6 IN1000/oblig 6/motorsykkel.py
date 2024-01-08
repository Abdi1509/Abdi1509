'''oppgave1: Motorsykkel'''

class Motorsykkel:   ##opretter ny klasse motorsykkel
    def __init__ (self,merke,regist,kilometeravstand):  ##konstruktøren til klassen
        self.merke=merke                    ##definerer instavariabelene
        self.regist=regist
        self.kilometeravstand=kilometeravstand


    def kjor(self,km):    ##opretter ny metode som skal øke km avstanden med den gitte antallen
        self.km=km
        assert (km>=0)  ##sjekker om km er mer eller lik 0km
        return km + 10          ##retunerer avstanden + antall økt km(øker med 10km)


    def hentKilometerstand(self):   ##ny metode returnerer totale km
        km_okning=self
        sum=Motorsykkel.kjor(self,self.kilometeravstand)
        print("\nDu har økt distansen med:",10, "km, og blir tilsammen", sum, "km")
        return self

    def skrivUt(self):      ##metode som skal printe ut info om motorsykkelen

        print("\nMerken på motorsykkelen er: " +self.merke)
        print("Regist nummer er: " ,self.regist)
        print("Du har kjørt antall kilometer: ",self.kilometeravstand,"km")
