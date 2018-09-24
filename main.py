#!/usr/bin/python3

import commands
import classes
import config

COMMAND_LIST = {
	"help": commands.helper
}

FILE = None

def init():
	global FILE
	FILE = classes.file.File(config.DEFAULT_FILE_PATH)

def destruct():
	FILE.close()

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
	init()
	main()
	destruct()
	print("STOP")
