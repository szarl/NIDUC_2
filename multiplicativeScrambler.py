
import losoweDane
import bitoper


vecMultAdd = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1];
MultScrmblrInitV = [0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0];

def MultScramb( Dane, ConVect, InitState ) :
    InBits = bitoper.BajtDoBitow(Dane)
    BitLen = len(InBits)
    RegState = InitState[:]
    OutBits = [0]*BitLen
    for j in range(BitLen) :
        RegBit = (sum([v1*v2 for v1,v2 in zip(RegState,ConVect)])%2)
        OutBits[j] = InBits[j]^RegBit
        RegState[1:] = RegState[:-1]
        RegState[0] = OutBits[j]
    return bitoper.BityDoBajtow(OutBits)

if __name__ == '__main__':
    print("obsluge plikow mozna dorobic")