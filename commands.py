#!/usr/bin/python3

def helper(globals,args=('',)):
	print("This is the help")
	print("\tThere is nothing here.")
	print("\tMaybe you should try 911")

	if "-h" in args:
		print("Switch triggered")

def unknown(globals,args=('',)):
	print("Unknown command")
	print("Try help")

def listColumns(globals,args=('',)):
	f = globals["FILE"]
	print(f.listColumns())

def addColumn(globals,args=('',)):
	try:
		name =args[0]
	except:
		name = input("Name: ")

	try:
		defValue = args[1]
	except:
		defValue = input("Default value: ")

	rV = globals["FILE"].addColumn(name,defValue)

	if not rV:
		print("Can't add this column")

def removeColumn(globals,args=('',)):
	try:
		name = args[0]
	except:
		name = input("Name: ")

	if not globals["FILE"].removeColumn(name):
		print("No column found")


def listRows(globals, args=('',)):
	try:
		frm = args[0]
	except:
		frm = input("From: ")

	try:
		to = args[1]
	except:
		to = input("To: ")

	if globals["FILE"].listRows(frm,to) == 1:
		print("Range Error")


def evil(globals,args=('',)):
	f = globals["FILE"]

	try:
		toev = args[0]
	except:
		toev = input(">>> ")

	while toev != 'stop':
		try:
			print(eval(toev))
		except Exception as e:
			print(e)
		toev = input(">>> ")


if __name__=="__main__":
	helper()
