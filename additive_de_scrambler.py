
import randomData
import bitOperations

addvectorDVB = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
poczotkowaWartoscDVB = [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0]

def addScramb( data, addVectorEquation, initialState ) :
    bits = bitOperations.bytes2Bits(data)
    bitLen = len(bits)
    tmpState = initialState[:]
    outbits = [0]*bitLen
    for j in range(bitLen) :
        tmp = (sum([v1*v2 for v1,v2 in zip(tmpState,addVectorEquation)])%2)
        outbits[j] = bits[j]^tmp
        tmpState[1:] = tmpState[:-1]
        tmpState[0] = tmp
    return bitOperations.bits2Bytes(outbits);


if __name__ == '__main__':
    inp = randomData.randomBytes(24);
    scr = addScramb(inp,addvectorDVB,poczotkowaWartoscDVB)
    out = addScramb(scr,addvectorDVB,poczotkowaWartoscDVB)
    print(inp,'\n')
    print(scr,'\n')
    print(out,'\n')
