ordene=input("vennligst skriv inn et setning: ") ##Brukeren oppgir ett setning
split_ordene=ordene.split()  ##setningen splittes i ord som key

setning={}   ##tom liste som skal innholde ordene i setningen som key

def antall(split_ordene): ##teller antall ord i setningen

        poeng=len(split_ordene)
        return(poeng) ##returnerer verien


##ord=str(input("vennligst skriv inn et ord: "))

poeng=antall(split_ordene)

def funksjon(split_ordene): ##skriver ut antall ganger ordet blir skrevet inn
    for ordene in split_ordene:
        if ordene in setning:
            setning[ordene]+=1
        else:
            setning[ordene]=1
    print("Det er: ", poeng,"bokstav/er i ordet ")
    for split_ordene in setning:
        print("Ordet","'",split_ordene,"'","har forekommet",setning[split_ordene], " gang/er og har" ,poeng,"bokstaver")

antall(split_ordene)
funksjon(split_ordene)


'''Oppgave 4c har jeg streved med ganske lenge (snakk om 4 + timer) der hvor jeg har virkelig prøvd å få til antall ord det er i bokstaven
 jeg vet at på linje 30 står verdien poeng som er antall ord i setningen men har prøvd å lage et annet variabel som skal telle antall ord i bokstaven og det har jeg slitt med
 men dette er ikke noe som skal stopp, leverer inn det her og jobber forsatt med å løse oppgaven selv/evt spørre om hjelp i gruppetimen ila uken'''
