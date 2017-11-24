import pickle
file_name = 'shapeshift.p'
contents50 = pickle.load(open(file_name,'rb'))

# Number of ETH as input currency
counter = 0
for item in contents50:
    if item['curIn'] == 'ETH':
        counter = counter + 1
print counter

# Number of BTC as output currency
counter = 0
for item in contents50:
    if item['curOut'] == 'BTC':
        counter = counter + 1
print counter

# Number of ZEC as input currency and BTC as output currency
counter = 0
for item in contents50:
    if item['curIn'] == 'ZEC' and item['curOut'] == 'BTC':
        counter = counter + 1
print counter