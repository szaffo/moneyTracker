from classes import fileiohandler

class File:
	def __init__(self,path):
		self.io = fileiohandler.FileIOHandler(path)
		self.io.openToRead()
		self.data = self.io.read()
		self.header = self.data.split('\n').pop(0).split(',')
		self.data = [x.split(",") for x in self.data.split("\n")]
		while [] in self.data:
			self.data.remove([])

	def headerToString(self):
		return ','.join(self.header)

	def dataToString(self):
		return '\n'.join([','.join(x) for x in self.data])

	def close(self):
		self.io.openToRead()
		self.io.write(self.headerToString()+'\n')
		self.io.write(self.dataToString())
		self.io.close()

	def listColumns(self):
		return ", ".join(self.header)

	def addColumn(self, name, defValue):
		if (name in self.header) or (name == ''):
			return False

		self.header.append(name)

		if defValue == '':
			defValue = '-'
		for record in self.data:
			record.append(defValue)

		return True

	def removeColumn(self,name):
		try:
			num = self.header.index(name)
		except:
			return False
		self.header.pop(num)
		for record in self.data:
			#record.pop(num)
			pass
		return True

if __name__=="__main__":
	f = File("../data/test.csv")
	f.close()
