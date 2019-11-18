import requests
import json


#url = "https://reports.sem-o.com/api/v1/documents/static-reports"

url = "https://prodapi.metweb.ie/observations/newport-furnace/today"

response = requests.get(url)
data = response.json()

for row in data:
    print(row["pressure"])

#filename = 'weatherRreport.json'
#Writing JSON data
#f = open(filename, 'w')
#json.dump(data, f, indent=4)