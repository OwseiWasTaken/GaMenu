from random import randint as rint

def main():
	#Intro:
	print("*************************************")
	print("    Welcome to Guess the Number!!	")
	print("*************************************")
	print()

	ContinuarJogo = "y"
	Score = 0
	Tentativas = 0

	#Definindo a função que perguntará e nos dara a resposta do usuário:
	def PegarChute() -> int:
		print()
		print(f"Turn: {Rodada+1} from {TotalDeRodadas}")
		Numero = input(f"Write a number between {Min} and {Max}: ")
		if not Numero.isnumeric():
			print("A number!!")
			return PegarChute()
		else:
			Chute = eval(Numero)
			if Chute > Max or Chute < Min:
				print(f"A number between {Min} and {Max}!!")
				return PegarChute()
			ConfirmacaoDeChute = input(f"Did you write: {Chute}? 'y' for yes and 'n' no: ")
			while True:
				if ConfirmacaoDeChute not in ["y", "Y", "n", "N"]:
					print()
					ConfirmacaoDeChute = input("Please, 'Y' or 'N': ")
				else:
					break
			if ConfirmacaoDeChute in ["n", "N"]:
				return PegarChute()
			Chute = eval(Numero)
			return Chute

	while ContinuarJogo != "n":
		TotalDeRodadas = 3
		Dificuldade = input("Select the difficulty level? Easy (1), Medium (2) or Hard (3)? ")
		if not Dificuldade.isnumeric():
			print("1 for Easy, 2 for Medium and 3 for Hard!!")
			continue
		if Dificuldade == "1":
			Min = 1
			Max = 10
		elif Dificuldade == "2":
			Min = 1
			Max = 100
			TotalDeRodadas = 5
		elif Dificuldade == "3":
			print("Good luck, you will needs it. lol!")
			print()
			Min = 1
			Max = 10000
			TotalDeRodadas = 10
		else:
			print("1 for Easy, 2 for Medium and 3 for Hard!!")
			continue
		NumeroSecreto = rint(Min, Max)
		#Para debug:
		#print(NumeroSecreto)
		Rodada = 0
		print()
		print("Random number generated")
			#Sistema de Acerto e Erros:
		while Rodada != TotalDeRodadas:
			Chute = PegarChute()
			Acertou = Chute == NumeroSecreto
			Tentativas += 1
			if Acertou and Dificuldade == "1":
				print()
				print(f"You won!! Using {Rodada+1} turns")
				Score+=5000
				break
			elif Acertou and Dificuldade == "2":
				print()
				print(f"You won!! Using {Rodada+1} turns")
				Score +=10000
				break
			elif Acertou and Dificuldade == "3":
				print()
				print(f"You won!! Using {Rodada+1} turns")
				Score+=99999999999999999999999999999999999999999999999999999999999999999999999999999999999
				break
			else:
				print("Wrong")
				Rodada+=1
					#A variável "diff" será usada para identificar automaticamente se o chute foi muito alto / muito baixo.
				diff = "too high" if Chute > NumeroSecreto else "too low"
				print()
				print(f"You guessed {diff}")
				continue
			if Score >= 9999999999999999999999999999999999999999999999999999999999999999999999999999999999:
				print("You are way too good, here, the ultimate prize!")
				print("...")
				print("...")
				print("...")
				print("...")
				print("Nothing!!! Cuz i don't have anything that is really good for your, the ultimate winner...")
				break
		if Rodada == TotalDeRodadas:
			print()
			print("Too bad! You lost")
			print(f"The secret number was: {NumeroSecreto}")
			print()
		ContinuarJogo = input("Want to replay the game? 'Y' for yes and 'N' for no: ")

	print()
	print(f"Your final score was: {Score}! With {Tentativas} totall turns")
	print("\nRemember, greater score with less turns is way better then greater scores with more turns")

if __name__ == "__main__":main()
