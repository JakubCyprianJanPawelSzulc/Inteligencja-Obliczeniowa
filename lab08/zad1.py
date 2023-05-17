from nltk.tokenize import sent_tokenize, word_tokenize
import nltk

def main():
    # nltk.download('punkt')
    # nltk.download('stopwords')

    with open('article.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    sentences = sent_tokenize(text)
    words = word_tokenize(text)
    print('Zdania: ', len(sentences))
    print('Słowa: ', len(words))
    print('Średnia liczba słów na zdanie: ', len(words) / len(sentences))

    # usuwanie stop-words
    stop_words = list(nltk.corpus.stopwords.words('english'))
    additional_stopwords = ['11lb', '7,280', '3.6%', '( $ 1.1m/£900,000 )', '1.2g', '3.6g']
    stop_words.append(additional_stopwords)
    words = [w for w in words if not w in stop_words]
    print('Słowa po usunięciu stop-words: ', len(words))
    with open('article_without_stopwords.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(words))




if __name__ == '__main__':
    main()
