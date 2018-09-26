#!/usr/bin/sudo python3

import commands
import classes
import config

COMMAND_LIST = {
	"help": commands.helper,
	"ac": commands.addColumn,
	"lc": commands.listColumns,
	"rc": commands.removeColumn
}


FILE = None

GLOBALS = {
	"FILE": FILE
}

def init():
	global GLOBALS
	GLOBALS["FILE"] = classes.file.File(config.DEFAULT_FILE_PATH)

def destruct():
	GLOBALS["FILE"].close()

def main():
	exit = False;
	prompt = "\n$> "
	while not exit:
		userInput = input(prompt).lower().strip().split(' ')
		command = userInput.pop(0)
		args = tuple(userInput)

		if command == "exit":
			exit = True
		elif command in COMMAND_LIST:
			COMMAND_LIST[command](GLOBALS,args)
		else:
			commands.unknown(GLOBALS)
	return 0

if __name__=="__main__":
	print("Money Tracker [v0.2]")
	init()
	main()
	destruct()
	print("STOP")
