from lib import *

#Intro:
print("*************************************")
print("                 Menu                ")
print("*************************************")
print()

Options = range(1, 7)

ListOfOptions = "Which program do your want to use?\n 1. Hangman\n 2. Guess the Number\n 3. Calculator\n 4. RPG Sheet Editor\n 5. TestZone\n 6. Exit Prograram\n\nWrite your choice: "

Doing = GetOption(prompt = ListOfOptions, list = Options)

Doing = int(Doing)

while True:
	if Doing == 1: #Forca
		print("Under development\n")
		#import forca
	elif Doing == 2: #adivinhacao
		print("Now running 'Guess the Number'\n")
		import adivinhacao
	elif Doing == 3:
		print("Now running 'Calculator'\n")
		import calculadora
	elif Doing == 4:
		print("Now running 'RPG Sheet Editor'\n")
		import RpgSheet
	elif Doing == 5:
		print("Now running 'TestZone'\n")
		import TestZone
	elif Doing == 6:
		print("Exiting...")
		break
	print()

	Doing = GetOption(prompt = ListOfOptions, list = Options)
