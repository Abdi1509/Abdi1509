'''Oppgave 3: skop'''

def minfunksjon():
    for x in range(2):
        c=2
        print(c)
        c+=1
        b=10
        b+=a
        print(b)
    return(b)

def hovedprogram():
    a=42
    b=0
    print(b)
    b=a
    a=minfunksjon()
    print(b)
    print(a)

hovedprogram()

'''
Først defineres prosedyren "minfunksjon" som ikke har noe parametere som argument. Inni prosedyren er det oppgave den har fått som enda
ikke aktiveres og venter på å bli kalt. Etter det blir det laget et nytt prosedyre "hovedprogram" som heller ikke tar imot noe parametere.
Prosedyren "hovedprogram" blir kalt på slutten og kjøres. Først lages det et variabel "a" so har verdi 42 i seg. Så et nytt variabel "b"
med verdi 0 i seg. Så printes det ut verdien til b som er = 0. Etter printen vil verdien til b endre med å være det samme som verdien til "a"
så a=42 og b=42 nå. variabelen "a" kaller på prosedyren "minfunksjon" og kjøres.

I prosedyren "minfunksjon" så er det en for løkke som kjøres med å begrense "x(eller antall)" med to. Først vil det lages et nytt variabel "c"
med verdien 2 og det printes ut "2". Også vil "c" plusses med 1 og ha verdi på 3. også kommer nye variabelen "b" i prosedyren med verdi 10.
Et problem vil da oppstå siden variabelen b+=a, er ikke a definert i selve funksjonen. Den er kun definert i prosedyren "hovedprogram", og siden
den ikke tar imot parametere og argument vil da verdien til a være none value, og gå tilbake til hovedprogram. Og siden a er none value return fra den
første prosedyren, vil de da ikke printes ut. Og siden b er definert som det samme verdi som a("none value") så vil ikke b heller printes.
Og tilsutt vil det programmet sluttes.




Det jeg trodde skulle skje er at funksjonen vil i "minfunksjon" ville printe ut verdien 0 siden a ikke eksisterer i funksjonen og dermed gi det verdien 0
(men har lært at det er forskjell mellom NULL og null som i 0 )

'''
