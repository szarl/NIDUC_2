
import randomData
import bitOperations
import multiplicativeScrambler

def multDescramb( InBytes, eqVect, initState ) :
    inBits = bitOperations.bytes2Bits(InBytes)
    bitLen = len(inBits)
    tmpState = initState[:]
    outBits = [0]*bitLen
    for j in range(bitLen) :
        tmpBit = (sum([v1*v2 for v1,v2 in zip(tmpState,eqVect)])%2)
        outBits[j] = inBits[j]^tmpBit
        tmpState[1:] = tmpState[:-1]
        tmpState[0] = inBits[j]
    return bitOperations.bits2Bytes(outBits)


if __name__ == '__main__':
    inp = randomData.randomBytes(16);
    scr = multiplicativeScrambler.multScramb(inp,multiplicativeScrambler.vecMultAdd,multiplicativeScrambler.multScrmblrInitV)
    out = multDescramb(scr,multiplicativeScrambler.vecMultAdd,multiplicativeScrambler.multScrmblrInitV)
    out2 = multDescramb(scr,multiplicativeScrambler.vecMultAdd,[0]*17)
    print("Dane:               ",inp,'\n')
    print("scrambled:          ",scr,'\n')
    print("synchronised output:",out,'\n')
    print("desynchronised:     ",out2,'\n')#tylko 2 pierwsze bajty(17 bitow) sie zle przesylaja
