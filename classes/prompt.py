import keyboard

class Prompt:

	def __init__(self, prompt="$> ", history=[]):
		self.prompt = prompt
		self.history = history

	def read(self):
		print("\n{}".format(self.prompt))

		char = keyboard.read_key()
		while (char!= 'enter'):
			print("Press Enter")
			char = keyboard.read_key()

if __name__=="__main__":
	p = Prompt()
	p.read()
