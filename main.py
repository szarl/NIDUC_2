import losoweDane
import additive_de_scrambler
import bitynadlugosc
import bitoper



if __name__ == '__main__':
    Dane = losoweDane.losoweBajty(16)
    dlugosciniezmienneDane = bitynadlugosc.DaneDoDlugosci(Dane)

    scrambled = additive_de_scrambler.AddScramb(Dane,additive_de_scrambler.addvectLadd,additive_de_scrambler.poczotkowaWartoscDVB)
    dnzscrambled = bitynadlugosc.DaneDoDlugosci(scrambled)

    unscrambled = additive_de_scrambler.AddScramb(scrambled,additive_de_scrambler.addvectLadd,additive_de_scrambler.poczotkowaWartoscDVB)
    dnzunscrambled = bitynadlugosc.DaneDoDlugosci(unscrambled)

    print("maksymalna dlugosc dla niezmieniajacych sie bitow")
    print("w danych wpelni losowych:",max(dlugosciniezmienneDane))
    print("w scramblowanych danych: ",max(dnzscrambled))
    print("w odzyskanych danych:    ",max(dnzunscrambled))

    print(Dane)
    print(scrambled)
    print(unscrambled)
    print()
    
    Dane = bitoper.BityDoBajtow(losoweDane.losoweBity(16*8,9))
    dlugosciniezmienneDane = bitynadlugosc.DaneDoDlugosci(Dane)

    scrambled = additive_de_scrambler.AddScramb(Dane,additive_de_scrambler.addvectLadd,additive_de_scrambler.poczotkowaWartoscDVB)
    dnzscrambled = bitynadlugosc.DaneDoDlugosci(scrambled)

    unscrambled = additive_de_scrambler.AddScramb(scrambled,additive_de_scrambler.addvectLadd,additive_de_scrambler.poczotkowaWartoscDVB)
    dnzunscrambled = bitynadlugosc.DaneDoDlugosci(unscrambled)
    
    print("maksymalna dlugosc dla niezmieniajacych sie bitow")
    print("w danych z wieksza iloscia zer:",max(dlugosciniezmienneDane))
    print("w scramblowanych danych:       ",max(dnzscrambled))
    print("w odzyskanych danych:          ",max(dnzunscrambled))

    print(Dane)
    print(scrambled)
    print(unscrambled)
