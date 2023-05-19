import snscrape.modules.twitter as sntwitter

hashtag = "#bmw"
location = "54.3520, 18.6464, 100km" 

tweets1 = []
for tweet in sntwitter.TwitterHashtagScraper(hashtag).get_items():
    tweets1.append(tweet.content)
    if len(tweets1) >= 100:
        break

query = f"near:\"{location}\""
tweets2 = []
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    tweets2.append(tweet.content)
    if len(tweets2) >= 50:
        break

#tag = "#bmw"
for tweet in tweets1:
    print(tweet)

#gdańsk
for tweet in tweets2:
    print(tweet)

# Problem jest taki, że najprawdopodbniej trzeba mieć konto dewelopera także dla tej biblioteki, żeby móc pobrać jakiekolwiek tweety z api twittera
