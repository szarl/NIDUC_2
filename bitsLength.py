import bitOperations
import randomData

def bitsLength(bytes):
	"""
	Returns list of length of given bytes
	
	bytes (list): list of bytes
	"""
	bits = bitOperations.bytes2Bits(bytes)
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

def testBitsLength():
	inp = randomData.randomBytes(4)
	len1 = bitsLength(inp)
	inp2 = [0,0,255,255,0]
	len2 = bitsLength(inp2)
	bits = bitOperations.bytes2Bits(inp)
	bits2 = bitOperations.bytes2Bits(inp2)
	print("Dane:",bits)
	print("Dlugosci:",len1)
	print("Dane:",bits2)
	print("Dlugosci:",len2)

if __name__ == '__main__':
	testBitsLength()
