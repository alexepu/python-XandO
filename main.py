from helper import deseneaza_tabla,verifTura,verificareWin
import os

spatii={1:'1',2:'2',3:'3',4:'4',
       5:'5',6:'6',7:'7',8:'8',9:'9'}

deseneaza_tabla(spatii)

jucam=True
completat=False
tura=0
tura_trecuta=-1

#Loop cu jocul
while jucam:
       #screen reset
       os.system('cls'if os.name == 'nt' else 'clear')
       #afiseaza cadranul
       deseneaza_tabla(spatii)
       #validare ca datele introduse sunt in parametrii
       if tura_trecuta == tura:
           print("Spatiul introdus nu este valid! Te rog alege altul.")
       tura_trecuta=tura
       print("Randul jucatorului "+str((tura%2)+1)+": Alege spatiul in care sa pui simbolul sau introduce ~q~ pentru a iesi din program.")
       #alegere si validare
       alegere=input()
       #stop joc
       if alegere=='q':
              jucam=False
       elif str.isdigit(alegere) and int(alegere) in spatii:
              #vedem daca spatiul e deja luat
              if not spatii[int(alegere)] in {"x","O"}:
                  #daca nu updatam cadranul
                  tura+=1
                  spatii[int(alegere)]=verifTura(tura)
      #verificare daca avem winner
       if verificareWin(spatii):jucam,completat=False,True
       if tura > 8: jucam=False

os.system('cls'if os.name == 'nt' else 'clear')
deseneaza_tabla(spatii)
if completat:
    if verifTura(tura) == 'X':print("Jucatorul 1 a castigat!")
    else: print("Jucatorul 2 a castigat!")
else:
    print("Niciun castigator")

