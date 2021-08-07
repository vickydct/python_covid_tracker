import json

import requests

api ="https://api.covid19india.org/data.json"
data = requests.get(api)
data =json.loads(data.text)


cases = data['cases_time_series']
print ("TOTAL CASES IN INDIA")
for i in cases:
    print(i['date'] +" : "+ i['totalconfirmed'])
cases = data['statewise']
print ("ACTIVE CASES IN STATES")
for i in cases:
    print(i['state'] +" : "+ i['active'])







