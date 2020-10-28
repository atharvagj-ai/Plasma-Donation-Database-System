import json
import urllib3

http = urllib3.PoolManager()

heroes = http.request('GET', 'https://api.covid19india.org/state_district_wise.json')

state_dict = json.loads(heroes.data.decode('UTF-8'))

# print(hero_dict)
# print(state_dict['Delhi']['districtData']['Central Delhi']['active'])
for i in state_dict['Delhi']['districtData']:
    print(i)
a = input("Enter a City")
temp = 0
for i in state_dict:
    for j in state_dict[i]['districtData']:
        if a == j:
            temp = 1
            print("Active: ", state_dict[i]['districtData'][j]['active'])
            break
if temp == 0:
    print("Not found")
else:
    print("Found")