import randomData

def bits2Bytes( inBits ):
    """Converts bits to bytes"""
    inLen = len(inBits)
    outBytes = [0]*(inLen>>3)
    for j in range(inLen) :
        if inBits[j] :
            outBytes[j>>3] |= (1<<(j%8))
    return outBytes


def bytes2Bits( inBytes ):
    """Converts bytes to bits"""
    outLen = len(inBytes)<<3
    outBits = [0]*outLen
    for j in range(outLen) :
        if (inBytes[j>>3] >>(j%8))%2 :
            outBits[j] = 1
    return outBits


def testBitConv():
    inp = randomData.randomBytes(16)
    out = bits2Bytes(bytes2Bits(inp))
    assert(inp == out)
    print("wejscie:",inp)
    print("wyjscie:",out)
    inp = randomData.randomBits(24)
    out = bytes2Bits(bits2Bytes(inp))
    assert(inp == out)
    print("wejscie:",inp)
    print("wyjscie:",out)
    return

if __name__ == '__main__':
    testBitConv()