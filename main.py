import json

import requests

api ="https://api.covid19india.org/data.json"
data = requests.get(api)
data =json.loads(data.text)


cases = data['cases_time_series']
print("---------------------------------------------------------------")
print ("TOTAL CASES IN INDIA DATE WISE")
print("---------------------------------------------------------------")
for i in cases:
    print(i['date'] +" : "+ i['totalconfirmed'])

cases = data['statewise']

print("---------------------------------------------------------------")
print ("ACTIVE CASES IN STATES")
print("---------------------------------------------------------------")
for i in cases:
    print(i['state'] +" : "+ i['active'])

print("---------------------------------------------------------------")
print ("TOTAL CASES IN STATES")
print("---------------------------------------------------------------")
for i in cases:
    print(i['state'] +" : "+ i['confirmed'])

print("---------------------------------------------------------------")
print ("RECOVERED CASES IN STATES")
print("---------------------------------------------------------------")
for i in cases:
    print(i['state'] +" : "+ i['recovered'])
print("---------------------------------------------------------------")




