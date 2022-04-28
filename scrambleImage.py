from matplotlib import image
from addScrambler import addScramb as scrambler
import cv2
import numpy as np

def scrambleImage(img, scrambler):
    shp = img.shape
    img.resize(img.size)
    img = scrambler(img)
    img = np.asarray(img)
    img = np.uint8(img)
    img.resize(shp)
    return img

if __name__ == '__main__':
    img = cv2.imread('res/cat.jpg')
    shp = img.shape
    cv2.imshow("before", img)

    print('Starting to scramble image')
    scrambled = scrambleImage(img, scrambler)
    print('Image scrambled')
    cv2.imshow("scrambled", scrambled)
     

    print('Starting to descramble image')
    descrambled = scrambleImage(scrambled, scrambler)
    print('Image descrambled')
    cv2.imshow("descrambled", descrambled)
    cv2.waitKey()
    cv2.destroyAllWindows()
