import json

filename = 'json\\numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)