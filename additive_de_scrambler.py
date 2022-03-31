
import losoweDane
import bitoper

addvectLadd = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
poczotkowaWartoscDVB = [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0]

def AddScramb( Dane, AddVect, InitState ) :
    Bity = bitoper.BajtDoBitow(Dane)
    BitLen = len(Bity)
    TmpState = InitState[:]
    OutBits = [0]*BitLen
    for j in range(BitLen) :
        Tmp = (sum([v1*v2 for v1,v2 in zip(TmpState,AddVect)])%2)
        OutBits[j] = Bity[j]^Tmp
        TmpState[1:] = TmpState[:-1]
        TmpState[0] = Tmp
    return bitoper.BityDoBajtow(OutBits);


if __name__ == '__main__':
    inp = losoweDane.losoweBajty(24);
    scr = AddScramb(inp,addvectLadd,poczotkowaWartoscDVB)
    out = AddScramb(scr,addvectLadd,poczotkowaWartoscDVB)
    print(inp,'\n')
    print(scr,'\n')
    print(out,'\n')
