
import randomData
import bitOperations

addvectorDVB = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
initialValueDVB = [1,0,0,1,0,1,0,1,0,0,0,0,0,0,0]

def addScramb( bytes, addVectorEquation=addvectorDVB, initialState=initialValueDVB ):
    """
    Scrambles data

    bytes (list): array of bytes (input)
    initialState (list): pseudo-random bit sequence
    addVectorEquation (list): control word

    returns a list of scrambled bytes
    """
    bits = bitOperations.bytes2Bits(bytes)
    bitLen = len(bits)
    tmpState = initialState[:]
    outbits = [0]*bitLen
    for j in range(bitLen):
        tmp = (sum([v1*v2 for v1,v2 in zip(tmpState,addVectorEquation)])%2)
        outbits[j] = bits[j]^tmp
        tmpState[1:] = tmpState[:-1]
        tmpState[0] = tmp
    return bitOperations.bits2Bytes(outbits)

def testAddScr():
    inp = randomData.randomBytes(24)
    scr = addScramb(inp,addvectorDVB,initialValueDVB)
    out = addScramb(scr,addvectorDVB,initialValueDVB)
    print("input:      ", inp)
    print("scrambled:  ", scr)
    print("descrambled:",out)
    assert(inp == out)

if __name__ == '__main__':
    testAddScr()