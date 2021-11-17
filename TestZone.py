from lib import *
import random

def main():
	question = "Which test do you want to do now?\n 1. 'For' loop test\n 2. Password Maker\n 3. None\n>>> "
	NumberOfOptions = 3
	RangeOfOptions = range(1, NumberOfOptions+1)
	options = [*RangeOfOptions]

	while True:
		ActualTest = GetOption(prompt = question, list = options)

		# For loop test
		while ActualTest == 1:
			cont = 0

			print("Welcome! This is the for loop test area, where we will count the exact number of characters in a word.")

			palavra = input("Please input any word: ")

			letras = []


			for letras in palavra:
				cont += 1

			print(f"\nThere is {cont} characters in '{palavra}'\n")

			ActualTest = GetOption(prompt=question, list=options)

		lower = "abcdefghijklmnopqrstuvwxyz"
		upper = lower.upper()
		numbers = "0123456789"
		symbols = r"_({[]})*;:/,.-@#$ "
		all = lower+upper+numbers+symbols
		leght = 16
		# Password Maker
		while ActualTest == 2:
			password = "".join(random.sample(all,leght))
			print(f"\nGenerated Password : {password}\n")

			ActualTest = GetOption(prompt=question, list=options)

		# Exit function
		if ActualTest == 3:
			print("\nExiting TestZone...")
			break
if __name__ == "__main__":main()
