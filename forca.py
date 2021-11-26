#Intro:
import sys
def main():
	if not "--dev" in sys.argv:
		assert 0, "under dev!"
	print("forca.py!")
	input()

if __name__ == "__main__":
	main()
