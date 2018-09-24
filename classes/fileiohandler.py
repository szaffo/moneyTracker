class FileIOHandler:

	def __init__(self, path):
		self.path = path
		self.stream = open(self.path,'r')
		self.direction = "IN"

	def changeDirection(self):
		if self.direction == "IN":
			sef.direction = "OUT"
			self.stream.close()
			self.stream = open(self.path,'w')
		elif self.direction == "OUT":
			self.direction = "IN"
			self.stream.close()
			self.stream = open(self.path,'w')

	def openToWrite(self):
		if self.direction != "OUT":
			self.changeDirection()

	def openToRead(self):
		if self.direction != "IN":
			self.changeDirection()

	def read(self):
		if self.direction == "IN":
			return self.stream.read()
		else:
			return ""

	def write(self,data):
		if self.direction == "OUT":
			self.stream.write(data)
			return data
		else:
			return ""

	def close(self):
		self.stream.close()
