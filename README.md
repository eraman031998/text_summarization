# Text Summarization
Text summarization is the problem of creating a short, accurate and fluent summary of a longer text document. Automatic text summarization methods are greatly needed to address the ever-growing amount of text data available online to both better help discover relevant information and to consume relevant information faster.
Summarization system often have additional evidence they can utilize in order to specify the most important topics of documents. For example, when summarizing blogs, there are discussions or comments coming after the blog posts that are good sources of information to determine which parts of the blog are critical and interesting. In scientific paper summarization, there is a considerable amount of information such as cited papers and conference papers which can be leveraged to identify important sentences in the original papers.
In this work, I would like to discover the problem of text summarization in natural language processing. Here, I have used one of the various methods used for text summarization.

## TF-IDF  Algorithm
It is one of the simplest approaches for text summarization. I have applied lemmatization and POS tagging on the text and then calculated the TF-IDF score for each sentence. Lemmatization is the process of grouping together the different inflected forms of a word so they can be analyzed as a single item. Lemmatization is similar to stemming but it brings context to the words. Part-of-Speech (POS) tagging is a technique for automatic annotation of lexical categories. Part-of –Speech tagging assigns an appropriate part of speech tag for each word in a sentence of a language. Finally, the scores are normalized by dividing by the length of each sentence. The sentences are sorted based on the TF-IDF score. TF-IDF stands for term frequency-inverse document frequency. It is a numeric measure; it gives a highest score to the word which occurs frequently in the document and a collection of documents. In the end, I have taken the score of the top `n` sentences to create the summary. In this approach we only consider noun and verb for considering the score of sentences so that the important sentences can be extracted to form the summary. This approach gives more accuracy and it also improves the speed of algorithm.

### Note
1.'tfidf.py' is the code written in python for TF-IDF Algorithm.<br/>
2.'text1.txt' is the text file which is to be summarized(you can use other text files too).<br/>
3.When running this code, you will be asked about the percentage of data you want to retain. You have to enter a number between 1 to 100 based on the amount of data you want in your summarization. For better results enter a number greater than or equal to 50.<br/>
4.Rest of information can be found in the code as i have made necessary comments to have a better understanding of the code.<br/>
5.Any pull requests are welcome!<br/>

Thanks!
