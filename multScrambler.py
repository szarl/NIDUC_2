import randomData
import bitOperations

vecMultAdd = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1]
multScrmblrInitV = [0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0]

def multScramb( bytes, eqVect=vecMultAdd, initState=multScrmblrInitV ):
    """
    Scrambles data

    bytes (list): array of bytes (input)
    initialState (list): pseudo-random bit sequence
    addVectorEquation (list): control word

    returns a list of scrambled bytes
    """
    inBits = bitOperations.bytes2Bits(bytes)
    bitLen = len(inBits)
    tmpState = initState[:]
    outBits = [0]*bitLen
    for j in range(bitLen) :
        outBits[j] = inBits[j]^ (sum([v1*v2 for v1,v2 in zip(tmpState,eqVect)])%2)
        tmpState[1:] = tmpState[:-1]
        tmpState[0] = outBits[j]
    return bitOperations.bits2Bytes(outBits)

def multDescramb( InBytes, eqVect = vecMultAdd, initState = [0]*17):
    """
    Descrambles data

    bytes (list): array of bytes (input)
    initialState (list): pseudo-random bit sequence
    addVectorEquation (list): control word

    returns a list of descrambled bytes

    """
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

def testMultScr():
    inp = randomData.randomBytes(16)
    scr = multScramb(inp,vecMultAdd,multScrmblrInitV)
    out = multDescramb(scr,vecMultAdd,multScrmblrInitV)
    out2 = multDescramb(scr,vecMultAdd,[0]*17)
    print("Dane:               ",inp)
    print("Scrambled:          ",scr)
    print("Synchronised output:",out)
    print("Desynchronised:     ",out2)  # tylko 2 pierwsze bajty(17 bitow) sie zle przesylaja


if __name__ == '__main__':
    testMultScr()