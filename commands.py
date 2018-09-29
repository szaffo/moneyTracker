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

	if 1 == rV:
		print("Can't add this column")

def removeColumn(globals,args=('',)):
	try:
		name = args[0]
	except:
		name = input("Name: ")

	if 1 == globals["FILE"].removeColumn(name):
		print("Column not found")


def listRows(globals, args=('',)):
	# print(args)
	try:
		if args[0] == '-a':
			globals["FILE"].listRows(1,globals["FILE"].size())
			return None

		if args[0] == '-s':
			print("Size of database:",globals["FILE"].size())
			return None
	except:
		pass

	try:
		frm = int(args[0])
	except:
		frm = input("From: ")

	try:
		to = int(args[1])
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

def addRow(globals,args=('', )):
	args = list(args)
	headers = globals["FILE"].header.copy()
	parameters = []
	id = headers.pop(0)
	parameters.append(globals["FILE"].nextID())
	for element in headers:
		try:
			parameters.append(args[0])
			args.pop(0)
		except:
			parameters.append(input("{}: ".format(element)))

	globals["FILE"].addRow(parameters)


def removeRow(globals,args=('',)):
	try:
		id = args[0]
	except:
		id = input("id: ")
		
	try:
		to = args[1]
	except:
		to = id

	for x in range(int(id),int(to)+1):	
		if 1 == globals["FILE"].removeRow(str(x)):
			print("No matching")


def reNameColumn(globals,args=('',)):
	try:
		old = args[0]
	except:
		old = input("Old name: ")

	try:
		new = args[1]
	except:
		new = input("New name: ")


	globals["FILE"].reNameColumn(old,new)

def open(globals,args=('',)):
	try:
		file = args[0]
	except:
		file = input("File: ")

	try:
		globals["FILE"].openFile(file)
	except:
		print("Can't open file")



if __name__=="__main__":
	helper()
