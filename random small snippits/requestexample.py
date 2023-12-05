import requests

url = 'https://www.reddit.com'

response = requests.get(url)
print(response.content)