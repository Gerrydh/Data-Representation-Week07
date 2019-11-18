import requests
import json



#url = "https://reports.sem-o.com/api/v1/documents/static-reports"

url = "https://reports.sem-o.com/api/v1/documents/static-reports?ReportName=Balancing%20and%20Imbalance%20Market%20Cost%20View&Date=>2019-11-10"

response = requests.get(url)
data = response.json()
totalPages = data["pagination"]["totalPages"]
#print(totalPages)
listOfReports = []

pageNumber=1
while pageNumber <= totalPages:
    pageUrl = url + "&page="+ str(pageNumber)
    #print(pageUrl)
    #print(pageNumber)
    data = requests.get(pageUrl).json()
    for item in data["items"]:
        #print(item["ResourceName"])
        listOfReports.append(item["ResourceName"])

    pageNumber +=1

#output to console
#print(data)
for reportName in listOfReports:
    print(reportName)

#other code
#save this to a file
filename = 'allreports.json'
#Writing JSON data
f = open(filename, 'w')
json.dump(data, f, indent=4)