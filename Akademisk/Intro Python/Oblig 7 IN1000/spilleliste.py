from sang import Sang                       ##imposterer klassen sang fra filen Sang.py

class Spilleliste:                          ##lager en ny klasse
    def __init__(self, listenavn):          ##kontruktør med parameter som skal introdusere hele musikkbiblioteket
        self._sanger = []                   ##Tom liste som oprettes
        self._navn = listenavn

    def lesFraFil(self,filnavn):            ##Metode som leser inn filen og gjør ulike operatører på den
        fil=open(filnavn)                   ##åpner filen
        for linje in fil:                   ##Leser filen for hver linje
            data=linje.strip().split(";")    ##Splitter opp linjen for hver ";"
            self._sanger.append(Sang(data[1],data[0]))   ##Posisjonerer artist på rad[1] og tittelen på rad[0]
        fil.close()

    def leggTilSang(self,nySang):   ##Metode som legger til nye sanger i listen
        self._sanger.append(nySang)


    def fjernSang(self,sang):   ##Metode som sletter sang fr1a listen
        self._sanger.remove(sang)


    def spillSang(self,sang):  ##Metode som spiller en spesifikt sang den blir bedt om å spille (Kjøres gjennom klassen sang)
        sang.spill()


    def spillAlle(self):    ##Metode som spiller alle sangene som eksisterer i listen for hver linje
        for sang in self._sanger:
            sang.spill()


    def finnSang(self,tittel):      ##Metode som finner sangen i listen
        for i in self._sanger:    ##For hver linje sjekekr den om sangen eksisterer
            if i.sjekkTittel(tittel)==True:   ##Hvis den matcher vil den returnere innholdet til rekken der deb har funnet sangen
                return i                    ##og returnere det
        return None  ##Hvis ikke sangen er funnet returnerer den NONE


    def hentArtistUtvalg(self,artistnavn):          ## Metode som oppretter en ny tom liste og sjekker om en sang har en eller flere navn på artisten og tar vare på den
        liste=[]
        for sanger in self._sanger:                 ## Går gjennom hver sang i listen
            if sanger.sjekkArtist(artistnavn)==True:        ##Hvis den finner finner artistnavnet i filen som er sent inn så vil den legge til sangen i den nye listen
                liste.append(sanger)
        return liste  ##Returnerer nye listen
