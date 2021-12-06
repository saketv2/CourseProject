import pandas as pd


# preprocess the df
df = pd.read_csv('reviews.csv')
df.dropna(subset=['Text', 'Score'], inplace=True)

text = df['Text']
scores = df['Score']

print(scores)