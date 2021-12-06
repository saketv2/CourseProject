import requests

# url = 'https://api.yelp.com/v3/businesses/search'
headers = {'Authorization': "Bearer l3FxpduQFrB6ZyMjJ4qOirPDONumEQ2kJtv_MWjpbv5yVzERMvDzRFAo6hyDJglz4v6iCNEestTCaJOQWVKTLvlcu0m34Z8BwxmLVlg3-gCo6dEP2Jtw2Pa2skhyYXYx"}
# params = {'term': 'restaurants', 'location': 'Green St. Champaign, Illinois', 'limit': 50, 'offset': 200}

# r = requests.get(url=url, params=params, headers=headers)
# r = r.json()

# with open('sample.txt', 'w') as file:
#     for i in range(0, 240, 50):
#         params['offset'] = i
#         if i == 200:
#             params['limit'] = 40

#         r = requests.get(url=url, params=params, headers=headers)
#         r = r.json()
#         for business in r['businesses']:
#             file.write(f"{business['id']}\t{business['name']}\n")
url = f"https://api.yelp.com/v3/businesses/{'nAo4t68uFs9g21sQVRXGig'}/reviews"
r = requests.get(url=url, headers=headers)
r = r.json()
for review in r['reviews']:
    print(review['rating'], review['text'])

print(len(r['reviews']))