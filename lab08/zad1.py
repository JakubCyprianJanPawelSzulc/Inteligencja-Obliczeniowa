from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.probability import FreqDist
import nltk
import string
import matplotlib.pyplot as plt
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

def main():
    nltk.download('punkt')
    nltk.download('stopwords')

    with open('article.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    words = word_tokenize(text)

    # Usuwanie stop-words
    stop_words = list(nltk.corpus.stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    print('Liczba słów po usunięciu stop-words: ', len(words))

    additional_stopwords = ['11lb', '7,280', '3.6%', '( $ 1.1m/£900,000 )', '1.2g', '3.6g', '35-year-old', '2021', '3.6', '``', "''", "16,000", '€1', '1.1/£0.9', '15,000', "'s", "n't", "1.1m/£900,000", '10,000', '--']
    stop_words.extend(additional_stopwords)
    stop_words.extend(list(string.punctuation))
    stop_words.extend([str(i) for i in range(0, 1000)])
    words = [w for w in words if not w in stop_words]
    print('Liczba słów po usunięciu innych niepotrzebnych: ', len(words))

    # # Stemming słów
    # stemmer = PorterStemmer()
    # words = [stemmer.stem(w) for w in words]
    # print('Liczba słów po stemmingu: ', len(words))

    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(w, pos='v') for w in words]  # Dodaj argument 'pos' dla lematyzacji czasowników
    words = [lemmatizer.lemmatize(w) for w in words]
    print('Liczba słów po lematyzacji: ', len(words))

    ########### nie wiem czemu niezależnie od tego czy użyję stemmingu czy lematyzacji, liczba słów jest taka sama jak przed tą operacją

    with open('article_clean.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(words))

    # Wektor zliczający słowa
    word_freq = FreqDist(words)

    top_words = word_freq.most_common(10)
    words, freqs = zip(*top_words)

    plt.figure(figsize=(10, 6))
    plt.bar(words, freqs)
    plt.xlabel('Słowa')
    plt.ylabel('Liczba wystąpień')
    plt.title('10 najczęściej występujących słów')
    plt.xticks(rotation=45)
    plt.show()

    wordcloud = WordCloud(width=1600, height=800, max_font_size=200).generate(text)
    plt.figure(figsize=(12,10))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()



if __name__ == '__main__':
    main()
