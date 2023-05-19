from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from text2emotion import get_emotion
# import nltk

# nltk.download('vader_lexicon')

def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    return sentiment_scores

with open('negativeOpinion.txt', 'r') as file:
    negativeOpinion = file.read().replace('\n', '')


with open('positiveOpinion.txt', 'r') as file:
    positiveOpinion = file.read().replace('\n', '')

# negativeOpinion = tokenize.sent_tokenize(negativeOpinion)

# positiveOpinion = tokenize.sent_tokenize(positiveOpinion)

scores1 = analyze_sentiment(negativeOpinion)
print("Opinia negatywna:")
print("Pozytywność:", scores1['pos'])
print("Negatywność:", scores1['neg'])
print("Neutralność:", scores1['neu'])
print("Wynik zagregowany (compound):", scores1['compound'])

scores2 = analyze_sentiment(positiveOpinion)
print("Opinia pozytywna:")
print("Pozytywność:", scores2['pos'])
print("Negatywność:", scores2['neg'])
print("Neutralność:", scores2['neu'])
print("Wynik zagregowany (compound):", scores2['compound'])


# Opinia negatywna:
# Pozytywność: 0.067
# Negatywność: 0.062
# Neutralność: 0.871
# Wynik zagregowany (compound): 0.5421

# Opinia pozytywna:
# Pozytywność: 0.457
# Negatywność: 0.0
# Neutralność: 0.543
# Wynik zagregowany (compound): 0.9877

emotions1 = get_emotion(negativeOpinion)
print("Opinia negatywna:")
for emotion, value in emotions1.items():
    print(emotion.capitalize(), ":", value)

emotions2 = get_emotion(positiveOpinion)
print("Opinia pozytywna:")
for emotion, value in emotions2.items():
    print(emotion.capitalize(), ":", value)

# Opinia negatywna:
# Happy : 0.18
# Angry : 0.11
# Surprise : 0.14
# Sad : 0.32
# Fear : 0.25

# Opinia pozytywna:
# Happy : 0.86
# Angry : 0.0
# Surprise : 0.0
# Sad : 0.0
# Fear : 0.14

#wyniki nie pokrywają się całkowicie z oczekiwaniami głównie z powodu negatywnej opinii, która napisana jest w taki sposób, że ciężko ją zakwalifikować do jakiejś emocji czy do pozytywnej/negatywnej opinii

with open('negativeOpinionSpicedUp.txt', 'r') as file:
    negativeOpinionSpicedUp = file.read().replace('\n', '')


with open('positiveOpinionSpicedUp.txt', 'r') as file:
    positiveOpinionSpicedUp = file.read().replace('\n', '')

scores3 = analyze_sentiment(negativeOpinionSpicedUp)
print("Opinia negatywna:")
print("Pozytywność:", scores3['pos'])
print("Negatywność:", scores3['neg'])
print("Neutralność:", scores3['neu'])
print("Wynik zagregowany (compound):", scores3['compound'])

scores4 = analyze_sentiment(positiveOpinionSpicedUp)
print("Opinia pozytywna:")
print("Pozytywność:", scores4['pos'])
print("Negatywność:", scores4['neg'])
print("Neutralność:", scores4['neu'])
print("Wynik zagregowany (compound):", scores4['compound'])

# Opinia negatywna:
# Pozytywność: 0.039
# Negatywność: 0.144
# Neutralność: 0.818
# Wynik zagregowany (compound): -0.9811

# Opinia pozytywna:
# Pozytywność: 0.431
# Negatywność: 0.0
# Neutralność: 0.569
# Wynik zagregowany (compound): 0.991

emotions3 = get_emotion(negativeOpinionSpicedUp)
print("Opinia negatywna:")
for emotion, value in emotions3.items():
    print(emotion.capitalize(), ":", value)

emotions4 = get_emotion(positiveOpinionSpicedUp)
print("Opinia pozytywna:")
for emotion, value in emotions4.items():
    print(emotion.capitalize(), ":", value)

# Opinia negatywna:
# Happy : 0.03
# Angry : 0.1
# Surprise : 0.13
# Sad : 0.32
# Fear : 0.42

# Opinia pozytywna:
# Happy : 0.58
# Angry : 0.0
# Surprise : 0.17
# Sad : 0.0
# Fear : 0.25

#jak widać po dodaniu dodatkowych słów i pozmienianiu trochę tekstu wyniki są bardziej wyraźnie pozytywne/negatywne i bardziej zgodne z oczekiwaniami







#https://www.booking.com/hotel/gb/white-house-london.pl.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaLYBiAEBmAEeuAEXyAEM2AEB6AEB-AEMiAIBqAIDuAL6ipqjBsACAdICJGY5MDhjMzlhLWM4ZDMtNDhiZC04YzU0LTAxMTI5NGEzZGE4OdgCBuACAQ&sid=d7a122c8938b31a87e3f595fa43dc469&dest_id=-2601889;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=2;hpos=2;nflt=ht_id%3D204;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;srepoch=1684440662;srpvid=3e438de6f3b90298;type=total;ucfs=1&#tab-main

# Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
# Sentiment Analysis of Social Media Text. Eighth International Conference on
# Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.