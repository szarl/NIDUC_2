import randomData
import addScrambler
import bitsLength
import bitOperations



if __name__ == '__main__':
    dane = randomData.randomBytes(16)
    dlugosciniezmiennedane = bitsLength.bitsLength(dane)

    scrambled = addScrambler.addScramb(dane,addScrambler.addvectorDVB,addScrambler.initialValueDVB)
    dnzscrambled = bitsLength.bitsLength(scrambled)

    unscrambled = addScrambler.addScramb(scrambled,addScrambler.addvectorDVB,addScrambler.initialValueDVB)
    dnzunscrambled = bitsLength.bitsLength(unscrambled)

    print("maksymalna dlugosc dla niezmieniajacych sie bitow")
    print("w danych wpelni losowych:",max(dlugosciniezmiennedane))
    print("w scramblowanych danych: ",max(dnzscrambled))
    print("w odzyskanych danych:    ",max(dnzunscrambled))

    print(dane)
    print(scrambled)
    print(unscrambled)
    print()
    
    dane = bitOperations.bits2Bytes(randomData.randomBits(16*8,9))
    dlugosciniezmiennedane = bitsLength.bitsLength(dane)

    scrambled = addScrambler.addScramb(dane,addScrambler.addvectorDVB,addScrambler.initialValueDVB)
    dnzscrambled = bitsLength.bitsLength(scrambled)

    unscrambled = addScrambler.addScramb(scrambled,addScrambler.addvectorDVB,addScrambler.initialValueDVB)
    dnzunscrambled = bitsLength.bitsLength(unscrambled)
    
    print("maksymalna dlugosc dla niezmieniajacych sie bitow")
    print("w danych z wieksza iloscia zer:",max(dlugosciniezmiennedane))
    print("w scramblowanych danych:       ",max(dnzscrambled))
    print("w odzyskanych danych:          ",max(dnzunscrambled))

    print(dane)
    print(scrambled)
    print(unscrambled)
