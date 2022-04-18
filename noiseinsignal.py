import bitOperations
import randomData

def addNoiseToData(data,noiseInvLevel=999):#0.1% zaklucenia
    bits = bitOperations.BajtDoBitow(data)
    length = len(bits)
    noise = randomData.randomBits(length,noiseInvLevel)
    for i in range(length):
        bits[i] = (bits[i]+noise[i])%2
    return bitOperations.BityDoBajtow(bits);