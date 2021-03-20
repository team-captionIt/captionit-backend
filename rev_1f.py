import pandas as pd

"This is my code"
import spacy

nlp = spacy.load('en_core_web_sm')
stopwords = spacy.lang.en.stop_words.STOP_WORDS
doc = "close-up"
p_doc = nlp(doc)

keywords = []
keywordslist = []
keywordslist1 = []

for token in p_doc:
    keywordslist.append((token,token.pos_))
    if token.lemma_ not in keywords:
        if not token.is_stop:
            keywords.append(token.lemma_)




for token in p_doc:
	if token.pos_ == 'NOUN' :
		keywordslist1.append(token)

try:
        for i in range(0,len(keywordsunique)):
                print(keywords[i])
except:
        pass

df = pd.read_csv("C:/quotes1.csv")
df.dropna(inplace = True)
df.drop(296,axis = 0, inplace = True)
keywords1 = ['dance','heaven','hurt','life']
keywordsxxx = ['abandon',
 'afterlife',
 'bereavement',
 'celebrate',
 'celebration',
 'dance',
 'dancing',
 'death',
 'death-poems',
 'deceased',
 'departure',
 'drunk',
 'dying',
 'end',
 'eternal',
 'stars',
 'swallowed',
 'truth',
 'union',
 'unity',
 'universe',
 'witness']
category = df['category']
quote = df['quote']
author = df['author']
def search(keywords):
    global found_keywords
    found_keywords = {}
    global inot
    inot = []
    for i in range(1, len(keywords)+1):
        found_keywords[i] = []
    for i in range(0,497898):
        c= 0
        for j in keywords:
            try:
                for k in list(str(category[i]).split(', ')):
                    if j == k: 
                        c +=1
                        break
            except:
                inot.append(i)
        """if c == 3:
            print(c)"""
        if c != 0 :
            found_keywords[c].append(i)

search(keywords)
print(keywords)
print(len(keywords))
print(len(inot))
print(found_keywords)
"""print(found_keywords[3])"""

try:
    for i in range(1,5):
        for j in range(0,5):
            print(found_keywords[i][j])
            print(category[found_keywords[i][j]])
            print(quote[found_keywords[i][j]] + "      -by  "+author[found_keywords[i][j]])
except:
    pass
