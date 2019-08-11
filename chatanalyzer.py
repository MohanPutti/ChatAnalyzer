import nltk.corpus
from nltk.text import Text
f=open('pandii.txt',encoding="utf8")
raw=f.read()
#print(raw)

#sentences of file 

sentences=nltk.sent_tokenize(raw)
'''print(sentences)'''
#---words----
''''
words=[nltk.word_tokenize(sent) for sent in sentences]
print(words)'''
t=nltk.tokenize.WhitespaceTokenizer()
c=Text(t.tokenize(raw))
#print(c)
#---concordance---
'''print(c.concordance('hey'))'''
print(len(raw))
print(len(set(raw)))
'''print(c.similar('hey'))'''
#c.dispersion_plot(["pandii", "hii", "piking"])
print(c.count('pandii'))
fdist=nltk.FreqDist(c)
print(fdist)
voc=fdist.keys()
print(voc)
print(fdist['pandii'])
fdist.plot(100,cumulative=True)
