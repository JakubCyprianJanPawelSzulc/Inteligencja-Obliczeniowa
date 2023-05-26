def categorize(data):
    positiveTweets = []
    negativeTweets = []

    for tweet, sentiment_scores, emotions in data:
        compound_score = sentiment_scores['compound']
        if compound_score > 0.05:
            positiveTweets.append(tweet)
        elif compound_score < -0.05:
            negativeTweets.append(tweet)
    
    return positiveTweets, negativeTweets


def saveBothToFiles(positiveTweets, negativeTweets, filename1, filename2):
    with open(filename1, "w", encoding="utf-8") as file:
        file.writelines("\n".join(positiveTweets))

    with open(filename2, "w", encoding="utf-8") as file:
        file.writelines("\n".join(negativeTweets))



def main():
    with open("sentimentScoresIsrael.txt", "r", encoding="utf-8") as file:
        dataIsrael = file.readlines()
    with open("sentimentScoresPalestine.txt", "r", encoding="utf-8") as file:
        dataPalestine = file.readlines()
    positiveTweetsIsrael, negativeTweetsIsrael = categorize(dataIsrael)
    saveBothToFiles(positiveTweetsIsrael, negativeTweetsIsrael, "positiveTweetsIsrael.txt", "negativeTweetsIsrael.txt")
    positiveTweetsPalestine, negativeTweetsPalestine = categorize(dataPalestine)
    saveBothToFiles(positiveTweetsPalestine, negativeTweetsPalestine, "positiveTweetsPalestine.txt", "negativeTweetsPalestine.txt")

if __name__ == '__main__':
    main()




