#!/usr/bin/python3

def helper(args=('',)):
	print("This is the help")
	print("\tThere is nothing here.")
	print("\tMaybe you should try 911")

	print(args)
	if "-h" in args:
		print("Switch triggered")

def unknown(args=('',)):
	print("Unknown command")
	print("Try help")

if __name__=="__main__":
	helper()
