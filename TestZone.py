from lib import *
import unittest

# in a unittest.TestCase class
#	self.assertEqual('foo'.upper(), 'FOO')
#	self.assertTrue('FOO'.isupper())
#	self.assertFalse('Foo'.isupper())

def example():
	# def testing func/class
	def SplitString(line:str, sep:str = " ", quote:str = '"', escape ='\\', MaintainQuotes:bool = True) -> list[str]:
		# 'hello my "cool friend" man!' -> ['hello', 'my', '"coll friend"', 'man!']
		InString = False
		ret:list[str] = []
		now = ""
		for pos in r(line):
			char = line[pos]
			if char == quote and pos > 0 and line[pos-1] != escape:
				if MaintainQuotes:now+='"'
				InString = not InString
			else:
				# " start or end string
				if char == sep and not InString:
					ret.append(now)
					now = ""
				else:
					now += line[pos]
		if now:ret.append(now)
		return ret
	# def tester class
	class Tester(unittest.TestCase):
		"""Tester""" # add this for class name
		def TestSplitString(this):
			# 'hello my "cool friend" man!' -> ['hello', 'my', '"coll friend"', 'man!']
			string = 'hello my "cool friend" man!'
			this.assertEqual(
				SplitString(string),
				['hello', 'my', '"cool friend"', 'man!']
			)
			string = 'hello my cool friend man!'
			this.assertEqual(
				SplitString(string),
				['hello', 'my', 'cool', 'friend', 'man!']
			)
	# TestAll(tester classes)
	TestAll(Tester)

def TestAll(cls):
	if type(cls) == type(int): # type type
		cls = cls()

	clsname = cls.__doc__

	funcs = dir(cls) # get all vars
	testfuncs = []
	for i in r(funcs):
		if funcs[i].startswith("Test"): # get Test... var (test func)
			testfuncs.append(eval(f"cls.{funcs[i]}")) # get func by name
	for func in testfuncs:
		func()
	if clsname:
		print(f"all tests for \"{clsname}\" passed")

def main():
	example()
	pass

if __name__ == "__main__":main()
