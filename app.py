from flask import Flask, request, jsonify
import json
import string
from spacy.lang.en.stop_words import STOP_WORDS
import spacy
import re
import joblib
import pandas as pd

application = Flask(__name__)

punctuations = string.punctuation
nlp = spacy.load('en_core_web_sm')
stop_words = spacy.lang.en.stop_words.STOP_WORDS
pipeline = joblib.load('model/pipeline.pkl')


@application.route('/json', methods = ['GET', 'POST'])
def handle_json():
    if request.method == 'POST':
        data = json.loads(request.get_data())
        parsedText = data['parsedText']

        print(parsedText)

        removed_numbers = re.sub(r'[0-9]', '', parsedText)
        tokenized = nlp(removed_numbers)
        tokenized = [word.lemma_.lower().strip() if word.lemma_ != '-PRON-' else word.lower_ for word in tokenized]
        tokenized_list = [word for word in tokenized if word not in stop_words and word not in punctuations]
        
        predict = pipeline.predict(tokenized_list)
  
        return jsonify(sum(predict)/len(predict))


if __name__ == '__main__':
    application.run(debug = True)
