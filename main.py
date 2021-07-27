import json

f = open("recipes_raw_nosource_epi.json")

data = json.load(f)

for i in data["05zEpbSqcs9E0rcnCJWyZ9OgdH0MLby"]:
    print(i)

f.close
