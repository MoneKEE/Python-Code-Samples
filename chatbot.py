'''
Chatbot

A simple retrieval-based chatbot based on python's NLTK library and scikit learn.

It reads in a text file document to create a bag of words.

Pre-processing - Document content is converted to lowercase, then tokenized on at both a word and sentence level.
    Punctuation and stopwords are removed and the resulting corpus is lemmatized.  Lemmatization was chosen over
    stemming in order to avoid introducing non-words into resulting bag of words.

Vectorization - Term frequency-inverse document frequency, or TF-IDF, is employed to counteract an imminent problem
    with the bag of words approach, namely, that highly frequent words start to dominate in the document, but may not
    contain much informational content.  Also, it will give more weight to longer doucments than shorter documents.
    TF-IDF rescales the frequency of words by how often they appear in all documents so that the scores for frequent
    words like "the" that are also frequent across al documents penalized.

    Term Frequency: is a scoring of the frequency of the word in the current document.
        TF = (Number of times term t appears in a document)/(Number of terms in the document)

    Inverse Document Frequency: is a scoring of how rare the word is across documents.
        IDF = 1+Log(N/n), where, N is the number of documents and n is the number documents a term t has appeared in.

    TF-IDF weight is a weight often used in information retrieval and text mining.  This weight is a statistical measure used to
        evaluate how important a word is to a document in a collection or corpus.

        Weight = TF * IDF

Vector Comparison - To find the similarity between between words entered by the user and the words in the corpus.  Cosine similarity
    is a measure of similarity between two non-zero vectors.  If d1 and d2 are two documents:
        Cosine Similarity (d1, d2) = Dot product(d1, d2)/(||d1|| * ||d2||)
'''
import nltk
import numpy as np
import random
import string
import os
from sklearn.feature_extraction.text import TfidfVectorizer
#Tf-Idf -> Term Frequency, Inverse document frequency
#Rescales the frequency of words by how often they appar in all documents so that the scores for 
# frequent words like "the" that are also frequent across all documents are penalized.

from sklearn.metrics.pairwise import cosine_similarity
#Is a measure of similarity between two non-zero vectors.

import warnings
warnings.filterwarnings('ignore')

os.chdir('C:\\Users\\mwill\\AppData\\Roaming\\nltk_data\\corpora\\state_union')

nltk.download('popular', quiet=True)

f=open('2006-GWBush.txt','r',errors='ignore')
raw=f.read()
raw=raw.lower()

sent_tokens=nltk.sent_tokenize(raw)
word_tokens=nltk.word_tokenize(raw)

lemmer=nltk.stem.WordNetLemmatizer()
#WordNet is a semantically-oriented dictionary of English included in NLTK.

stop_words = nltk.corpus.stopwords.words('english')

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens if not token in stop_words]

remove_punct_dict=dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)

GREETING_RESPONSES = ("hi", "hey", "*nods*", "hi there", "hello","I am glad!  You are talking to me")

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)

    TfidfVec=TfidfVectorizer(tokenizer=LemNormalize,stop_words=stop_words)
    tfidf=TfidfVec.fit_transform(sent_tokens)
    vals=cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat=vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry!  I don't understand you"
        return robo_response
    else:
        robo_response=robo_response+sent_tokens[idx]
        return robo_response

flag=True
print("ROBO: My name is Robo.  I will answer your queries about Chatbots.  If you want to exit, type Bye!")

while(flag==True):
    user_response=input()
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("ROBO: You are welcome..")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sent_tokens.remove(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")