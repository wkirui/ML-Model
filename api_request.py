import requests
url = 'http://localhost:8000/resultsApi'

r =  requests.post(url, 
                   json={'guests': 3,'bedrooms': 2,
                         'beds': 2,'baths': 1,
                         'reviews':135,'rating': 4,
                         'kitchen':'yes','is_superhost':'no',
                         'wifi':'yes','parking':'yes',
                         'pool':'no','shared_bath':'yes'}
                   )

print(r.json())