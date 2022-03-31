
import losoweDane
import bitoper
import multiplicativeScrambler

def MultDescramb( InBytes, ConVect, InitState ) :
    InBits = bitoper.BajtDoBitow(InBytes)
    BitLen = len(InBits)
    RegState = InitState[:]
    OutBits = [0]*BitLen
    for j in range(BitLen) :
        RegBit = (sum([v1*v2 for v1,v2 in zip(RegState,ConVect)])%2)
        OutBits[j] = InBits[j]^RegBit
        RegState[1:] = RegState[:-1]
        RegState[0] = InBits[j]
    return bitoper.BityDoBajtow(OutBits)


if __name__ == '__main__':
    inp = losoweDane.losoweBajty(16);
    scr = multiplicativeScrambler.MultScramb(inp,multiplicativeScrambler.vecMultAdd,multiplicativeScrambler.MultScrmblrInitV)
    out = MultDescramb(scr,multiplicativeScrambler.vecMultAdd,multiplicativeScrambler.MultScrmblrInitV)
    out2 = MultDescramb(scr,multiplicativeScrambler.vecMultAdd,[0]*17)
    print("Dane:               ",inp,'\n')
    print("scrambled:          ",scr,'\n')
    print("synchronised output:",out,'\n')
    print("desynchronised:     ",out2,'\n')#tylko 2 pierwsze bajty(17 bitow) sie zle przesylaja
