from classes import fileiohandler
from classes import printTable

def bytes_2_human_readable(number_of_bytes):
	# This function comes from StackOverflow
	# https://stackoverflow.com/questions/12523586/python-format-size-application-converting-b-to-kb-mb-gb-tb/37423778 (2018)
    if number_of_bytes < 0:
        raise ValueError("!!! number_of_bytes can't be smaller than 0 !!!")

    step_to_greater_unit = 1024.

    number_of_bytes = float(number_of_bytes)
    unit = 'bytes'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'KB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'MB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'GB'

    if (number_of_bytes / step_to_greater_unit) >= 1:
        number_of_bytes /= step_to_greater_unit
        unit = 'TB'

    precision = 1
    number_of_bytes = round(number_of_bytes, precision)

    return str(number_of_bytes) + ' ' + unit

class File:
	def __init__(self,path):
		self.io = fileiohandler.FileIOHandler(path)
		self.io.openToRead()
		self.data = self.io.read().strip()
		if self.data == '':
			print("FILE EMPTY")
			self.header = ["id"]
			self.data = []
			return 
		self.data = self.data.split('\n')
		while '' in self.data:
			self.data.remove('')
		# print(self.data)
		self.header = self.data.pop(0)
		self.header = ["id"] + self.header.split(',')
		self.data = [x.split(',') for x in self.data]
		self.data = [[str(x)]+self.data[x] for x in range(len(self.data))]



	def headerToString(self):
		return ','.join(self.header[1:])

	def dataToString(self):
		return '\n'.join([','.join(x[1:]) for x in self.data])

	def save(self):
		self.io.openToWrite()
		toPrint = self.headerToString()+'\n'+self.dataToString()+'\n'
		# print(toPrint)
		out = self.io.write(toPrint)
		print("{} bytes was written.".format(bytes_2_human_readable(len(out)))) 
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

if __name__=="__main__":
	f = File("../data/test.csv")
	f.close()
