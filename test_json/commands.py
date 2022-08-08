import json, random

with open('commands.json', 'r') as f:
    commands = json.loads(f.read())
    ball = random.choice(commands["ball"])
    login = random.choice(commands["login"])
    logout = random.choice(commands["logout"])
    hugs = random.choice(commands["hugs"])
    kill = random.choice(commands["kill"])
    kiss = random.choice(commands["kiss"])
    pats = random.choice(commands["pats"])
    poke = random.choice(commands["poke"])
    rip = random.choice(commands["rip"])
    snowball = random.choice(commands["snowball"])

input()
