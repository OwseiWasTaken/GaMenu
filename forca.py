#Intro:
import sys
def main():
	if not "--dev" in sys.argv:
		sys.stderr.write("under dev!\n")
		sys.exit(0x1)
	print("forca.py!")
	input()

if __name__ == "__main__":
	main()
