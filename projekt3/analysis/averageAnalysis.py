import ast
import matplotlib.pyplot as plt

def parseSentimentScores(line):
    sentiment_start = line.index("{'neg':")
    sentiment_end = line.index("},") + 1
    emotions_start = line.index("{", sentiment_end)
    emotions_end = line.index("};", emotions_start) + 1

    sentiment_scores = ast.literal_eval(line[sentiment_start:sentiment_end])
    emotions = ast.literal_eval(line[emotions_start:emotions_end])

    return sentiment_scores, emotions

def parseData(file):
    data = []
    for line in file:
        line = line.strip()
        if line:
            tweet_end = line.index(",")
            tweet = line[:tweet_end]
            scores, emotions = parseSentimentScores(line)
            data.append((tweet, scores, emotions))
    return data

def calculateAverageScores(data):
    avgScores = {
        'neg': 0,
        'neu': 0,
        'pos': 0,
        'compound': 0
    }
    avgEmotions = {
        'Happy': 0,
        'Angry': 0,
        'Surprise': 0,
        'Sad': 0,
        'Fear': 0
    }

    numOpinions = len(data)
    for i in range(numOpinions):
        _, scores, emotions = data[i]
        for key in avgScores:
            avgScores[key] += scores[key] / numOpinions
        for key in avgEmotions:
            avgEmotions[key] += emotions[key] / numOpinions

    return avgScores, avgEmotions

def main():
    with open("sentimentScoresIsrael.txt", "r", encoding="utf-8") as file:
        dataIsrael = parseData(file)
        avgScoresIsrael, avgEmotionsIsrael = calculateAverageScores(dataIsrael)
        print("Average Sentiment Scores - Israel:")
        print(avgScoresIsrael)
        print("Average Emotions - Israel:")
        print(avgEmotionsIsrael)

    with open("sentimentScoresPalestine.txt", "r", encoding="utf-8") as file:
        dataPalestine = parseData(file)
        avgScoresPalestine, avgEmotionsPalestine = calculateAverageScores(dataPalestine)
        print("Average Sentiment Scores - Palestine:")
        print(avgScoresPalestine)
        print("Average Emotions - Palestine:")
        print(avgEmotionsPalestine)

if __name__ == '__main__':
    main()
