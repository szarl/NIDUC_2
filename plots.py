import addScrambler
import multScrambler
import bitOperations
import bitsLength as bitLen
import randomData as rand
import matplotlib.pyplot as plt
import csv
import os

LEN_OF_DATA = 10000*8

def showPlot(data):
    length = bitLen.bitsLength(data)
    plt.ion()
    plt.hist(length, bins=10)
    plt.show()
   
def save(name, data):
    name = 'results/' + name.replace(' ', '_')
    f = open(name+'.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(data)
    f.close()

def plotData(name, data):
    plt.figure(name)
    plt.title(name)
    plt.xlabel('liczba niezmieniajacych sie bitow')
    plt.ylabel('liczba bitow')
    showPlot(data)
    save(name,data)
    filename = 'plots/'+name.replace(' ', '_')+'.png'
    plt.savefig(filename)

def testData(data):
    zeroesPerc = data.count(0) / len(data)
    message = ' (All to '+ str(zeroesPerc) + '% wszystkich bitow)'
    dataBytes = bitOperations.bits2Bytes(data)

    plotData('Losowe dane ' + message, data)

    scrambledAdd = addScrambler.addScramb(dataBytes)
    plotData('Zescramblowane - additive '+message, scrambledAdd)

    scrambledMult = multScrambler.multScramb(dataBytes)
    plotData('Zescramblowane - multiplicative '+message, scrambledMult)

def makeDir(name):
    folderPath = os.getcwd()+'\\'+name
    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

if __name__ == "__main__":
    makeDir('results')
    makeDir('plots')

    randData = rand.randomBits(LEN_OF_DATA)
    testData(randData)

    randDataZeroes = rand.randomBits(LEN_OF_DATA,999)
    testData(randDataZeroes)

    randDataOnes = rand.randomBits(LEN_OF_DATA,999)
    for i in range(LEN_OF_DATA):
        randDataOnes[i] = (randDataOnes[i]+1)%2
    testData(randDataOnes)

    zeroes = [0]*LEN_OF_DATA
    testData(zeroes)

    ones = [1]*LEN_OF_DATA
    testData(ones)

    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
    plt.waitforbuttonpress()
