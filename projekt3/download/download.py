import snscrape.modules.twitter as sntwitter
from datetime import datetime, timedelta

hashtag = "israel"
hashtag2 = "palestine"

lang = "en"
tweetsPerDay = 100
maxTotalTweets = 30000


def downloadTweets(maxTotalTweets, tweetsPerDay, hashtag, lang):
    
    totalTweets = 0
    totalTweetsDay = 0
    tweets = []
    
    daysToProcess = generateDaysToProcess(maxTotalTweets, tweetsPerDay)

    for day in daysToProcess:
        if totalTweets >= maxTotalTweets:
                print("Max total tweets reached")
                print("Total tweets: " + str(totalTweets))
                break
                
        for tweet in sntwitter.TwitterHashtagScraper(hashtag + " lang:" + lang + " since:" + str(day) + " until:" + str(day + timedelta(days=1))).get_items():
                 
                tweets.append(str(tweet.date.date())+", "+str(tweet.rawContent).replace("\n", " ")+"\n")
                totalTweets += 1
                totalTweetsDay += 1
    
                if totalTweetsDay >= tweetsPerDay:
                    totalTweetsDay = 0
                    print("Total tweets: " + str(totalTweets))
                    break
    return tweets

def saveTweets(filename, tweets):
    with open (filename, "w", encoding="utf-8") as file:
        for tweet in tweets:
            file.write(tweet + "\n")

def generateDaysToProcess(maxTotalTweets, tweetsPerDay):
    daysToProcess = []
    for i in range(maxTotalTweets//tweetsPerDay):
        daysToProcess.append((datetime.now() - timedelta(days=i)).date())
    return daysToProcess

def main():
    saveTweets("tweetsIsrael.txt", downloadTweets(maxTotalTweets, tweetsPerDay, hashtag, lang))
    saveTweets("tweetsPalestine.txt", downloadTweets(maxTotalTweets, tweetsPerDay, hashtag2, lang))

if __name__ == '__main__':
    main()