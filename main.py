#! /bin/python3.10

from lib import *
from TestZone import main as TestZone
from RpgSheet import main as RpgSheet
from calculadora import main as calculadora
from adivinhacao import main as adivinhacao
from forca import main as forca

menu = """
********************************************
*				   Menu					   *
********************************************
"""
ListOfOptions = """
Which program do your want to use?
1. Hangman [udev]
2. Guess the Number
3. Calculator
4. RPG Sheet Editor
5. TestZone
6. Exit Prograram


Your choice:
"""

class OP(IntEnum):
	HANGMAN = auto()
	GUESS = auto()
	CALC = auto()
	RPG = auto()
	TEST = auto()
	EXIT = auto()
	COUNT = auto()

def main():
	print(menu)
	while True:
		clear()
		print(ListOfOptions)
		Doing = GetIn(GetInt, range(1, OP.COUNT), '>')
		match Doing:
			case OP.HANGMAN:
				print("Now running 'Hangman'\n")
				forca()
			case OP.GUESS:
				print("Now running 'Guess the Number'\n")
				adivinhacao()
			case OP.CALC:
				print("Now running 'Calculator'\n")
				calculadora()
			case OP.RPG:
				print("Now running 'RPG Sheet Editor'\n")
				RpgSheet()
			case OP.TEST:
				print("Now running 'TestZone'\n")
				TestZone()
			case OP.EXIT:
				print("Exiting...")
				break

if __name__ == "__main__":main()
