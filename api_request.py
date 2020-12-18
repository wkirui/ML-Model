import requests
url = 'http://localhost:5000/resultsApi'

r =  requests.post(url, 
                   json={'guests':2,'bedrooms':1,
                         'beds':1,'baths':1,
                         'reviews':12,'rating':4,
                         'kitchen':'yes','is_superhost':'yes',
                         'wifi':'yes','parking':'yes',
                         'pool':'no','shared_bath':'no'}
                   )

print(r.json())