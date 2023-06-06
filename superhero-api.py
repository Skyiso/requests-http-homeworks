import requests
import pprint as pp

url = 'https://akabab.github.io/superhero-api/api/all.json'
response = requests.get(url)
superheroes_list = ['Hulk', 'Captain America', 'Thanos']
superheroes_dict = response.json()
# pp.pprint(superheroes_dict)

intelligence_list = []

for superhero in superheroes_dict:
    if superhero['name'] in superheroes_list:
        intel = superhero['powerstats']['intelligence']
        name = superhero['name']
        intelligence_list.append(intel)
#         print(f'{name}: {intel}')
# print(intelligence_list)

result = dict(zip(superheroes_list, intelligence_list))
# print(result)
res = max(result, key = result.get)
print(res)