#This is Anghie's library
from random import *

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

# Yo, this is a really IMPORTANT WARNING, if you for any reason, needs a specific roll, you MUST pay atention to what you are going to write as the 'prompt' cuz if u mess it up
# It will not work!
# The ''Create a Sheet' Roll' function will work as: prompt = "Run 6 D20".
def Dice(EspecifictRoll = None, CustomDiceMax = None):

	DicePrompt = " 1. D4		6. D20\n 2. D6		7. D100\n 3. D8		8. Custom Dice\n 4. D10		9. 'Create a Sheet' Roll\n 5. D12		10. Exit\n\nSelect a option: "
	Min = 1
	Roll = 0

	if EspecifictRoll == None:	
		WhichDice = GetOption(prompt = DicePrompt, list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	else:
		WhichDice = EspecifictRoll

	if WhichDice == 1 or "D4":
		Max = 4
	elif WhichDice == 2 or "D6":
		Max = 6
	elif WhichDice == 3 or "D8":
		Max = 8
	elif WhichDice == 4 or "D10":
		Max = 10
	elif WhichDice == 5 or "D12":
		Max = 12
	elif WhichDice == 6 or "D20":
		Max = 20
	elif WhichDice == 7 or "D100":
		Max = 100
	elif WhichDice == 8 or "Custom Dice":
		if CustomDiceMax == None:
			while True:
				NewDice = input("What is the max number that you want? ")
				if not NewDice.isnumeric():
					print("Please remember that you need to enter a number")
				else:
					break
		else:
			NewDice = CustomDiceMax
		Max = int(NewDice)

	elif WhichDice == 9 or "Run 6 D20":
		NescessariesRolls = 5
		while NescessariesRolls != 0:
			Max = 20
			Roll = randint(Min, Max)
			print(f"You rolled {Roll}")
			NescessariesRolls = NescessariesRolls - 1
	
	elif WhichDice == 10:
		print("Exiting 'Roll a Dice'")
		return

	Roll = randint(Min, Max)
	print(f"You rolled {Roll}")
	print()

	if EspecifictRoll == None:
		Confirmation = GetStr(prompt = "Do you want to roll again? ('y' for yes, and 'n' for no): ")
		if Confirmation == "Y":
			return Dice
		elif Confirmation == "N":
			return Roll
	else:
		return Roll