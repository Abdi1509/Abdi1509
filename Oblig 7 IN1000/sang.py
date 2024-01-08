'''Opggave 1:Klassen sang'''


class Sang:                 ##Klasse Sang opprettes
    def __init__(self,artist,tittel):    ##kontruktør som innholder parametere som tar imot navnet på artisten og tittelen
        self._artist=artist
        self._tittel=tittel



    def spill(self):
        print("Nå spilles det av:", self._tittel ,"av",self._artist)  ##Metode som spiller av den spesifikke sangen den blir bedt om å spilles og med artisten

    def sjekkArtist(self,navn):  ## Metode som sjekker om artisten stemmer ved å sammenligne artistnavnet og et navn som blir sendt fra objektet
        splitter=navn.lower().split()  ##Splitter opp navnet først og setter alle bokstavene i små bokstav
        for ord in splitter:           ##Går gjennom hver ord i navnet
            if ord in self._artist.lower().split():  ##Sammenligner navnet som er sendt fra objektet med navnet som er i self._artist ved å også splitte den og lowere
                return True    ##Returnere True hvis den stemmer
        return False ##Hvis ikke False

    def sjekkTittel(self,tittel):    ##Metode som sjekker om tittelen stemmer ved å hente inn tittel som argument
         myTittel=tittel.lower()   ##Kun lowerer bokstavene og ikke splitter
         if myTittel == self._tittel.lower():  ## Sammenligner
             return True    ##Hvis sant returner den True
         return False  ##Hvis ikke False

    def sjekkArtistOgTittel(self,artist,tittel):  #Metode som sjekker om tittelen og artistnavnet stemmer med instansvariabelene
        return self.sjekkArtist(artist) and self.sjekkTittel(tittel) ##Sjekker om artist og Tittelen er True, hvis en av dem ikke er det eller begge ikke er returner den false
