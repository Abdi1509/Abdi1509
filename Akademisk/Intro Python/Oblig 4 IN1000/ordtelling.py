'''Oppgave 4: Originalen fra 4.1-4.2'''


def antall(ord):  ##Funksjonen regner ut antall bokstaver i setningen
    poeng=len(ord)
    return(poeng)       ##returnerer verdien tilbake


ord=str(input("vennligst skriv inn et ord: "))  ##brukeren skriver inn kun et ord

poeng=antall(ord)
print("Det er ",poeng, "bokstaver i setningen din")

setning={}          ##tom liste som brukeren oppgir et setning i ordboken
def funksjon(split_ordene):
    for ordene in split_ordene:
        if ordene in setning:      ##sjekker om ordene er først i listen
            setning[ordene]+=1    ##legger til en tall for antall gang den er i listen
        else:
            setning[ordene]=1

    for split_ordene in setning:  ##for løkken skriver ut et svar for hvert ord som er i listen(utenom hvis de er skrevet flere ganger)
        print("ordet", split_ordene,"har forekommet",setning[split_ordene])




ordene=input("vennligst skriv inn et setning: ")
split_ordene=ordene.split() ##splitter setningen i ord og lagrer det som nøkkelverdier i ordboken


funksjon(split_ordene)##kaller funksjonen med parametere(split_ordene)



'''Skrev et annet versjon der hvor jeg prøvde ut oppgave 4.3 i filen ordtellingto.py'''
