from random import randint
from celle import Celle


class Spillebrett:  ## Klasse spillebrett blir oprettet
    def __init__(self, rader, kolonner):                 ##Konstruktøren som skal ta imot to verdier fra brukeren som argument
        self._rader = rader                              ##Definerer som instansvaribeler for både rader og kolonner
        self._kolonner = kolonner

        #self._rutenett = [[Celle() for rad in range(self._rader)]for kolonner in range(self._kolonner)]   -->OBS!!! : Fikk litt komplikasjoner med definsjonene til brettet der hvor den misforstår hvordan plasseringen til cellene skal være

        self._rutenett = []                              ##Definerer rutenettet som en tom liste --> (Selve spillebrettet)
        for rad in range (self._rader):                  ##Går gjennom hver rad som er inrange av raden brukeren oppgir og lager et tom liste for det
            liste = []
            self._rutenett.append(liste)                 ##Setter inn tomme listen for hver rad inn i selve rutenettet
            for kolonne in range(self._kolonner):        ## og for hver kolonne skal det innholdet cellene
                liste.append(Celle())

        self._generasjon = 0                             ##Setter genrasjon på 0 som start (nullstiller)
        self._generer()                                  ##kaller på metoden _generer




    def tegnBrett(self):                                 ##metod som tegner  og viser fram brettet
        for i in self._rutenett:                         ##nøstet løkke som irriterer ut elementene i rutenettet
            print(" ")                                   ##Printer mellomrom
            for j in i:                                  ##går dypere inn i listen som innholder kolonnene
                print(j,end="")                          ## og tilsutt printer ut cellene som er i kolonnene



    def oppdatering(self):                               ## Metode som oppdaterer cellene
        levende=[]                                      ##Lager to nye tomme lister som skal enten innholde levende celler eller døende
        doende=[]

        for rad in range(self._rader):                  ##irriterer gjennom radene som brukeren oppgir
            for kolonne in range(self._kolonner):        ## Går et hakk dypere
                nabo = self.finnNabo(rad,kolonne)        ##Oppretter en ny variabel som skal finne naboenene for hvert av cellene
                celle = self._rutenett[rad][kolonne]     ##Definerer posisjonen til varibalene celle som er i kolonnene
                celle_status = celle.erLevende()         ##henter inn statusen til celle
                levende_nabo = []                         ##Oppretter en ny tom liste som tar imot de levende naboenene
                for naboer in nabo:                       ##For å kunne gjøre det tar jeg ut de levende cellene som er i nabo listen og appender de i levende_nabo
                    if naboer.erLevende():
                        levende_nabo.append(naboer)

                if celle_status:                            ##for å kunne følge med på spillets regler sjekker den først om cellen lever
                    if len(levende_nabo) < 2 or len(levende_nabo) > 3:  ##Hvis cellen innholder mindre enn 2 (underpopulasjon ) eller mer enn 3 levende naboer dør den(overpopulasjon )
                            doende.append(celle)                ##Legger til de cellene inn i døende liste

                else:
                     if len(levende_nabo) == 3:             ##Hvis ikke cellen lever men har 3 levende nabo skal den bli lagt til inn i levende liste
                         levende.append(celle)

        for celle in levende:                               ##Endrer statusen til hvert av cellene i levende celler til at de lever
            celle.settLevende()
        for celle in doende:                                 ##Endrer statusen til hvert av cellene i døende celler til at de dør
            celle.settDoed()

        self._generasjon += 1                               ##Øker generasjon for hvergang metoden kjøres


    def finnAntallLevende(self):                           ##Metode som skal oppgi antall levende celler
        levende_celler = 0                                 ##Nullstiller antall levende celler
        for rad in self._rutenett:                           ##irriterer gjennom listen og går ett hakk dypere for å finne cellene
            for celle in rad:
                if celle.erLevende() == True:                ##Hvis cellene lever(True) skal antalllevende celler økes
                    levende_celler += 1

        return print("\nGenerasjon:",self._generasjon, "- Antall levende celler:",levende_celler)       ## returner verdien til genrasjon og antall levende celler

    def _generer(self):                                     ##Generer eller randomise cellene
        import random

        for i in self._rutenett:                             ##irriterer gjennom listen for å finne cellene
            for j in i:
                if random.randint(0,2) == 0:                 ##og hvor hvert av cellene skal det 1/3 sjanse for å leve(eller spawne på brettet:)
                    j.settLevende()                          ##Setter dem til status levende


    def finnNabo(self, rad, kolonne):                        ## Metode som skal finne nabo og ta imot rad og kolonne som argumenter
         nabo=[]                                             ## opretter en tom liste som skal fylles ut av naboen til hvert av cellene

         for i in range(-1,2):                              ##Starter først ved cellene øverst til venstre ved å oppgi posisjonen
             for j in range(-1,2):
                 nabo_Rad= rad + i                           ##naborad som skal være den cellen pluss verdien til i
                 nabo_Kolonne= kolonne + j

                 gyldig = True                              ##Varibel som setter status om naboene er gyldig til True

                 if nabo_Rad == rad and (nabo_Kolonne) == kolonne:     ##sjekker om naboen til cellen(0) er cellen(0) i seg selv --> samme med kolonner
                     gyldig = False                             ##Setter statusen til False

                 if (nabo_Rad) < 0 or (nabo_Rad) >= self._rader:  ##Sjekker om naboraden er mindre enn 0 eller større eller lik anntal rader brukeren oppgir
                     gyldig = False

                 if (nabo_Kolonne) < 0 or (nabo_Kolonne) >= self._kolonner: ##Sjekker om nabokolonnen er mindre enn 0 eller større eller lik kolonnen brukeren oppgir
                     gyldig = False

                 if gyldig == True:                             ##Hvis statusen til naboene til cellene er godkjent legges de i spillbretten
                      nabo.append(self._rutenett[nabo_Rad][nabo_Kolonne])


         return nabo ##returnerer nabolisten
