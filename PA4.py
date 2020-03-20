"""
Program to predict the sentiment of input text as either positive, neagtive or neutral.
"""

def read_sentiment_words(filename):
    """
    Read the input text file line by line and 
    return the dictionary of words with their value set to zero.
    Output format example: {'orange':0, 'banana':0,...}
    """
    sentiment = open(filename, 'r')
    lines = sentiment.readlines()
    Dict = {}
    for w in lines:
        if w not in Dict:
            w = w[:-1]
            Dict[w] = 0
        else:
            continue
    sentiment.close()
    return Dict

positive_words = read_sentiment_words('positive-words.txt')
negative_words =  read_sentiment_words('negative-words.txt')
def read_sentences(filename):
    """
    Read the input text file line by line and
    return the data as a list of list.
    Output format example: [['1', 'hello , how are you?'], ['2', 'have a great day !'], ...]
    """
    files = open(filename, 'r')
    lines = files.readlines()
    sentenceLst = []
    mainList = []
    w = 1
    for i in lines:
        sentenceLst.append(str(w))
        w = w + 1
        sentenceLst.append(i.lower())
        mainList.append(sentenceLst)
        sentenceLst = []
    return mainList
def listOfPositiveWords():
    postiveList = {}
    for i in read_sentiment_words('positive-words.txt'):
        postiveList[i] = 0
    return postiveList
def listOfNegativeWords():
    negativeList = {}
    for i in read_sentiment_words('negative-words.txt'):
        negativeList[i] = 0
    return negativeList
posWords = listOfPositiveWords()
negWords = listOfNegativeWords()
def write_sentiments(filename, sentence_sentiment_lst):
    """
    Write a list of lists of review text sentiment values to file.
    The sentence index and the sentiment value must be separated by comma.
    Example Input: sentence_sentiment_lst = [['1', 'positive'], ['2', 'negative'],...]
    Output File format: lastname_firstname_sentiments.txt

    """

    sentiFile = open(filename, 'w+')
    reviewFile = open(sentence_sentiment_lst, 'r')
    lines = reviewFile.readlines()
    p = 1
    for line in lines:
        line.lower()
        sentimentCount = 0
        words = line.split("\t")[1]
        words = words.lower()
        for w in words.split():
            w = w.lower()
            if w in posWords:
                sentimentCount += 1
                posWords[w] += 1
            elif w in negWords:
                sentimentCount += -1
                negWords[w] += 1
        if sentimentCount > 0:
            sentiFile.write(str(p) + ", " + "positive" + "\n")
            p += 1
        elif sentimentCount < 0:
            sentiFile.write(str(p) + ", " + "negative" + "\n")
            p += 1
        else:
            sentiFile.write(str(p) + ", " + "neutral" + "\n")
            p += 1
    reviewFile.close()
    sentiFile.close()
    return sentiFile





def  write_sentiment_words(filename, top_words_frequency_lst):
    """
    Write the word and frequency value for top 5 (no top 2 one negative one positive) sentiment words to file separated by comma.
    Output File format: lastname_firstname_sentiment_words.txt
  """
    wordsFile = open(filename, 'w+')
    comparisonlist = open(top_words_frequency_lst, 'r')
    maxPosNum = 0
    maxNegNum = 0
    for x in posWords:
        if posWords[x] > maxPosNum:
            maxPosNum = posWords[x]
            maxPosWord = x
    for x in negWords:
        if negWords[x] > maxNegNum:
            maxNegNum = negWords[x]
            maxNegWord = x
    wordsFile.write(maxPosWord + ", " + str(maxPosNum) + "\n")
    wordsFile.write(maxNegWord + ", " + str(maxNegNum) + "\n")
    comparisonlist.close()
    wordsFile.close()
    return wordsFile



def predict_sentiment(review_text):
    """
    Find the sentiment of the review text, based on the sentiment of each word in the text.
    Return "postive", "negative", or "neutral" depending on the total sentiment word count value.
    """
    reviewFile = open(review_text, 'r')
    lines = reviewFile.readlines()
    sentimentCount = 0
    for line in lines:
        words = line.split("\t")[1]
        for w in words.split():
            w.lower()
            if w in posWords:
                sentimentCount += 1
            elif w in negWords:
                sentimentCount += -1
            else:
                sentimentCount += 0
    if sentimentCount == 0:
        return 'neutral'
    if sentimentCount > 0:
        return 'positive'
    if sentimentCount < 0:
        return 'negative'
    reviewFile.close()
    #Your code here

def most_frequent_sentiment_word():
    """
    Find the word with the highest frequency value from the dictionary and
    return the word and it's frequency.
    """
    ''' #############
       *******************
        Deepthi says to return the top positive and 
        the top negative words and their frequencies
        I did it a little differently because nothing needs to be passed through 
        function however I left the pre-written parameter there just to avoid making any changes
        
        
        
        SO my code returns the max negative and max positive words in one list. it does not require any 
        additional input, there are no parameters involved.*****'''



    """ ##########################################"""



    MaxList = []
    maxPosNum = 0
    maxNegNum = 0
    postiivesList = []
    negatiiveList = []

    for x in posWords:
        if posWords[x] > maxPosNum:
            maxPosNum = posWords[x]
            maxPosWord = x
    for x in negWords:
        if negWords[x] > maxNegNum:
            maxNegNum = negWords[x]
            maxNegWord = x
    postiivesList.append(maxPosNum)
    postiivesList.append(maxPosWord)
    negatiiveList.append(maxNegNum)
    negatiiveList.append(maxNegWord)
    MaxList.append("Most positive: ")
    MaxList.append(postiivesList)
    MaxList.append("Most negative: ")
    MaxList.append(negatiiveList)
    return MaxList



def main():
    read_sentences('sentences.tsv')
    write_sentiments('Ahmed_Awais_sentiments.txt', 'sentences.tsv')
    write_sentiment_words('Ahmed_Awais_sentiment_words.txt', 'sentences.tsv')
    print(predict_sentiment('sentences.tsv'))
    print(most_frequent_sentiment_word())

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
# My most_frequent_sentiment does not require any arguments!! It automatically returns the most frequent #
# positive and negative words !!                                                                         #
###########################################################################################################


#    reviews = #read reviews from file


if __name__ == '__main__':
    main()
