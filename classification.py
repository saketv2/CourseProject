# import pandas as pd
# import joblib




# if __name__ == '__main__':
#     df = pd.read_csv('data/final_cleaned_data.csv')
#     pipeline = joblib.load('model/pipeline.pkl')
#     bound = int(len(df) * .8)
#     predictions = pipeline.predict(df['Word List Cleaned'][bound:])
#     print(predictions, len(predictions), len(df['Word List Cleaned'][bound:]))

#     for i in range(100):
#         print(predictions[i])