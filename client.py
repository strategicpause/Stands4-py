from Stands4 import *

if __name__ == "__main__":
	word = "test"
	key = ""
	stands4 = Stands4(key)
	w = stands4.getWord(word)
	print w.word
	print w.definitions