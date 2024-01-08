'''Oppgave 1 regenfunksjoner'''

def addisjon(tall1,tall2):            ##funksjon for addisjon
    return(tall1 + tall2)

def subtraksjon(tall1,tall2):  ##funksjon for subtraksjon
    return(tall2-tall1)

def divisjon(tall1,tall2):      ##funksjon for deling
    return (tall1/tall2)

def tommerTilCm(antallTommer):        ##funksjoner som omgjøre cm til antall tommer
    assert (antallTommer>0),"større enn 0"
    return (antallTommer*2.54)

def skrivBeregninger():             ##funksjonen gir mulighetentil å skrie inn tall og regne det ut ved å kalle inn funksjonene
    tall1=float(input("skriv inn første tallet: "))
    tall2=float(input("skriv inn andre tallet: "))
    addisjon(tall1,tall2)
    subtraksjon(tall1,tall2)
    divisjon(tall1,tall2)
    tommer=float(input("Vennligst skriv inn antall tommer: "))


    print("Utregninger: ")
    print("Du skrev inn tall1 som: ", tall1)
    print("Du skrev inn tall2 som: ", tall2)

    print("Resultatet av summeringen: ",addisjon(tall1,tall2))
    print("Resultatet av summeringen: ",subtraksjon(tall1,tall2))
    print("Resultatet av summeringen: ",divisjon(tall1,tall2))

    print("Konvertering fra",tommer, "tommer til Cm: ",tommerTilCm(tommer))

assert addisjon(2,2)==4  ##sjekker om funksjonene stemmer
assert addisjon(25,25)==50

assert subtraksjon(10,-5)==-15
assert subtraksjon(25,-5)==-30

assert divisjon(10,2)==5
assert divisjon(20,10)==2

skrivBeregninger()
