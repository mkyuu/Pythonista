class HensatiSansyutu:
	def __init__(self):
		self.goukei_tensuu = []
		self.bunsan =0
		self.dosuu = []
		self.tensuu = [237.5,212,187,162,137,112,87,37]
	
	def Kekka(self,tensuu_mean,honnin_tensuu):
		'''tensuu_mean,syouei_tensuu'''
		self.tensuu_mean = tensuu_mean
		self.honnin_tensuu = honnin_tensuu
		self.goukei_tensuu = [self.tensuu[n] for n in range(len(self.dosuu)) for i in range(self.dosuu[n])]
		#for n in range(len(self.dosuu)):
			#for i in range(self.dosuu[n]):
				#self.goukei_tensuu.append(self.tensuu[n])
		
		
		for i in self.goukei_tensuu:
			b=(i-self.tensuu_mean)**2
			self.bunsan+=b
		self.bunsan = self.bunsan//len(self.goukei_tensuu)
		self.tensuu_std = int(self.bunsan**0.5)
		
		self.hensati = int((self.honnin_tensuu-self.tensuu_mean)/self.tensuu_std * 10 + 50)
		
		return str(self.hensati)

class KamokubetuHS(HensatiSansyutu):
	def __init__(self):
		super().__init__()
		self.tensuu = [45,34.5,24.5,14.5,4.5]

