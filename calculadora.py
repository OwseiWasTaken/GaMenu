from lib import *
from math import sqrt

#TODO panic &{}() system

def main():
	#Intro:
	print("*************************************")
	print("		 Welcome to the Calculator		")
	print("*************************************")
	print()

	mem = {}
	while True:
		op = input('>')
		memname = "\x00" # \x00 not "inputable"

		if '=' in op: # mem def
			assert op.count('=') == 1, "more deffinitions than possible!"
			memname, op = op.split('=')
			op = op.strip()
			memname = memname.strip()

		if '{' in op: # if var replace
			op = SplitBracket(op, '{')
			for opi in range(len(op)): # "3{x}5" -> ['3', 'x', '5']
				if opi%2: # get every OTHER var (if in {} index will be even)
					assert op[opi] in mem.keys(), "Var Reference [%s] Not Found In Memory [%s]" % (op[opi], (mem if len(mem) < 20 else "mem size too big"))
					if op[opi] in mem.keys():
						op[opi] = mem[op[opi]]

			op = ''.join(op)
		# op now is just numbers and +-... symbols
		try:
			try:
				evldop = eval(op)
			except SyntaxError:
				assert 0, "can't compute operation \"%s\"" % op
		except NameError:
			assert 0, "can't find external Reference \"%s\"" % op
		if memname == "\x00":
			print(evldop)
		else:
			mem[memname] = str(evldop)


if __name__ == "__main__":main()
