def deseneaza_tabla(spatii):

    tabla=(f"|{spatii[1]}|{spatii[2]}|{spatii[3]}|\n"
           f"|{spatii[4]}|{spatii[5]}|{spatii[6]}|\n"
           f"|{spatii[7]}|{spatii[8]}|{spatii[9]}|\n")

    print(tabla)

def verifTura(tura):
    if tura % 2 == 0 : return 'O'
    else: return 'X'

def verificareWin(spatii):
    #castig pe linie
    if (spatii[1]==spatii[2]==spatii[3]) \
        or (spatii[4]==spatii[5]==spatii[6]) \
        or (spatii[7]==spatii[8]==spatii[9]):
        return True
    #castig pe coloana
    elif (spatii[1]==spatii[4]==spatii[7]) \
        or (spatii[2]==spatii[5]==spatii[8]) \
        or (spatii[3]==spatii[6]==spatii[9]):
        return True
    #castig pe diagonala
    elif (spatii[1]==spatii[5]==spatii[9]) \
        or (spatii[3]==spatii[5]==spatii[7]):
        return True
    else: return False