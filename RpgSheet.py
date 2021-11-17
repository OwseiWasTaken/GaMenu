from lib import * #My libary uses prompt, ErrorPrompt and list for costumizating the 'Get' functions
from random import randint as rint
import pickle
from dataclasses import dataclasse

def main():

	print("*************************************")
	print("  Welcome to the RPG Sheet Editor!!	")
	print("*************************************\n")

	ListOfOptions = """RPG Sheet Editor:
1. Create a Sheet
2. Show a Sheet
3. Level Up
4. Roll a dice
5. Save a Sheet
6. Load a Sheet
7. Exit editor
	"""

	DicePrompt = """
1. D4		6. D20
2. D6		7. D100
3. D8		8. Custom Dice
4. D10		9. 'Create a Sheet' Roll
5. D12		10. Exit
"""


	RangeForStats = list(range(1, 21))
	Min = 1

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
		print(ListOfOptions)
		GetIn(GetInt, range(1, 8), "Select a option:")
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
			print("... ... ... ...")
			with open("SheetLog", "wb") as file:
				pickle.dump(SaveState, file)
			print("Saved!")

	# This is the 'Load a sheet' option
		while Doing == 6:
			Confirmation = GetStr(prompt = "Do you want to load a sheet? ('y' for yes, and 'n' for no): ")
			if Confirmation == "Y":
				pass
			elif Confirmation == "N":
				print("Exiting Load")
				break
			print("... ... ... ...")
			with open("SheetLog", "rb") as f:
				SaveState = pickle.load(f)
			print("Loaded!")

	# This is the 'Exit editor' option
		if Doing == 7:
			Confirmation = GetStr(prompt="Do your really want to exit? ")
			if Confirmation in ["N", "n"]:
				print("Ok, then\n")
			else:
				print("Existing 'RPG Sheet Editor'")
				break

@dataclass
class Stats:
	STR:int
	DEX:int
	CON:int
	INT:int
	WIS:int
	CHA:int

@dataclass
class Sheet:
	Name:str
	Health:int
	Stats:Stats

def Get(prompt, confs = "is \"%s\" right?", conflist = ['Y', 'y'], GetFunc = input):
	ipt = GetFunc(prompt)
	if confs:
		conf = input(confs % ipt)
		if not conf in conflist:
			return Get(prompt, confs, conflist)
	return ipt

def GetStat(StatName):
	return Get("What is your %s stat? " % StatName, conflist = RangeForStats, GetFunc = GetInt)

def MakeSheet():
	# This asks the users Nickname
	Name = Get("What is your name:")

	#This asks the users intial Strenght
	BaseSTR = GetStat("STR")

	#This asks the users intial Dexterity
	BaseDEX = GetStat("DEX")

	#This asks the users intial Constituition
	BaseSTR = GetStat("CON")

	#This asks the users intial Intelligence
	BaseINT = GetStat("INT")

	#This asks the users intial Wisdom
	BaseWIS = GetStat("WIS")

	# This asks the users intial Charisma
	BaseCHA = GetStat("CHA")

	return Sheet(
		Name, Health,
		Stats( BaseSTR, BaseDEX, BaseCON, BaseINT, BaseWIS, BaseCHA)
	)

if __name__ == "__main__":main()
