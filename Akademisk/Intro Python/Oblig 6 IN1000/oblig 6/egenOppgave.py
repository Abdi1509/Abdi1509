
class Person:  ##Opretter klassen Person
    def __init__(self,navn,alder,hobbyer): ##kontruktøren
        self.navn=navn   ##definerer kontruktøren
        self.alder=alder
        self.hobbyer=hobbyer
        self.liste=[]  ##lager ny liste



    def leggTilHobby(self,aktiviteter): ##metode som skal legge til nye hobbyer

        self.aktiviteter=aktiviteter
        self.liste.append(self.aktiviteter)  ##legger til nye hobbyer i listen

        return self.liste  ##returnerer listen

    def skrivHobbyer(self,hobbyer_info):
        Person.leggTilHobby(hobbyer_info)  ##metode som gir brukeren mulighet til å skrive flere hobbyer

        svar2=input("Har du flere hobbyer?: ")
        svar2=svar2.lower() ##setter svarer fro små skrift
        if svar2=="ja":
           while svar2=="ja": ##loop som spør om flere hobbyer hvis brukeren oppgir ja
                hobbyer_info=input("oppgi den ekstra hobbyen du har: ")
                Person.leggTilHobby(hobbyer_info)

                svar3=input("Flere?: ")
                if svar3=="nei":  ##Hvis svare er nei skriver den ut listen
                    print("\nDen er grei! Dine hobbyer er: ", self.liste)
                elif svar3=="ja":
                    svar2=="ja"
                else:
                    print("feil")
        elif svar2=="nei":
            print("\nDen er grei! Dine hobbyer er: ", self.liste)

        else:
            print("feil")


    def skrivUt(self):   ##Skriver ut navnet og alderen til brukeren
        print("\nNavnet ditt er: ",self.navn)
        print("Din alder er: ",self.alder)

        Person.skrivHobbyer(hobbyer_info)



svar1=input("velg enten i mellom s: ")  ##programmet starter mede i
while svar1=="i":  ##så lenge svaret er i vil loopen kjøres

    navn_info=str(input("Hei og velkommen, Vennligst oppgi navn: "))  ##henter inn info om navn,alder og hobbyer
    alder_info=int(input("Vennligst oppgi alder: "))
    hobbyer_info=str(input("Vennligst oppgi favoritt hobbyen din: "))


    Person=Person(navn_info,alder_info,hobbyer_info) ##kaller på klassen og oppgir objekter
    Person.skrivUt()

    if svar1=="s":  ##hvis brukeren skriver s vil programmet ikke starte
        break;
