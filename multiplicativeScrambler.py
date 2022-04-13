
import bitOperations


vecMultAdd = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1];
multScrmblrInitV = [0,0,1,0,1,1,0,0,0,0,1,1,0,1,0,1,0];

def multScramb( data, eqVect, initState ) :
    inBits = bitOperations.bytes2Bits(data)
    bitLen = len(inBits)
    tmpState = initState[:]
    outBits = [0]*bitLen
    for j in range(bitLen) :
        outBits[j] = inBits[j]^ (sum([v1*v2 for v1,v2 in zip(tmpState,eqVect)])%2)
        tmpState[1:] = tmpState[:-1]
        tmpState[0] = outBits[j]
    return bitOperations.bits2Bytes(outBits)

if __name__ == '__main__':
    print("obsluge plikow mozna dorobic")