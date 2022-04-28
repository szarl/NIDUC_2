import bitOperations
import randomData

def addNoise(bytes, noiseLevel=0.1):
    """
    Adds noise to data
    
    bytes (list): input data
    noiseInvLevel (int): percent of bits changed (as default 0.1%)
    """
    noiseInvLevel = 1000-(int(10*noiseLevel))
    bits = bitOperations.bytes2Bits(bytes)
    length = len(bits)
    noise = randomData.randomBits(length, noiseInvLevel)
    for i in range(length):
        bits[i] = (bits[i]+noise[i])%2
    return bitOperations.bits2Bytes(bits)

def testAddNoise():
    data = randomData.randomBytes(50)
    addedNoise = addNoise(data)
    print(data)
    print(addedNoise)

    diff = 0
    for i in range(len(data)):
        if data[i] != addedNoise[i]:
            diff += 1
            print(f"Difference: data[{i}]={data[i]}, dataWithNoise[{i}]={addedNoise[i]}")
    print("mismatched values: ", diff)


if __name__ == "__main__":
    testAddNoise()
