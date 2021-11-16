from lib import *
from math import sqrt
import sys

errors = {
	1:"more deffinitions than possible!",
	2:"Var Reference [%s] Not Found In Memory [%s]",
	3:"can't compute operation \"%s\"",
	4:"can't find external Reference \"%s\"",
}

def panic(ecode, *args):
	msg = errors[ecode]
	if args:
		msg = msg % args
	sys.stderr.write(msg+'\n')
	sys.exit(ecode)

def main():
	#Intro:
	print("*************************************")
	print("		 Welcome to the Calculator		")
	print("*************************************")
	print()

	mem = {}
	while True:
		op = input('>')
		if op in ["exit", "break", "quit"]:break
		memname = "\x00" # \x00 not "inputable"

		if '=' in op: # mem def
			if op.count('=') != 1:
				panic(1)
			memname, op = op.split('=')
			op = op.strip()
			memname = memname.strip()

		if '{' in op: # if var replace
			op = SplitBracket(op, '{')
			for opi in range(len(op)): # "3{x}5" -> ['3', 'x', '5']
				if opi%2: # get every OTHER var (if in {} index will be even)
					if not op[opi] in mem.keys():
						panic(2, (op[opi], (mem if len(mem) < 20 else "mem size too big")))
					if op[opi] in mem.keys():
						op[opi] = mem[op[opi]]

			op = ''.join(op)
		# op now is just numbers and +-... symbols
		try:
			try:
				evldop = eval(op)
			except SyntaxError:
				panic(3, op)
		except NameError:
			panic(4, op)
		if memname == "\x00":
			print(evldop)
		else:
			mem[memname] = str(evldop)


if __name__ == "__main__":main()
