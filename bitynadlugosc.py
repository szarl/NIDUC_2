import bitoper
import losoweDane

def DaneDoDlugosci(Data):
	Bity = bitoper.BajtDoBitow(Data)
	dl = len(Bity)
	dlugosc=0
	wart = Bity[0]
	wynik = []
	for i in range(dl):
		if wart==Bity[i]:
			dlugosc+=1
		else:
			wynik+=[dlugosc]
			dlugosc=1
			wart = Bity[i]
	wynik+=[dlugosc]
	return wynik


if __name__ == '__main__':
	inp = losoweDane.losoweBajty(4);
	dlg = DaneDoDlugosci(inp)
	inp2 = [0,0,255,255,0]
	dlg2 = DaneDoDlugosci(inp2)
	bits = bitoper.BajtDoBitow(inp)
	bits2 = bitoper.BajtDoBitow(inp2)
	print("Dane:",bits,'\n')
	print("wyniki:",dlg,'\n')
	print("Dane:",bits2,'\n')
	print("wyniki:",dlg2,'\n')




