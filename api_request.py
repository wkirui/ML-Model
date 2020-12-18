import requests
# url = 'http://localhost:8000/resultsApi'
url = 'https://naimodel.herokuapp.com/resultsApi'

r =  requests.post(url, 
                   json={'guests': 4,'bedrooms': 2,
                         'beds': 2,'baths': 1,
                         'reviews':45,'rating': 4,
                         'kitchen':'yes','is_superhost':'no',
                         'wifi':'yes','parking':'yes',
                         'pool':'no','shared_bath':'yes'}
                   )

print(r.json())