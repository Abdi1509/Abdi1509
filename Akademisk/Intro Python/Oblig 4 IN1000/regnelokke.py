'''oppgave 2'''


tall=int(input("Skriv inn et tall: "))##Brukeren oppgir ett tall
liste=[] ##putter alt det brukeren oppgir(utenom 0) i listen


while tall!=0:   ##while loopen kjører funksjonen flere ganger så lenge brukeren skriver alt utnom 0
    liste.append(tall)          ##putter alle tallene i liste
    tall=int(input("Feil, skriv igjen:"))  ##skriver ut en feilmelding til brukeren

if tall==0:                             ##if testen kjører hvis brukeren oppgir 0
    i=0
    print("Her er tallene du skrev som forsøk: ")
    for i in liste:                             ##Printer ut alt det brukeren har oppgitt i listen
        print(i)

    for i in range(1):         ##for listen kjører og regner ut summen av det brukeren har skrevet inn
        print("summen av listen din er: ")
        minSum=sum(liste)    ##summen av verdiene i listen
        print(minSum)

    for tall in range(1):       ##printer ut minste verdien brukeren har oppgitt
        print("Minste tallet er: ", min(liste))

    for tall in range(1):       ##printer ut størte verdien brukeren har oppgitt
        print("Største tallet er: ",max(liste))
