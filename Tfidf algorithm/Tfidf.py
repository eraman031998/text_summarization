#Text Summarization using Tf-idf algorithm
import nltk
import re
import math
import operator
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
Stopwords = set(stopwords.words('english'))
wordlemmatizer = WordNetLemmatizer()

def lemmatize_words(words):
    lemmatized_words = []
    for word in words:
       lemmatized_words.append(wordlemmatizer.lemmatize(word))
    #print('Lemmatized words \n', lemmatized_words)
    return lemmatized_words

def remove_special_characters(text):  #removes special characters from original text
    regex = r'[^a-zA-Z0-9\s]'
    text = re.sub(regex,'',text)
   # print('Removing special characters: \n', text)
    return text

def freq(words): #passing lemmatized words
    words = [word.lower() for word in words]
    dict_freq = {}
    words_unique = []
    for word in words:
       if word not in words_unique:
           words_unique.append(word)
    for word in words_unique:
       dict_freq[word] = words.count(word)
    #print(dict_freq)
    return dict_freq

def pos_tagging(text): #passing 1 sentence at a time
    pos_tag = nltk.pos_tag(text.split())
    #print(pos_tag) first prints the word along with the tag
    pos_tagged_noun_verb = []
    for word,tag in pos_tag: #then stores words with only these tags
        if tag == "NN" or tag == "NNP" or tag == "NNS" or tag == "VB" or tag == "VBD" or tag == "VBG" or tag == "VBN" or tag == "VBP" or tag == "VBZ":
             pos_tagged_noun_verb.append(word)
    return pos_tagged_noun_verb

def tf_score(word,sentence): #passing a word and the sentence containing that word
    word_frequency_in_sentence = 0 #calculating word freq in that sentence
    len_sentence = len(sentence)
    for word_in_sentence in sentence.split():
        if word == word_in_sentence:
            word_frequency_in_sentence = word_frequency_in_sentence + 1
    tf =  word_frequency_in_sentence/ len_sentence
    return tf

def idf_score(no_of_sentences,word,sentences): #calculates no. of sentence containing that word
    no_of_sentence_containing_word = 0
    for sentence in sentences:
        sentence = remove_special_characters(str(sentence))
        sentence = re.sub(r'\d+', '', sentence)
        sentence = sentence.split()
        sentence = [word for word in sentence if word.lower() not in Stopwords and len(word)>1]
        sentence = [word.lower() for word in sentence]
        sentence = [wordlemmatizer.lemmatize(word) for word in sentence]
        if word in sentence: #checking that word in each sentence
            no_of_sentence_containing_word = no_of_sentence_containing_word + 1
    idf = math.log10(no_of_sentences/no_of_sentence_containing_word)
    return idf

def tf_idf_score(tf,idf):
    return tf*idf

def word_tfidf(dict_freq,word,sentences,sentence):
    word_tfidf = []
    tf = tf_score(word,sentence)
    idf = idf_score(len(sentences),word,sentences)
    tf_idf = tf_idf_score(tf,idf)
    return tf_idf

def sentence_importance(sentence,dict_freq,sentences): #passing each sentence,  word frequency and tokenized sentences
     sentence_score = 0
     sentence = remove_special_characters(str(sentence)) #removing special characters from each sentence
     sentence = re.sub(r'\d+', '', sentence) #removing digits
     pos_tagged_sentence = []
     no_of_sentences = len(sentences)
     pos_tagged_sentence = pos_tagging(sentence) #tagging each word in the sentence
     for word in pos_tagged_sentence:
          if word.lower() not in Stopwords and word not in Stopwords and len(word)>1:
                word = word.lower()
                word = wordlemmatizer.lemmatize(word)
                sentence_score = sentence_score + word_tfidf(dict_freq,word,sentences,sentence)
     #print(sentence_score)
     return sentence_score


file = 'msft.txt'
file = open(file , 'r')
text = file.read()
from nltk.tokenize import sent_tokenize,word_tokenize
tokenized_sentence = sent_tokenize(text)
#print('Printing tokenized sentence: \n',tokenized_sentence)
text = remove_special_characters(str(text))
text = re.sub(r'\d+', '', text) #removing digits
#print('After removing digits \n',text)
tokenized_words_with_stopwords = word_tokenize(text)
#print('Tokenized words with stopwords \n', tokenized_words_with_stopwords)
tokenized_words_with_stopwords = [word.lower() for word in tokenized_words_with_stopwords]
tokenized_words = [word for word in tokenized_words_with_stopwords if word not in Stopwords] #removing stopwords

tokenized_words = lemmatize_words(tokenized_words)#lemmitization of tokenized words
word_freq = freq(tokenized_words)
input_user = int(input('Percentage of information to retain(in percent):'))
no_of_sentences = int((input_user * len(tokenized_sentence))/100)
print(no_of_sentences)

#calc sentence score for each sentence
c = 1
sentence_with_importance = {}
for sent in tokenized_sentence: #taking each sentence from the tokenized sentence
    sentenceimp = sentence_importance(sent,word_freq,tokenized_sentence)
    sentence_with_importance[c] = sentenceimp
    c = c+1

sentence_with_importance = sorted(sentence_with_importance.items(), key=operator.itemgetter(1),reverse=True) #sorting with score in descending order
#print(sentence_with_importance)
cnt = 0
summary = []
sentence_no = []
for word_prob in sentence_with_importance:
    #print('Word prob',word_prob)
    if cnt < no_of_sentences:
        sentence_no.append(word_prob[0])
        cnt = cnt+1
    else:
      break
sentence_no.sort()

cnt = 1
for sentence in tokenized_sentence:
    if cnt in sentence_no:
       summary.append(sentence)
    cnt = cnt+1
summary = " ".join(summary)
print("\n")
print("Summary:")
print(summary)


