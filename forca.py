from lib import *

#Intro:
def main():
	if not "--dev" in argv:
		fprint(stderr, "under dev!\n")
		exit(0x1)
	print("forca.py!")
	input()

if __name__ == "__main__":
	main()
