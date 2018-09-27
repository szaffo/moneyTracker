from classes import fileiohandler

class File:
	def __init__(self,path):
		self.io = fileiohandler.FileIOHandler(path)
		self.io.openToRead()
		self.data = self.io.read()
		self.data = self.data.split('\n')
		while '' in self.data:
			self.data.remove('')
		# print(self.data)
		self.header = self.data.pop(0)
		self.header = self.header.split(',')
		self.data = [x.split(',') for x in self.data]


	def headerToString(self):
		return ','.join(self.header)

	def dataToString(self):
		return '\n'.join([','.join(x) for x in self.data])

	def save(self):
		self.io.openToWrite()
		toPrint = self.headerToString()+'\n'+self.dataToString()+'\n'
		# print(toPrint)
		out = self.io.write(toPrint)
		print("{} bytes was written.".format(len(out))) 

	def close(self):
		self.save()
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

		self.save()
		return True

	def removeColumn(self,name):
		try:
			num = self.header.index(name)
		except:
			return False
		self.header.pop(num)
		for record in self.data:
			record.pop(num)
		self.save()
		return True

	def listRows(self, frm, to):
		pass

if __name__=="__main__":
	f = File("../data/test.csv")
	f.close()
