steder=[]
klesplagg=[]
avreisedatoer=[]
reiseplan=[steder,klesplagg,avreisedatoer]

for i in range(0,5):
    land=input(str("Vennligst skriv inn 5 reisemåler: "))
    steder.append(land)
    i=i+1

for i in range(0,5):
    plagg=input(str("Vennligst skriv inn 5 klesplagg: "))
    klesplagg.append(plagg)
    i=i+1

for i in range(0,5):
    dato=input(str("Vennligst skriv inn 5 datoer: "))
    avreisedatoer.append(dato)
    i=i+1

for elements in reiseplan:
    print(reiseplan)


forste=int(input("skriv inn et input(i1): "))
if forste<len(reiseplan):
    print(reiseplan[forste])
else:
    print("ugyldig inputt")

andre=int(input("skriv inn et input(i2): "))
forsteReiseplan=reiseplan[forste]
if andre<len(reiseplan[forste]):
    print(forsteReiseplan[andre])
else:
    print("ugyldig tall!")

steder=[]
klesplagg=[]
avreisedatoer=[]
reiseplan=[steder,klesplagg,avreisedatoer]
for i in range(0,5):
    land=input(str("Vennligst skriv inn 5 reisemåler: "))
    steder.append(land)
    i=i+1
for i in range(0,5):
    plagg=input(str("Vennligst skriv inn 5 klesplagg: "))
    klesplagg.append(plagg)
    i=i+1
for i in range(0,5):
    dato=input(str("Vennligst skriv inn 5 datoer: "))
    avreisedatoer.append(dato)
    i=i+1
for elements in reiseplan:
    print(reiseplan)

forste=int(input("skriv inn et input(i1): "))
if forste<len(reiseplan):
    print(reiseplan[forste])
else:
    print("ugyldig inputt")
andre=int(input("skriv inn et input(i2): "))
forsteReiseplan=reiseplan[forste]
if andre<len(reiseplan[forste]):
    print(forsteReiseplan[andre])
else:
    print("ugyldig tall!")


'''Note! Evt har jeg tenkt å gjøre koden litt kortere med å:
#for i in range(0,5):
#    print("Planleggin Nr: ",verdi)
#    land=input(str("Vennligst skriv inn reisemål: "))
#    steder.append(land)
#    klesplagg.append(plagg)
#    dato=input(str("Vennligst skriv inn dato: "))
#    avreisedatoer.append(dato)
#    i=i+1
#    verdi=verdi+1


#for elements in range(1):
#    print(reiseplan)
skriver inn alle for løkkene til et. men krevde mye forandringer som krevde ekstra tid som jeg ikke hadde'''
