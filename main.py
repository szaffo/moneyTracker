#!/usr/bin/python3

import commands

COMMAND_LIST = {
	"help": commands.helper
}

def main():
	exit = False;
	prompt = "\n$> "
	while not exit:
		userInput = input(prompt).lower().split(' ')
		command = userInput.pop(0)
		args = userInput

		if command == "exit":
			exit = True
		elif command in COMMAND_LIST:
			COMMAND_LIST[command]()
		else:
			commands.unknown()

	return 0

if __name__=="__main__":
	print("Money Tracker [v 0.1]")
	main()
	print("STOP")
