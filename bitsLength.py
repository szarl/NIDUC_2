import bitOperations
import randomData

def bitsLength(data):
	bits = bitOperations.bytes2Bits(data)
	bitLen=0
	tmpBit = bits[0]
	out = []
	for i in range(len(bits)):
		if tmpBit==bits[i]:
			bitLen+=1
		else:
			out+=[bitLen]
			bitLen=1
			tmpBit = bits[i]
	out+=[bitLen]
	return out


if __name__ == '__main__':
	inp = randomData.randomBytes(4);
	len1 = bitsLength(inp)
	inp2 = [0,0,255,255,0]
	len2 = bitsLength(inp2)
	bits = bitOperations.bytes2Bits(inp)
	bits2 = bitOperations.bytes2Bits(inp2)
	print("Dane:",bits,'\n')
	print("Dlugosci:",len1,'\n')
	print("Dane:",bits2,'\n')
	print("Dlugosci:",len2,'\n')




