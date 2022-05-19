import addScrambler
import multScrambler
import bitOperations
import bitsLength as leng
import randomData as rand
import matplotlib.pyplot as plt
import csv
import cv2

dlugosc = 10000*8

def policzdlg(data):
    dlugosci = leng.bitsLength(data)
    plt.ion()
    plt.hist(dlugosci, bins = 10)   #mi nie dziala wyswietlanie nie wiem czemu
    plt.show()
   
def zapisz(name,data):
    f = open(name, 'w')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

def both(name,data):
    plt.figure(name)
    plt.xlabel('ilosc niezmieniajacych sie bitow')
    policzdlg(data)
    zapisz(name+'.csv',data)

def wykresy():
    losowedane = bitOperations.bits2Bytes(rand.randomBits(dlugosc))
    losowedanescr = addScrambler.addScramb(losowedane)
    losowedanescrmult = multScrambler.multScramb(losowedane)
    
    both('losowedane',losowedane)
    both('losowedane_scrambled',losowedanescr)
    both('losowedane_multscrambled',losowedanescrmult)


    zwiecejzer =  bitOperations.bits2Bytes(rand.randomBits(dlugosc,999))
    zwiecejzerscr = addScrambler.addScramb(zwiecejzer)
    zwiecejzerscrmult = multScrambler.multScramb(zwiecejzer)
    
    both('zwiecejzer_dane',zwiecejzer)
    both('zwiecejzer_scrambled',zwiecejzerscr)
    both('zwiecejzer_multscrambled',zwiecejzerscrmult)


    zwiecejjedt = rand.randomBits(dlugosc,999)
    for i in range(dlugosc):
        zwiecejjedt[i] = (zwiecejjedt[i]+1)%2
    #
    zwiecejjed = bitOperations.bits2Bytes(zwiecejjedt)
    zwiecejjedscr = addScrambler.addScramb(zwiecejjed)
    zwiecejjedscrmult = multScrambler.multScramb(zwiecejjed)
    
    both('zwiecejjed_dane',zwiecejjed)
    both('zwiecejjed_scrambled',zwiecejjedscr)
    both('zwiecejjed_multscrambled',losowedanescrmult)

    
    samezera = bitOperations.bits2Bytes([0]*dlugosc)
    samezerascr = addScrambler.addScramb(samezera)
    samezerascrmult = multScrambler.multScramb(samezera)
    
    both('samezera_dane',samezera)
    both('samezera_scrambled',samezerascr)
    both('samezera_multscrambled',samezerascrmult)
    
    samejeden = bitOperations.bits2Bytes([1]*dlugosc)
    samejedenscr = addScrambler.addScramb(samejeden)
    samejedenscrmult = multScrambler.multScramb(samejeden)
    
    both('samejeden_dane',samejeden)
    both('samejeden_scrambled',samejedenscr)
    both('samejeden_multscrambled',samejedenscrmult)















if __name__ == "__main__":
    wykresy()
    
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()