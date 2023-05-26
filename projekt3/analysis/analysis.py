from nltk.sentiment.vader import SentimentIntensityAnalyzer
from text2emotion import get_emotion

def analyzeSentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentimentScores = sid.polarity_scores(text)
    return sentimentScores

def getFile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        tweets = file.readlines()
    return tweets

def analyzeEmotions(text):
    emotions = get_emotion(text)
    return emotions

def analyzeFile(filename):
    tweets = getFile(filename)
    sentimentScores = [analyzeSentiment(tweet) for tweet in tweets]
    emotions = [analyzeEmotions(tweet) for tweet in tweets]
    return sentimentScores, emotions

sentimentScores1, emotions1 = analyzeFile("../preprocessing/preprocessedIsrael.txt")
sentimentScores2, emotions2 = analyzeFile("../preprocessing/preprocessedPalestine.txt")

print("Izrael:")
print("Pozytywność:", sum([score['pos'] for score in sentimentScores1]) / len(sentimentScores1))
print("Negatywność:", sum([score['neg'] for score in sentimentScores1]) / len(sentimentScores1))
print("Neutralność:", sum([score['neu'] for score in sentimentScores1]) / len(sentimentScores1))
print("Wynik zagregowany (compound):", sum([score['compound'] for score in sentimentScores1]) / len(sentimentScores1))

print("Palestyna:")
print("Pozytywność:", sum([score['pos'] for score in sentimentScores2]) / len(sentimentScores2))
print("Negatywność:", sum([score['neg'] for score in sentimentScores2]) / len(sentimentScores2))
print("Neutralność:", sum([score['neu'] for score in sentimentScores2]) / len(sentimentScores2))
print("Wynik zagregowany (compound):", sum([score['compound'] for score in sentimentScores2]) / len(sentimentScores2))

print("Izrael:")
for emotion, value in sum(emotions1).items():
    print(emotion.capitalize(), ":", value)

print("Palestyna:")
for emotion, value in sum(emotions2).items():
    print(emotion.capitalize(), ":", value)
