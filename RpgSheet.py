from lib import *
import pickle
from dataclasses import dataclass
import sys
#TODO safer design

print("*************************************")
print("  Welcome to the RPG Sheet Editor!!	")
print("*************************************\n")

types = (
	"Create a new Sheet",
	"List Sheets",
	"Show a Sheet",
	"Level Up",
	"Roll Dice",
	"Delete Sheet",
	"Save",
	"Load",
	"Clear",
	"Exit",
)

def main():
	class OP(IntEnum):
		MakeSheet = auto()
		ListSheets = auto()
		PrintSheet = auto()
		LevelUp = auto()
		RollDice = auto()
		DeleteSheet = auto()
		Save = auto()
		Load = auto()
		Clear = auto()
		Exit = auto()
		COUNT = auto()

	Sheets = []
	#Sheets.append(Sheet("pedro", 100, Stats(0, 0, 0, 0, 0, 2)))
	#Sheets.append(Sheet("owsei", 100, Stats(2, 0, 0, 0, 0, 0)))
	#Sheets.append(Sheet("o", 100, Stats(2, 2, 2, 2, 2, 2)))
	def PrintSheet():
		nonlocal Sheets
		for i in r(Sheets):
			print(f"{i+1}: {Sheets[i].Name}")
	while True:
		for i in r(types):
			print(f"{i+1}: {types[i]}")
		Doing = GetIn(GetInt, range(1, OP.COUNT), '>')
		print()
		match Doing:
			case OP.MakeSheet:# make sheet
				Sheets.append(MakeSheet())
				Sheets = sorted(Sheets)
			case OP.PrintSheet:
				PrintSheet()
				ShowSheet = GetIn(GetInt, range(len(Sheets)+1), 'Sheet$')-1
				PrintSheet(Sheets[ShowSheet])
			case OP.ListSheets:
				PrintSheet()
				print('\n')
			case OP.LevelUp:pass
			case OP.RollDice:pass
			case OP.DeleteSheet:
				PrintSheet()
			case OP.Save:
				UseFile("rpg.dat", Sheets)
			case OP.Load:
				#TODO
				#if Sheets:
				ld = UseFile("rpg.dat")
				ldr = False # load will remove
				rms:list[Sheet] = [] # removes
				if Sheets:
					for i in r(ld):
						if not Sheets[i] in ld:
							ldr = True
							rms.append(Sheets[i].Name)
				if ldr:
					print("loading error")
					print(f"there are {len(rms)} created sheets that are not in rpg file")
					print("replace or append? [r/a]")
					x = GetIn(input, ['r', 'R', 'a', 'A'], '>').lower()
					if x == 'r':
						Sheets = ld # replace
					else:
						Sheets = list(set([*Sheets, *ld])) # append (ironically doens't uses append)
				else:
					Sheets = ld

			case OP.Clear:
				clear()
			case OP.Exit:
				exit(0)


		#The ideia is simple: It shows all currents stats, and how many points we have + health that would be gained and mana...
		#The problem here is: I don't know how level up in top table rpgs... lol

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
	def __gt__(this, x):
		assert type(x) == Sheet
		return this.Name > x.Name

def PrintSheet(sheet):
	print(f"""
=====================
= {sheet.Name}{' '*(17-len(sheet.Name))} =
=====================
Stats:
-> STR: {sheet.Stats.STR}
-> DEX: {sheet.Stats.DEX}
-> CON: {sheet.Stats.CON}
-> INT: {sheet.Stats.INT}
-> WIS: {sheet.Stats.WIS}
-> CHA: {sheet.Stats.CHA}
""")

def LevelUp():pass
def RollDice():pass

def Get(prompt, confs = "is \"%s\" right?", conflist = ['Y', 'y', "yes", "Yes", "YES"], GetFunc = input):
	ipt = GetFunc(prompt)
	if confs:
		conf = input(confs % ipt)
		if not conf in conflist:
			return Get(prompt, confs, conflist)
	return ipt

_gts = list(range(1, 21))
def GetStat(StatName):
	global _gts
	return GetIf(GetInt, lambda x: x in _gts, "What is your %s stat? " % StatName)

def MakeSheet():
	# This asks the user's stuff
	Name = Get("What is your name:")
	BaseSTR = GetStat("STR")
	BaseDEX = GetStat("DEX")
	BaseCON = GetStat("CON")
	BaseINT = GetStat("INT")
	BaseWIS = GetStat("WIS")
	BaseCHA = GetStat("CHA")
	return Sheet(
		Name, 100,# 100?
		Stats( BaseSTR, BaseDEX, BaseCON, BaseINT, BaseWIS, BaseCHA)
	)

if __name__ == "__main__":main()
