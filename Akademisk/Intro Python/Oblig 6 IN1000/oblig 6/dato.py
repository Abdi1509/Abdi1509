'''Oppgave 4:Dato '''

class Dato: ##lager klasse Dato
    def __init__(self,ny_dag,ny_maaned,ny_aar): ##opretter kontruktører
        self.ny_dag=ny_dag   ##definerer kontruktørene
        self.ny_maaned=ny_maaned
        self.ny_aar=ny_aar


    def les_aar(self):  ##metodde som leser av året for datoen
        self.ny_aar=ny_aar
        return(self.ny_aar)

    def streng(self,ny_dag,ny_maaned,ny_aar): ##metode som lager streng av datoen
        self.ny_dag= str(dag)
        self.ny_maaned=srt(ny_maaned)
        self.ny_aar=str(aar)

    def les_dato(self,ny_dag):
        self.ny_dato=ny_dag  ##en metode som sjekker om datoen er en bestemt dag i måneden
        if ny_dag==15:     ##if sjekk som sjekker om dagen er 15
            print("Lønningsdag!")   ##printer ut svar til brukeren
        elif ny_dag==1:     ##sjekker om dagen er 1
            print("Ny måned,nye mulighter") ##printer ut svar til brukeren
        elif ny_dag!=1 and ny_dag!=15:
            print("Ikke no lonningsdag eller start på ny måned :( ")
        return(ny_dag)   ##returnerer datoen tilbake
