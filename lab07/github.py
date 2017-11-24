import requests
r = requests.get("https://api.github.com/repos/smeiklej/secu2002_2017/commits")
text = r.json()

# Printing the commit message for every entry x
y = map(lambda x: x['commit']['message'], text)
for msgs in y:
    print msgs