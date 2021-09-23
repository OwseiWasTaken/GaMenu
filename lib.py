#This is Anghie's library

def GetInt(prompt = "Please enter a number: ", ErrorPrompt = None, list = [1, 2, 3]):
	Intenger = input(prompt)
	if not Intenger.isnumeric():
		if ErrorPrompt == None:
			print(f"\nPlease enter something that's in {list}\n")
		else:
			print(ErrorPrompt)
		return GetInt(prompt = prompt, ErrorPrompt = ErrorPrompt, list = list)
	Intenger = int(Intenger)
	if list == None:
		pass
	else:
		if Intenger not in list:
			if ErrorPrompt == None:
				print(f"\nPlease enter something that's in {list}")
			else:
				print(ErrorPrompt)
			return GetInt(prompt = prompt, ErrorPrompt = ErrorPrompt, list = list)
		else:
			Intenger = int(Intenger)
			return Intenger

def GetStr(prompt = "Please enter a string: ", ErrorPrompt = None, list = ["Y", "N"]):
	String = input(prompt)
	String = String.upper()
	if list == None:
		pass
	else:
		if String not in list:
			if ErrorPrompt == None:
				print(f"\nPlease enter something that's in {list}\n")
			else:
				print(ErrorPrompt)
			return GetStr(prompt = prompt, ErrorPrompt = ErrorPrompt, list = list)
		else:
			return String

def GetOption(prompt = None, ErrorPrompt = None, list = ["1", "2", "3"]):

	if prompt == None:
		Option = input(f"Which option do you want? {list} (No need for captalization): ")
	else:
		Option = input(prompt)

	if Option.isnumeric():
		Option = int(Option)
	else:
		Option = Option.upper()

	if Option not in list:
		if ErrorPrompt == None:
			print(f"\nPlease enter something that's in {list}\n")
		else:
			print(ErrorPrompt)
		return GetOption(prompt = prompt, ErrorPrompt = ErrorPrompt, list = list)
	else:
		return Option
