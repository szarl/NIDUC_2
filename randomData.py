import random

def randomBytes(length):
    out= [0]*length
    for i in range(length):
        out[i] = random.sample(range(256), counts=[1]*256,k=1)[0]
    return out


def randomBits(length,moreZero=1):
    out= [0]*length
    for i in range(length):
        out[i] = random.sample([0, 1], counts=[moreZero, 1],k=1)[0]
    return out

if __name__ == '__main__':
    print(randomBytes(24));
    print(randomBits(24));
    print(randomBits(24,9));#90% to zera