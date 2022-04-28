import random

def randomBytes(length):
    """Returns array of random bytes"""
    out= [0]*length
    for i in range(length):
        out[i] = random.sample(range(256), counts=[1]*256,k=1)[0]
    return out


def randomBits(length,zeroes=1):
    """
    Returns array of random bits
    length (int): number of generated bits
    zeros (int): ratio of zeroes to ones"""
    out= [0]*length
    for i in range(length):
        out[i] = random.sample([0, 1], counts=[zeroes, 1],k=1)[0]
    return out

if __name__ == '__main__':
    print(randomBytes(24))
    print(randomBits(24))
    print(randomBits(24,9))