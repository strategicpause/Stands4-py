import urllib
from xml.dom.minidom import parseString

class Stands4:
	def __init__(self, key):
		self.key = key
	
	def getWord(self, word):
		xml = self.__getXML(word)
		definitions = self.__getDefinitions(xml)
		return Word(word, definitions)
		
		
	def __getXML(self, word):
			url = "http://www.abbreviations.com/services/v1/syno.aspx?tokenid=" + self.key + "&word=" + word
			xml = urllib.urlopen(url).read()
			return parseString(xml)
			
	def __getDefinitions(self, xml):
		results = xml.getElementsByTagName('result')
		definitions = []
		for result in results:
			definition = result.getElementsByTagName('definition')[0].childNodes[0].data
			partofspeach = result.getElementsByTagName('partofspeach')[0].childNodes[0].data
			definitions += [Definition(definition, partofspeach)]
		return definitions
	
class Definition:
	def __init__(self, definition, partofspeach = ""):
		self.definition = definition
		self.partofspeach = partofspeach
	def __str__(self):
		return self.partofspeach + ": " + self.definition
	def __repr__(self):
		return self.__str__()
		
class Word:
	def __init__(self, word, definitions):
		self.word = word
		self.definitions = definitions