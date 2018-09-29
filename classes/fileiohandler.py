class fakeFile:
	def write(*args):
		# print("No file opend")
		return 0

	def read(*args):
		# print("No file opened")
		return ''

	def close(*args):
		pass

class FileIOHandler:

	def opener(self,path,direction='r'):
		self.path = path
		if '' == path:
			self.stream = fakeFile()
		else:
			self.stream = open(f".data/{self.path}",directon)

	def __init__(self, path):
		self.opener(path)
		self.direction = "IN"

	def save(self):
		self.direction = "IN"
		self.stream.close()
		self.opener(self.path,'r')

	def changeDirection(self):
		if self.direction == "IN":
			self.direction = "OUT"
			self.stream.close()
			self.opener(self.path,'w')
		elif self.direction == "OUT":
			self.direction = "IN"
			self.stream.close()
			self.opener(self.path,'r')

	def openToWrite(self):
		if self.direction != "OUT":
			self.changeDirection()

	def openToWriteDirect(self):
		#for debug
		self.stream.close()
		self.opener(self.path,'w')

	def openToRead(self):
		if self.direction != "IN":
			self.changeDirection()

	def read(self):
		if self.direction == "IN":
			return self.stream.read()
		else:
			return ""

	def write(self,data):
		#print("in write")
		if self.direction == "OUT":
			byte = self.stream.write(data)
			self.save()
			return byte
		else:
			return 0

	def close(self):
		self.stream.close()
