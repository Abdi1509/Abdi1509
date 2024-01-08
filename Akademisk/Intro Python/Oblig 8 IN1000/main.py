from spillebrett import Spillebrett  ##Henter inn klassen spillebrett fra filen spillebrett

def main():   ##definerer funksjonen main uten paramterer
  

  svar = input("\nTrykk Enter for å starte programmet, eller q og enter for å stoppe: ")  ##lagrer det brukeren oppgir som svar
  svar = svar.lower()    ##lowerer svare
  teller = 0
  dimensjon1 = int(input("Sett inn første dimensjon for spillebrettet: ")) ##Dimensjon y
  dimensjon2 = int(input("Sett in andre dimensjon for spillebrettet: "))   ##Dimensjon x


  while svar == "" and teller < 1 :  ##Kjører en while-løkke for kun første brett

      Test=Spillebrett(dimensjon1,dimensjon2)
      Test.tegnBrett()
      Test.finnAntallLevende()
      svar2 = input("\nTrykk enter for å forsette, eller q for stoppe: ")
      teller += 1  ##øker verdien til teller sånn at første brettet ikke kjøres omigjen

      while teller > 0 and svar2 == "":  ##om brukeren skal kunne forsette med nye generasjoneer skal oppdatering skje her
          Test.oppdatering()
          Test.tegnBrett()
          Test.finnAntallLevende()
          svar2 = input("\nTrykk enter for å forsette, eller q og enter for stoppe: ")





  if svar == "q" or svar2 == "q":  ##Hvis brukeren oppgir "q" stopper programmet
      print("\nProgrammet har stoppet")

  else:
       print("Ugyldig inntastning")




# starte hovedprogrammet
main()
