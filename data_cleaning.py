import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import re
import string
import threading
from nltk.corpus import wordnet as wn 


def lemmatize(text):
    lemmatized_word = [wordnet_lemmatizer.lemmatize(word) for word in nltk.word_tokenize(text)]
    return " ".join(lemmatized_word)


def clean_string(word):
    stripped_string = word.strip()
    removed_numbers = re.sub(r'[0-9]', '', stripped_string)
    remove_tags = re.compile('<.*?>')
    removed_html = re.sub(remove_tags, '', removed_numbers)
    remove_punct = re.compile(f'[{re.escape(string.punctuation)}]')
    cleaned_string = re.sub(remove_punct, '', removed_html)
    cleaned_string = ' '.join([w for w in nltk.word_tokenize(cleaned_string) if not w in stopwords]) 

    return cleaned_string


def handle_string(input_text):
    sentences = nltk.sent_tokenize(input_text.lower())

    ret = []
    for sentence in sentences:
        lemmatize_sent = lemmatize(sentence)
        cleaned_string = clean_string(lemmatize_sent)
        word_tokenized = nltk.word_tokenize(cleaned_string)

        ret.extend(word_tokenized)

    return ret

def thread_routine(df, start, end):
    df.loc[start:end, ('Word List Cleaned')] = df['Text'][start:end].apply(handle_string)

    print(f'thread ({start}, {end}) is done')


if __name__ == '__main__':
    df = pd.read_csv('data/reviews.csv')

    df['Word List Cleaned'] = np.nan

    wordnet_lemmatizer = WordNetLemmatizer()
    stopwords = stopwords.words('english')

    wn.ensure_loaded()

    # use threads to increase performance for large dataset
    # dataset has over 500,000 rows
    t1 = threading.Thread(target=thread_routine, args=(df, 400000, 442114))
    t2 = threading.Thread(target=thread_routine, args=(df, 442114, 484227))
    t3 = threading.Thread(target=thread_routine, args=(df, 484227, 526341))
    t4 = threading.Thread(target=thread_routine, args=(df, 526341, len(df)))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()


    print('Done')
    df.dropna(subset=['Word List Cleaned'], inplace=True)

    df.to_csv('data/final_cleaned_data.csv')




