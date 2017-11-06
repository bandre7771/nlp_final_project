import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
from nltk.tag.stanford import StanfordPOSTagger

def splitFile(fileName):
	text = ""
	input_file = open(fileName, "r")
	for line in input_file:
		text += line

	articles = text.split("DEV-")

	i = 1
	for article in articles:
		if len(article.strip()) > 0:
			#print(nltk.pos_tag(word_tokenize(atricle.lower())))
			print(i)
			# print(parseInput(article))
			posInput(article)

			i += 1

def parseInput(text):

	st = StanfordNERTagger('./stanford-ner/classifiers/english.all.3class.distsim.crf.ser.gz',
						   './stanford-ner/stanford-ner.jar',
						   encoding='utf-8')

	tokenized_text = word_tokenize(text)
	classified_text = st.tag(tokenized_text)

	print (classified_text)

def posInput(text):
	path_to_model = "./stanford-postagger/models/english-caseless-left3words-distsim.tagger"
	path_to_jar = "./stanford-postagger/stanford-postagger.jar"
	tagger=StanfordPOSTagger(path_to_model, path_to_jar)
	tagger.java_options='-mx4096m'          ### Setting higher memory limit for long sentences
	# sentence = 'THIS IS TESTING'
	print tagger.tag(word_tokenize(text))


splitFile("sample-textfile.txt")
# posInput("")
#print(nltk.pos_tag(word_tokenize("SIX PEOPLE WERE KILLED AND FIVE WOUNDED TODAY IN A BOMB ATTACK THAT DESTROYED A PEASANT HOME IN THE TOWN OF QUINCHIA,  ABOUT  300  KM  WEST  OF  BOGOTA,  IN  THE  COFFEE-GROWING  DEPARTMENT OF RISARALDA, QUINCHIA MAYOR SAUL BOTERO HAS REPORTED.".lower())))
