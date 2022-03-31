import losoweDane

def BityDoBajtow( InBits ) :
    InLen = len(InBits)
    OutLen = InLen>>3
    OutBytes = [0]*OutLen
    for j in range(InLen) :
        if InBits[j] :
            ByteIdx = j>>3
            BitIdx = j%8
            OutBytes[ByteIdx] |= (1<<BitIdx)
    return OutBytes



def BajtDoBitow( InBytes ) :
    InLen = len(InBytes)
    OutLen = InLen<<3
    OutBits = [0]*OutLen
    for j in range(OutLen) :
        ByteIdx = j>>3
        BitIdx = j%8
        if (InBytes[ByteIdx] >>BitIdx)%2 :
            OutBits[j] = 1
    return OutBits


def testBitConv():
    inp = losoweDane.losoweBajty(16)
    out = BityDoBajtow(BajtDoBitow(inp))
    print(inp,'\n',out,'\n')
    inp = losoweDane.losoweBity(16)
    out = BajtDoBitow(BityDoBajtow(inp))
    print(inp,'\n',out,'\n')
    return



if __name__ == '__main__':
    testBitConv()