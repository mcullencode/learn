import requests
import json

url = "https://reddit.com/.json"

#headers to make reddit think a browser is making the request and stop rate limiting me :(
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


r = requests.get(url, headers=headers)
print(r.status_code)

data = r.json()
with open('data.json','w') as f:
    json.dump(data, f)

