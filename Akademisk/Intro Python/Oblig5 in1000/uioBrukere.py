'''Oppgave4'''


ordbok={}       ##lager ny tom liste

def lagBrukernavn(navn,etternavn,suffix_en):               ##definerer en prosedyre som henter inn to argumenter
    navn=navn.lower()                              ##omgjør alle navn inputene til lower
    etternavn=etternavn.lower()
    forsteBokstav=etternavn.split()
    brukernavn=navn + etternavn[0]         ##Legger navnene sammen og kun første bokstaven av etternavnet
    ordbok[brukernavn]=suffix_en            ##lagrer de i listen der hvor innholdsverdien er suffixen brukeren oppgir sammen med brukernavnet

    return(brukernavn)                       ##returner brukernavnet tilbake


def lagEpost(brukernavn):                     ##definerer en funksjon som skal lage epost til brukeren
    epost=brukernavn,"@",suffix
    print("Epost adresset ditt er: ",brukernavn,"@",suffix)

    return(epost,suffix)

def printerEposter(brukernavn):
        suffix="student.matnat.no"
        print(ordbok)
        return(ordbok)
                                            ## NOTE: Forsto ikke oppgaven helt om den skal kalles eller ikke etter å ha fullført oppgae 4.5.
tall=0                                      ##variabel med verdien 0 som skal brukes til while-løkken
while tall==0:                              ##løkken kjøres så lenge verdien til tall er == 0
    svar= str(input("Vennligst skriv inn enten i,p eller s: " ))     ##brukeren oppgir et av de tre bokstavene for å starte oppgave med if tester som sjekker hva brukeren oppgir
    if svar=="i":
        navn=input("Skriv inn navn: ")
        etternavn=input("vennligst oppgi etternavn: ")        ##brukeren får muligheten til å skrive etternavnet pg suffixen deres
        suffix_en=input("Skriv inn suffixen din: ")
        lagBrukernavn(navn,etternavn,suffix_en)
    elif svar=="p":
        printerEposter(ordbok)                              ##funksjonen printerEposter kalles
    elif svar=="s":
        print("programmet avsluttes")
        tall+=1                              ##skriver brukeren inn "s" øker verdien til "tall" og dermed slutter whileløkken med en beskjed om at programmet avsluttes
