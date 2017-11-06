import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

def splitFile(fileName):
	text = ""
	input_file = open(fileName, "r")
	for line in input_file:
		text += line

	articles = text.split("DEV-")
	
	i = 1
	for atricle in articles:
		if len(atricle.strip()) > 0:
			#print(nltk.pos_tag(word_tokenize(atricle.lower())))
			print(i)
			print(parseInput(atricle))
			i += 1 

def parseInput(text):

	st = StanfordNERTagger('./stanford-ner/classifiers/english.all.3class.caseless.distsim.crf.ser.gz',
						   './stanford-ner/stanford-ner.jar',
						   encoding='utf-8')

	tokenized_text = word_tokenize(text)
	classified_text = st.tag(tokenized_text)

	print (classified_text)


splitFile("sample-textfile.txt")
#print(nltk.pos_tag(word_tokenize("SIX PEOPLE WERE KILLED AND FIVE WOUNDED TODAY IN A BOMB ATTACK THAT DESTROYED A PEASANT HOME IN THE TOWN OF QUINCHIA,  ABOUT  300  KM  WEST  OF  BOGOTA,  IN  THE  COFFEE-GROWING  DEPARTMENT OF RISARALDA, QUINCHIA MAYOR SAUL BOTERO HAS REPORTED.".lower())))