from classes import fileiohandler
from classes import printTable
from classes import dataToHumanReadable

class File:

	def openFile(self,path):
		self.io = fileiohandler.FileIOHandler(path)
		self.io.openToRead()
		data = self.io.read().strip()
		
		if data == '':
			# print("FILE EMPTY")
			pass
		else:
			data = data.split('\n')
			
			while '' in data:
				data.remove('')
			# print(self.data)
			
			header = data.pop(0)
			header = ["id"] + header.split(',')
			data = [x.split(',') for x in data]
			data = [[str(x)]+data[x] for x in range(len(data))]

			self.data = data
			self.header = header

	def __init__(self,path=''):
		self.header = ["id"]
		self.data = []
		self.openFile(path)



	def headerToString(self):
		return ','.join(self.header[1:])

	def dataToString(self):
		return '\n'.join([','.join(x[1:]) for x in self.data])

	def save(self):
		self.io.openToWrite()
		toPrint = self.headerToString()+'\n'+self.dataToString()+'\n'
		# print(toPrint)
		out = self.io.write(toPrint)
		print("{} bytes was written.".format(dataToHumanReadable.bytes_2_human_readable(out))) 
		return 0

	def close(self):
		self.save()
		self.io.close()
		return 0

	def listColumns(self):
		return ", ".join(self.header)

	def addColumn(self, name, defValue):
		if (name in self.header) or (name == ''):
			return 1

		self.header.append(name)

		if defValue == '':
			defValue = '-'
		for record in self.data:
			record.append(defValue)

		self.save()
		return 0

	def removeColumn(self,name):
		try:
			num = self.header.index(name)
		except:
			return 1
		self.header.pop(num)
		for record in self.data:
			record.pop(num)
		self.save()
		return 0

	def headerToPrint(self,header):
		return '\t'.join(header)

	def recordToPrint(self,record):
		return '\t'.join(record)

	def listRows(self, frm, to):
		num = len(self.data)
		frm = int(frm)
		to = int(to)
		if frm > num or to > num or frm > to:
			return 1

		data  = list()
		for record in self.data[frm-1:to]:
			data.append(record)


		# print('data',data)

		printTable.print_table(data, header=self.header, wrap=True, max_col_width=20, wrap_style='wrap',
            row_line=True, fix_col_width=False, extender_spaces=3, extender_string=' ')

	def addRow(self,parameters):
		self.data.append(parameters)
		num = len(self.data)
		self.listRows(num,num)
		return 0

	def size(self):
		return len(self.data)

	def nextID(self):
		return 0 if len(self.data) <= 0 else str(int(self.data[-1][0])+1)
		# Maybe in the future there will be negative list indexes. Who knows?...

	def removeRow(self,id):
		index = 1
		# print(self.data)
		while (self.data[index-1][0] != str(id)) and ((index-1)<len(self.data)):
			# print(self.data[index][0])
			# print(id)
			index += 1
		# print(index)

		if index-1>=len(self.data):
			return 1
		else:
			self.data.remove(self.data[index-1])
			return 0

	def reNameColumn(self,old,new):
		if not (old in self.header):
			return 1

		self.header[self.header.index(old)] = new 

if __name__=="__main__":
	f = File("../data/test.csv")
	f.close()
