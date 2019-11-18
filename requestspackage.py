import requests

url = 'https://www.gmit.ie'

response = requests.get(url)

print(response.status_code)
print(response.text)