from lib import *
import TestZone
import RpgSheet
import calculadora
import adivinhacao
#import forca

print("********************************************")
print("*                   Menu                   *")
print("********************************************")
print()

ListOfOptions = """
Which program do your want to use?
1. Hangman [Under development]
2. Guess the Number
3. Calculator
4. RPG Sheet Editor
5. TestZone
6. Exit Prograram


Write your choice:
"""[1:-1] # [...] cus \n at start and end
class OP:
	HANGMAN = 1
	GUESS = 2
	CALC = 3
	RPG = 4
	TEST = 5
	EXIT = 6

while True:
	clear()
	print(ListOfOptions)
	Doing = GetIn(GetInt, range(1, 8), '>')
	match Doing:
		case OP.HANGMAN:
			assert False, "Under development"
		case OP.GUESS:
			print("Now running 'Guess the Number'\n")
			adivinhacao.main()
		case OP.CALC:
			print("Now running 'Calculator'\n")
			calculadora.main()
		case OP.RPG:
			print("Now running 'RPG Sheet Editor'\n")
			RpgSheet.main()
		case OP.TEST:
			print("Now running 'TestZone'\n")
			TestZone.main()
		case OP.EXIT:
			print("Exiting...")
			break
