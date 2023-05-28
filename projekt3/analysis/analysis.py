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
    sentimentScores = []
    emotions = []
    text = []
    for tweet in tweets:
        if tweet == '\n':
            continue
        if tweet[-1]=='\n':
            tweet = tweet[:-1]
        sentimentScores.append(analyzeSentiment(tweet))
        emotions.append(analyzeEmotions(tweet))
        text.append(tweet)

    return sentimentScores, emotions, text

def main():
    sentimentScores1, emotions1, text1 = analyzeFile("../preprocessing/preprocessedIsrael.txt")
    with open("sentimentScoresIsrael.txt", "w", encoding="utf-8") as file:
        for i in range(len(text1)):
            file.write(str(text1[i])+", "+str(sentimentScores1[i])+", "+str(emotions1[i])+";"+'\n')


    sentimentScores2, emotions2, text2 = analyzeFile("../preprocessing/preprocessedPalestine.txt")
    with open("sentimentScoresPalestine.txt", "w", encoding="utf-8") as file:
        for i in range(len(text2)):
            file.write(str(text2[i])+", "+str(sentimentScores2[i])+", "+str(emotions2[i])+";"+'\n')

if __name__ == "__main__":
    main()