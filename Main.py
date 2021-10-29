from lib import *
import TestZone
import RpgSheet
import calculadora
import adivinhacao
#import forca

print("********************************************")
print("*				   Menu					  *")
print("********************************************\n")
print()

ListOfOptions = "\
Which program do your want to use?\n\
1. Hangman [Under development]\n\
2. Guess the Number\n\
3. Calculator\n\
4. RPG Sheet Editor\n\
5. TestZone\n\
6. Exit Prograram\
\n\n\
Write your choice: "

while True:
	clear()
	print(ListOfOptions)
	while True:
		Doing = GetInt(">")
		if Doing in range(1, 7):break
	if Doing == 1: #Forca
		assert False, "Under development"
	elif Doing == 2: #adivinhacao
		print("Now running 'Guess the Number'\n")
		adivinhacao.main()
	elif Doing == 3:
		print("Now running 'Calculator'\n")
		calculadora.main()
	elif Doing == 4:
		print("Now running 'RPG Sheet Editor'\n")
		RpgSheet.main()
	elif Doing == 5:
		print("Now running 'TestZone'\n")
		TestZone.main()
	elif Doing == 6:
		print("Exiting...")
		break
