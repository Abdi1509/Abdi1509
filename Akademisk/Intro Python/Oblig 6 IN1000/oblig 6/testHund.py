from hund import Hund ##importerer klassen Hund

def hovedprogram():   ##funksjon som legger til objekter og verdier som skal brukes i klassen
    Hund1=Hund(3,5)
    Hund1.spring()
    Hund1.spring()
    Hund1.spis(10)
    Hund1.spis(20)


    print(Hund1.skrivUt()) ##skriver ut resultatet



hovedprogram()  ##kjører prgrammet
