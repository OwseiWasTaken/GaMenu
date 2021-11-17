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
	"Show a Sheet",
	"Level Up",
	"Roll Dice",
	"Save",
	"Load",
	"Exit",
)
def main():
	class OP:
		MakeSheet = 0
		PrintSheet = 1
		LevelUp = 2
		RollDice = 3
		Save = 4
		Load = 5
		Exit = 6
	Sheets = []
	Sheets.append(Sheet("pedro", 100, Stats(0, 0, 0, 0, 0, 2)))
	Sheets.append(Sheet("owsei", 100, Stats(2, 0, 0, 0, 0, 0)))
	while True:
		for i in r(types):
			print(f"{i+1}: {types[i]}")
		Doing = GetIn(GetInt, range(1, 8), '>')-1
		match Doing:
			case OP.MakeSheet:# make sheet
				Sheets.append(MakeSheet())
			case OP.PrintSheet:
				for i in r(Sheets):
					print(f"{i+1}: {Sheets[i].Name}")
				ShowSheet = GetIn(GetInt, range(len(Sheets)+1), '>')-1
				PrintSheet(Sheets[ShowSheet])
				continue
			case OP.LevelUp:pass
			case OP.RollDice:pass
			case OP.Save:
				Save(Sheets)
			case OP.Load:
				#TODO
				#if Sheets:
				Sheets = Load(Sheets)
			case OP.Exit:
				exit(0)
		clear()


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

def Save(sheets: list[Sheet]):
	pickle.dump(sheets, (f:=open("rpg.dat", 'bw')))
	f.close()

def Load():
	ld = pickle.load((f:=open("rpg.dat", 'br')))
	f.close()
	return ld

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
