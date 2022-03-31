import bitoper
import losoweDane

def AddNoiseToData(Data):
    bity = bitoper.BajtDoBitow(Data)
    length = len(bity)
    Noise = losoweDane.losoweBity(length,999)#0.1% zaklucenia
    for i in range(length):
        bity[i] = (bity[i]+Noise[i])%2
    return bitoper.BityDoBajtow(bity);