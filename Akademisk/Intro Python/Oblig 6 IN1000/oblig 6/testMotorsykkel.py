
from motorsykkel import Motorsykkel ##henter inn klassen i en annet fin

def hovedprogram(): ##funksjon som opretter nye objekter

    Motorsykkel1=Motorsykkel("toyota",4000,5000)##objekter som gir instavariabelene verdi
    Motorsykkel2=Motorsykkel("Mercedes",56791,400)
    Motorsykkel3=Motorsykkel("BMW",9653,10000)




    Motorsykkel1.skrivUt() ##kjører metoden skrivUt i klassen motorsykkel
    Motorsykkel1.hentKilometerstand()

    Motorsykkel2.skrivUt() ##kjører metoden skrivUt i klassen motorsykkel
    Motorsykkel2.hentKilometerstand()

    Motorsykkel3.skrivUt() ##kjører metoden skrivUt i klassen motorsykkel
    Motorsykkel3.hentKilometerstand()
hovedprogram()
