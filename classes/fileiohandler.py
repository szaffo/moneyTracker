class FileIOHandler:

	def __init__(self, path):
		self.path = path
		self.stream = open(self.path,'r')
		self.direction = "IN"

	def changeDirection(self):
		if self.direction == "IN":
			self.direction = "OUT"
			self.stream.close()
			self.stream = open(self.path,'w')
		elif self.direction == "OUT":
			self.direction = "IN"
			self.stream.close()
			self.stream = open(self.path,'r')

	def openToWrite(self):
		if self.direction != "OUT":
			self.changeDirection()

	def openToWriteDirect(self):
		#for debug
		self.stream.close()
		self.stream = open(self.path,"w")

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
			self.stream.write(data)
			#self.close()
			#print("data written")
			return data
		else:
			return ""

	def close(self):
		self.stream.close()
