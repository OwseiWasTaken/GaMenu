from lib import * #My libary uses prompt, ErrorPrompt and list for costumizating the 'Get' functions
from random import randint as rint
import pickle

NoOfOptions = 7
RangeOfOptions = range(1, NoOfOptions+1)
Options = [*RangeOfOptions]

#intro!!
print("*************************************")
print("  Welcome to the RPG Sheet Editor!!  ")
print("*************************************\n")

ListOfOptions = "RPG Sheet Editor:\n 1. Create a Sheet\n 2. Show a Sheet\n 3. Level Up\n 4. Roll a dice\n 5. Save a Sheet\n 6. Load a Sheet\n 7. Exit editor\n\nSelect a option: "
DicePrompt = " 1. D4		6. D20\n 2. D6		7. D100\n 3. D8		8. Custom Dice\n 4. D10		9. 'Create a Sheet' Roll\n 5. D12		10. Exit\n\nSelect a option: "

RangeForStats = range(1, 21)

Min = 1

Doing = ""

Name = None
Health = None
BaseSTR = None
BaseDEX = None
BaseCON = None
BaseINT = None
BaseWIS = None
BaseCHA = None

SaveState = None

while True:

	Doing = GetOption(prompt = ListOfOptions, list = Options)

	if Doing == 1:
		print("\nRunning 'Create a Sheet'\n")
	if Doing == 2:
		print("\nRunning 'Show a Sheet'\n")
	if Doing == 3:
		print("\nRunning 'Level Up'\n")
	if Doing == 4:
		print("\nRunning 'Roll a Dice'\n")
	if Doing == 5:
		print("\nRunning 'Save a Sheet'")
	if Doing == 6:
		print("\nRunning 'Load a Sheet'")

# This is the 'Create a sheet' option
	while Doing == 1:
		while True:

			# This asks the users Nickname
			Name = input("What is your name? ")
			Confirmation = GetStr(prompt = f"Is '{Name}' your name? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Strenght
		while True:
			BaseSTR = GetInt(prompt="What is your STR stat? ", list= [*RangeForStats])
			Confirmation = GetStr(prompt="Are you sure? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Dexterity
		while True:
			BaseDEX = GetInt(prompt="What is your DEX stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt="Are you sure? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Constituition
		while True:
			BaseCON = GetInt(prompt="What is your CON stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt="Are you sure? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Intelligence
		while True:
			BaseINT = GetInt(prompt="What is your INT stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt="Are you sure? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		#This asks the users intial Wisdom
		while True:
			BaseWIS = GetInt(prompt="What is your WIS stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt="Are you sure? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		# This asks the users intial Charisma
		while True:
			BaseCHA = GetInt(prompt="What is your CHA stat? ", list=[*RangeForStats])
			Confirmation = GetStr(prompt="Are you sure? ")
			if Confirmation in ["N", "n"]:
				print("So...")
			else:
				print()
				break

		SaveState = {"Name": Name, "Health": Health, "STRstat": BaseSTR, "DEXstat": BaseDEX, "CONstat": BaseCON, "INTstat": BaseINT, "WISstat": BaseWIS, "CHAstat": BaseCHA}
		
		#This create a confirmation, so if the user is unsatisfied with the sheet created, he can redo it
		while True:
			Confirmation = GetStr(prompt = "Do you want to redo everything? ")
			if Confirmation == "Y":
				while True:
					print("ARE YOU SURE?")
					Confirmation = GetStr(prompt = ">>> ")
					if Confirmation == "Y":
						break
					else:
						break
			elif Confirmation == "N":
				print()
				Doing = GetOption(prompt = ListOfOptions, list = Options)
				if Doing == 1:
					print("\nRunning 'Create a Sheet'\n")
				if Doing == 2:
					print("\nRunning 'Show a Sheet'\n")
				if Doing == 3:
					print("\nRunning 'Level Up'\n")
				if Doing == 4:
					print("\nRunning 'Roll a Dice'\n")
				if Doing == 5:
					print("\nRunning 'Save a Sheet'")
				if Doing == 6:
					print("\nRunning 'Load a Sheet'")
				break

# This is the 'Show a sheet' option
	while Doing == 2:

		if SaveState == None:
			print("There is no sheet yet, create or load a sheet...")
			print()
			break
		else:
			print(f"{SaveState}\n")
			break

# NOT WORKING YET
# This is the 'Level Up' option
	while Doing == 3:
		print("under development")
		print()
		break
		
		#The ideia is simple: It shows all currents stats, and how many points we have + health that would be gained and mana...
		#The problem here is: I don't know how level up in top table rpgs... lol

# This is the 'Roll a dice' option
	while Doing == 4:
		WhichDice = GetOption(prompt = DicePrompt, list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
		if WhichDice == 1:
			Max = 4
		elif WhichDice == 2:
			Max = 6
		elif WhichDice == 3:
			Max = 8
		elif WhichDice == 4:
			Max = 10
		elif WhichDice == 5:
			Max = 12
		elif WhichDice == 6:
			Max = 20
		elif WhichDice == 7:
			Max = 100
		elif WhichDice == 8:
			while True:
				NewDice = input("What is the max number that you want? ")
				if not NewDice.isnumeric():
					print("Please remember that you need to enter a number")
				else:
					break
			Max = int(NewDice)
		elif WhichDice == 9:
			NescessariesRolls = 5
			while NescessariesRolls != 0:
				Max = 20
				Roll = rint(Min, Max)
				print(f"You rolled {Roll}")
				NescessariesRolls = NescessariesRolls - 1
		
		elif WhichDice == 10:
			print("Exiting 'Roll a Dice'")
			break

		Roll = rint(Min, Max)
		print(f"You rolled {Roll}")
		print()

		Confirmation = GetStr(prompt = "Do you want to roll again? ('y' for yes, and 'n' for no): ")
		if Confirmation == "Y":
			pass
		elif Confirmation == "N":
			break

# This is the 'Save the sheet' option
	while Doing == 5:
		SaveState = {"Name": Name, "Health": Health, "STRstat": BaseSTR, "DEXstat": BaseDEX, "CONstat": BaseCON, "INTstat": BaseINT, "WISstat": BaseWIS, "CHAstat": BaseCHA}
		Confirmation = GetStr(prompt = "Do you want to save the current sheet? ('y' for yes, and 'n' for no): ")
		if Confirmation == "Y":
			pass
		elif Confirmation == "N":
			print("Exiting Save")
			break
		with open("SheetLog", "wb") as f:
			pickle.dump(SaveState, f)
		print("... ... ... ...\nSaved!\n")
		break

# This is the 'Load a sheet' option
	while Doing == 6:
		Confirmation = GetStr(prompt = "Do you want to load a sheet? ('y' for yes, and 'n' for no): ")
		if Confirmation == "Y":
			pass
		elif Confirmation == "N":
			print("Exiting Load")
			break
		with open("SheetLog", "rb") as f:
			SaveState = pickle.load(f)
		print("... ... ... ...\nLoaded!\n")
		break

# This is the 'Exit editor' option
	if Doing == 7:
		Confirmation = GetStr(prompt="Do your really want to exit? ")
		if Confirmation in ["N", "n"]:
			print("Ok, then\n")
		else:
			print("Existing 'RPG Sheet Editor'")
			break