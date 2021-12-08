from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib


if __name__ == '__main__':
    df = pd.read_csv('data/final_cleaned_data.csv')

    pipeline = Pipeline([
        ('vectorize', CountVectorizer(ngram_range=(1, 2))),
        ('tfidf', TfidfTransformer(use_idf=True)),
        ('classifier', MultinomialNB(alpha=0.01))
    ])

    parameters = {
        'vectorize__ngram_range': [(1, 1), (1, 2)],
        'tfidf__use_idf': (True, False),
        'classifier__alpha': (1e-2, 1e-3)
    }

    best_pipeline = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)

    bound = int(len(df) * .8)

    best_pipeline.fit(df['Word List Cleaned'][:bound], df['Score'][:bound])
    print('Finding best params for model')

    for param in parameters.keys():
        print(f'{param}: {best_pipeline.best_params_[param]}')

    # best params to use
    # vectorize__ngram_range: (1, 2)
    # tfidf__use_idf: True
    # classifier__alpha: 0.01

    pipeline.fit(df['Word List Cleaned'][:bound], df['Score'][:bound])
    print('Finished fitting data to model')
    joblib.dump(pipeline, 'model/pipeline.pkl')
    print('Finished saving the model')



