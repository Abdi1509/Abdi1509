'''Oppgave 2:temperatur'''


def fil(filnavn): ## starter p lage en prosedyre som tar imot fil som argument
    fil=open(filnavn)  ##åpner filen
    ordbok={}               ##ny tom liste
    for x in fil:           ##for løkke som irriterer gjennom hver linje
        bytte=x.strip("")      ##kopierer hver linje i en stringform
        linje=bytte.split(",")  ##Splitter alt som innholder komma
        maaned=linje[0]               ##oppgir hvilke posisjon variabelen "maaned" har
        ordbok[maaned]=float(linje[1])          ##angir temperaturene som innholdsverdi til nøkkelverdien "maaned"

    fil.close()                                 ##lukker filen
    return ordbok                               ##returnerer ordboken

print(fil("max_temperatures_per_month.csv"))          ##funksjonen "fil" kalles med fil som argument


def max_temperatur(ordbok,filnavn):               ##definerer en prosedyre med orboken og filnavn som argument
    fil=open(filnavn)
    for x in fil:
        bytte=x.strip()                          ##har det samme strukturen som tildigere prosdeyren med å splitte og stripe men med forskjellig variabel
        info=bytte.split(",")
        maaned=info[0]
        dato=info[1]
        temperatur=float(info[2])


        if temperatur > ordbok[maaned]:            ##if test som sjekker om temperaturen pr dag er høyere enn høyeste temperaturen pr måned
            print("Ny varmerekord! Datoen er : ", maaned, dato,"og har nye temperaturen på: " ,temperatur,"grader.")
            print("Den gamle rekordvarmen var: ", ordbok[maaned],"grader")
            ordbok[maaned]=temperatur
    fil.close()  ##filen lukkes

    return(ordbok)  ##nye oppdaterte orboken returneres
oppdater=max_temperatur(fil("max_temperatures_per_month.csv"),"max_daily_temperature_2018.csv")    ##ny variabel som innholder den nye oppdaterte ordboken



print(max_temperatur(fil("max_temperatures_per_month.csv"),"max_daily_temperature_2018.csv"))    ##prosedyren "max_temperatur" kalles


def maxtemp(ordbok,fil2):                ##definerer ny prosedyre med nye opppdaterte orboken og en ny fil som argument
    fil2=open(fil2,"w")             ##åpner den nye filen og gir muligheten til å skrive i den
    for i in ordbok:                          ##irriterer gjennom hver temperatur i den nye ordboken
        fil2.write(f"{i},{ordbok[i]}\n")       ##oppdaterer nye filen med den gamle ordboken og skriver om de nye temperaturene
    fil2.close()
    print(fil2)

maxtemp(oppdater,"oppdatert_max_temperatures_per_month.csv")      ##kalles på funksjonen "maxtemp"
