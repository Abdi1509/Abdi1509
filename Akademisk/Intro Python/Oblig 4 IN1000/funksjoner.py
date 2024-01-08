'''oppgave 1'''
'''NOTE!:skønte ikke helt oppgave 1c men har laget begge funksjonene. som jeg tolker oppgave 1c er at jeg skal skrive om funksjonen antall og omgjøre det til samme funksjon som tellforekomst.
        # men jeg kommenterte ut 1b(og den funker) og lot 1c funksjonen stå'''




def adder(tall1,tall2): ##funksjon summerer sammen to tall og har får det vie parametere
    sum=tall1 + tall2
    print(sum)


adder(8,4) ##parameterene som funksjonen skal brukes som variabel verdi

'''1b'''
#ord=[] ##lager en tom liste som brukeren setter in en tekststreng
#streng=input("Hei, vennligst skriv en tekst: ")
#ord.append(streng)
#bokstav=input("Vennligst velg bokstav: ")         ##brukeren oppgir bokstaven han/hun er ute etter

#def antall(streng,bokstav):           ##funksjonen sjekker hvor mange ganger bokstaven er i teksten ved hjelp av parametere
#    antall=0
#    for letter in streng:
#        if letter ==bokstav:
#           antall=antall+ 1
#    print(antall)

#antall(streng,bokstav)                ##funksjonen kjøres med verdier fra brukeren


'''1c'''

minTekst=input("Hei, vennligst skriv en setning: ")
minBokstav=input("Vennligst velg bokstav: ")


ordbok={}  ##Lager en tom ordbok som brukeren oppgir et tekst og bokstav
def tellForekomst(minTekst,minBokstav):
    antall=0
    for letter in minTekst:
        if letter ==minBokstav:
            antall=antall+1
    print("Det er ",antall, minBokstav,"/er", "bokstaver i setningen")
    return(minTekst,minBokstav)

tellForekomst(minTekst,minBokstav)
