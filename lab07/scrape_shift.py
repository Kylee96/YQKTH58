import pickle
import requests
r = requests.get('https://shapeshift.io/recenttx/50')
contents50 = r.json()

file_name = 'shapeshift.p'
pickle.dump(contents50, open(file_name, 'wb'))