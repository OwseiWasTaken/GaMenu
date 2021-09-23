#Intro:
print("*************************************")
print("      Welcome to the Calculator      ")
print("*************************************")
print()

def Valor1() -> int:
	No1 = input("Write the first value: ")
	if not No1.isnumeric():
		print("It needs to be a number...")
		return Valor1()
	else:
		No1 = eval(No1)
		return No1

def Valor2() -> int:
	No2 = input("Write the second value: ")
	if not No2.isnumeric():
		print("It needs to be a number...")
		return Valor2()
	else:
		No2 = eval(No2)
		return No2

def Operacao():
	QualOp = input("What calculation do you wanna do? +, -, *, /, Root or Power? ")
	QualOp = QualOp.upper()
	if QualOp not in ["+", "-", "*", "/", "POWER", "ROOT"]:
		print("+, -, *, /, Root or Power...")
		return Operacao()
	else:
		return QualOp

Op = Operacao()
Var1 = Valor1()
Var2 = Valor2()
Continuar = None

while True:
	if Op == "+":
		total = Var1 + Var2
		print(total)
	elif Op == "-":
		total = Var1 - Var2
		print(total)
	elif Op == "*":
		total = Var1 * Var2
		print(total)
	elif Op == "/":
		total = Var1 / Var2
		print(total)
	elif Op == "POWER":
		total = Var1 ** Var2
		print(total)
	elif Op == "ROOT":
		total = Var1 ** (1/Var2)
		print(total)
	print()

	Continuar = input("Want to do another calculation? 'Y' for yes and 'N' for no: ")

	while True:
		if Continuar not in ["Y", "y", "N", "n"]:
			print("Please, 'Y' or 'N'")
			Continuar = input("'Y' for yes and 'N' for no: ")
		else:
			break

	if Continuar in ["N", "n"]:
		break

	Op = Operacao()
	Var1 = Valor1()
	Var2 = Valor2()