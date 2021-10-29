#! /bin/python3.9

#This is Anghie's library
from random import randint as rint
from sys import platform as OS
from os import system as ss

nop = lambda *a, **b:None # gets anything, does nothing and returns None

if OS in ["linux", "osx"]:
	def clear():
		ss("clear")
elif OS == "windows":
	def clear():
		ss("cls")


def r(end:object, offset = 0, diff = nop) -> int:
	ret = range(len(end)+offset)
	if diff != nop:
		ret = diff(nop)
	return ret

def GetInt(prompt = "Enter a number:", Error = None, parse = eval):
	while True:
		ipt = input(prompt)
		if [True for x in ipt if x in "0987654321+-"]:
			return parse(ipt)
		else:
			if Error:
				raise Error

def GetStr(prompt = "Please enter a string:", Error = None, lst = None, parse = nop):
	String = input(prompt)
	if parse != nop:
		String = parse(String)
	if not lst:
		return String
	else:
		if String in lst:
			return String
		else:
			if Error:
				raise Error
			else:
				print(f"\nPlease enter something that's in {lst}\n")
			return GetStr(prompt, Error, lst)


# Yo, this is a really IMPORTANT WARNING, if you for any reason, needs a specific roll, you MUST pay atention to what you are going to write as the 'prompt' cuz if u mess it up
# It will not work!
# The ''Create a Sheet' Roll' function will work as: prompt = "Run 6 D20".
def dice(CustomDiceMax = None, CanRetryRolls = False):
	if CustomDiceMax: # why? just use rint
		return rint(0, CustomDiceMax)
	else:
		Dices = [
			2,  4,  6,  8,
			10, 20, 50, 100,
		] # len(Dices) needs to be even
		offset = len(Dices)//2
		for i in range(len(Dices)//2):
			print(f"{i+1}. D{Dices[i]}    {i+offset+1}. D{Dices[i+offset]}")
		print(f"{len(Dices)+1}. Custom {0}. Exit")

		# gets dice option
		while True:
			WhichDice = GetInt(prompt = ">")-1
			if WhichDice in [-1]+list(range(len(Dices)+1)): break

		# set opt / exit / custom dice
		if WhichDice in list(range(len(Dices))):
			Max = Dices[WhichDice]
		else:
			if WhichDice == 8:
				while True:
					Max = GetInt("What is the max number that you want:")
					if Max > 0: break
			else: # WhichDice == 0
				return
		# make roll
		Roll = rint(1, Max) # min = 1
		print(f"You rolled {Roll}!\n")

		if CanRetryRolls:
			Confirmation = GetStr(prompt = "Do you want to roll again: [Y/n]").upper()
			if Confirmation == "Y":
				return dice(CustomDiceMax, CanRetryRolls)
			elif Confirmation == "N":
				return Roll
		else:
			return Roll
