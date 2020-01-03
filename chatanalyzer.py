import nltk.corpus
import re
from nltk.text import Text
from nltk.tokenize import LineTokenizer
class Mychat:
	def __init__(self,file):
		self.myfile=file
		self.raw=""
	def openFile(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
	def printRaw(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		print(raw)
	def printSentences(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		sentences=LineTokenizer(blanklines='keep').tokenize(raw)
		print(sentences)
	def printWords(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		sentences=nltk.sent_tokenize(raw)
		words=[nltk.word_tokenize(sent) for sent in sentences]
		print(words)
	def printConcordance(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		t=nltk.tokenize.WhitespaceTokenizer()
		c=Text(t.tokenize(raw))
		print(c.concordance('ha'))
	def printLengths(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		print("total words used are",len(raw))
		print("total words with out repitition are",len(set(raw))) 
	def dispersionPlot(self,word1,word2,word3):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		t=nltk.tokenize.WhitespaceTokenizer()
		c=Text(t.tokenize(raw))
		c.dispersion_plot([word1, word2, word3])
	def countTheWord(self,word):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		t=nltk.tokenize.WhitespaceTokenizer()
		c=Text(t.tokenize(raw))
		print(c.count(word),'Number of times',word,'has been used')
	def freqDistribution(self):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		t=nltk.tokenize.WhitespaceTokenizer()
		c=Text(t.tokenize(raw))
		fdist=nltk.FreqDist(c)
		voc2=fdist.items()
		print('All words with their frequencies',voc2)
		print('The word with most frequency',fdist.max())
	def freqDist(self,word):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		t=nltk.tokenize.WhitespaceTokenizer()    #Same functionality as countTheWord() 
		c=Text(t.tokenize(raw))
		fdist=nltk.FreqDist(c)
		print(fdist[word])
	def visualize(self,number):
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		t=nltk.tokenize.WhitespaceTokenizer()
		c=Text(t.tokenize(raw))
		fdist=nltk.FreqDist(c)
		fdist.plot(number)
	def visWithoutDate(self,number):
		sp=[]
		x=input('enter friend name')
		y=input('enter your name')
		name_pattern="\d*\/\d*\/\d*, \d*:\d*\s-\s("+x+": |"+y+": )|<Media omitted>|\.|\-"
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		sentences=LineTokenizer(blanklines='keep').tokenize(raw)
		for i in sentences:
			sp.append(re.sub(name_pattern,'',i))
		print(sp)
		myplot=nltk.FreqDist(sp)
		myplot.plot(number)
	def  sentOnDate(self,day,month,year):
		sp=[]
		y="/"
		name_pattern=str(month)+y+str(day)+y+str(year)
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		sentences=LineTokenizer(blanklines='keep').tokenize(raw)
		for i in sentences:
			if(re.search(name_pattern,i)):
				print(i)
	def  visualOnDay(self,day,month,year,number):
		sp=[]
		y="/"
		sp2=[]
		p=input('enter friend name')
		k=input('enter your name')
		date_pattern=str(month)+y+str(day)+y+str(year)
		f=open(self.myfile,encoding="utf8")
		raw=f.read()
		sentences=LineTokenizer(blanklines='keep').tokenize(raw)
		for i in sentences:
			if(re.search(date_pattern,i)):
				sp.append(i)
		pattern2="\d*\/\d*\/\d*, \d*:\d*\s-\s("+p+": |"+k+": )|<Media omitted>|\.|\-|\s"
		for i in sp:
			sp2.append(re.sub(pattern2,'',i))
		myplot=nltk.FreqDist(sp2)
		myplot.plot(number)

x=Mychat('anna.txt') 
#x.openFile()
#x.printRaw()
#x.printSentences()
#x.printWords()
#x.printConcordance()
#x.printLengths()

'''word1=input('enter word1')
word2=input('enter word2')
word3=input('enter word3') 
x.dispersionPlot(word1,word2,word3)'''


#word4=input('enter a word to be counted')
#x.countTheWord(word4)
#x.freqDistribution()
#x.freqDist('chep')
'''num=int(input('enter number of frequent words you wish to visualize'))
x.visualize(num)'''

num2=int(input('enter number of frequent words you wish to visualize'))
x.visWithoutDate(num2)

'''day=int(input('enter day'))
month=int(input('enter month with non zero for single digit months'))
year=int(input('enter year last two digits'))'''

#x.sentOnDate(day,month,year)
'''day=int(input('enter day'))
month=int(input('enter month with non zero for single digit months'))
year=int(input('enter year last two digits'))	
num_on_date=int(input('enter num for frequent words'))
x.visualOnDay(day,month,year,num_on_date)'''
