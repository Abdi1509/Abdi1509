''' Celle Fil'''

class Celle:   ##Klasse celle blir laget
   # Konstruktør
    def __init__(self):   ##Konstruktøren setter statusen til cellen som False
        self._celle = False         ## False = dø True = levende

    def __str__(self):  ##String Konstruktør som omgjør verdien som returneres fra metoden hentStatusTegn til string
        return(self.hentStatusTegn())  ##returnerer string

    # Endre status
    def settDoed(self):   ##Setter statusen til cellene til False(dø)
         self._celle = False


    def settLevende(self):  ##Setter statusen til cellene til True(levende)
         self._celle = True


    # Hente status
    def erLevende(self):  ##Sjekker status
        if self._celle == True:  ## Hvis cellen lever returnerer den True som verdi
            return True
        return False   ##Hvis ikke cellen lever returnerer den som False

    def hentStatusTegn(self):  ## Metoden returner statusen til cellene på en skriftelig måte "o" for True og "." for False
        if self._celle == True:
            return"O"
        return"."
