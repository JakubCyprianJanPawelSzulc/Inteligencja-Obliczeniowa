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
    averages = []
    num_opinions = len(data)
    for i in range(0, num_opinions, 100):
        start_index = i
        end_index = min(i + 100, num_opinions)
        opinions = data[start_index:end_index]
        avg_scores = {
            'neg': sum(scores['neg'] for _, scores, _ in opinions) / len(opinions),
            'neu': sum(scores['neu'] for _, scores, _ in opinions) / len(opinions),
            'pos': sum(scores['pos'] for _, scores, _ in opinions) / len(opinions),
            'compound': sum(scores['compound'] for _, scores, _ in opinions) / len(opinions)
        }
        averages.append(avg_scores)
    return averages

def plotAverageScores(averages, title):
    days = range(1, len(averages) + 1)
    neg_scores = [avg_scores['neg'] for avg_scores in averages]
    neu_scores = [avg_scores['neu'] for avg_scores in averages]
    pos_scores = [avg_scores['pos'] for avg_scores in averages]
    compound_scores = [avg_scores['compound'] for avg_scores in averages]

    plt.plot(days, neg_scores, label='Negative')
    plt.plot(days, neu_scores, label='Neutral')
    plt.plot(days, pos_scores, label='Positive')
    plt.plot(days, compound_scores, label='Compound')

    plt.xlabel('Days')
    plt.ylabel('Average Scores')
    plt.title(title)
    plt.legend()
    plt.show()

def main():
    with open("sentimentScoresIsrael.txt", "r", encoding="utf-8") as file:
        dataIsrael = parseData(file)
        averagesIsrael = calculateAverageScores(dataIsrael)
        plotAverageScores(averagesIsrael, 'Sentiment Analysis - Israel')

    with open("sentimentScoresPalestine.txt", "r", encoding="utf-8") as file:
        dataPalestine = parseData(file)
        averagesPalestine = calculateAverageScores(dataPalestine)
        plotAverageScores(averagesPalestine, 'Sentiment Analysis - Palestine')

if __name__ == '__main__':
    main()
