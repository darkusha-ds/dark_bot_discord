import json, random

mam = "AUTHOR" # 0 is mam
mum = "USER" # 1 is mum

with open('cmd.json', 'r') as f:
    text = json.loads(f.read())
    snow = random.choice(text["snowball"])
    print(snow.format(mam, mum))
