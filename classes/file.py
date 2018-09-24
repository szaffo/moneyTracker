import fileiohandler

class File:
	def __init__(self,path):
		self.io = fileiohandler.FileIOHandler(path)
		self.io.openToRead()
		self.data = self.io.read()
		self.header = self.data.split('\n').pop(0).split(',')
		self.data = [x.split(",") for x in self.data.split("\n")]
		while [] in self.data:
			self.data.remove([])

	def close(self):
		self.io.close()

if __name__=="__main__":
	f = File("../data/test.csv")
	f.close()
