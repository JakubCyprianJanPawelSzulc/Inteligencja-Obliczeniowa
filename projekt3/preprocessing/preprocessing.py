import re
from nltk.tokenize import word_tokenize
import nltk

def preprocessTweet(tweet):
    tweet = re.sub(r'^\d{4}-\d{2}-\d{2}, ', '', tweet)
    tweet = re.sub(r'#', '', tweet)
    tweet = re.sub(r'@\w+', '', tweet)
    tweet = re.sub(r'https?://\S+', '', tweet)
    tweet = tweet.lower()
    words = tweet.split()
    words = [re.sub(r'&amp;', '', word) for word in words]
    words = [re.sub(r'(?<=\w)[^\s\w](?![^\s\w])', '', word) for word in words]
    words = [re.sub(r'[|«»“”‘’,"–—…-]', '', word) for word in words]
    words = [re.sub(r'\([^)]*\)', '', word) for word in words]
    words = [re.sub(r'\.\.+$', '', word) for word in words]
    words = [re.sub(r'\.', '', word) for word in words]
    words = [re.sub(r'^[\(\[]', '', word) for word in words]
    words = [re.sub(r'[\)\]]$', '', word) for word in words]
    words = [word for word in words if word]
    preprocessedTweet = ' '.join(words)

    stop_words = list(nltk.corpus.stopwords.words('english'))
    words = word_tokenize(preprocessedTweet)
    words = [w for w in words if not w in stop_words]
    preprocessedTweet = ' '.join(words)


    return preprocessedTweet

def saveToFile(filename, tweets):
    with open (filename, "w", encoding="utf-8") as file:
        for tweet in tweets:
            file.write(tweet + "\n")

def getFile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        tweets = file.readlines()
    return tweets

def preprocessFile(filename):
    tweets = getFile(filename)
    preprocessedTweets = [preprocessTweet(tweet) for tweet in tweets]
    return preprocessedTweets

def main():
    saveToFile("preprocessedIsrael.txt", preprocessFile("../download/tweetsIsrael.txt"))
    saveToFile("preprocessedPalestine.txt", preprocessFile("../download/tweetsPalestine.txt"))

if __name__ == '__main__':
    main()
