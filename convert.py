import csv
import json

strings = []

with open('resources/Adjectives.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        number, string = row
        strings.append(string)

with open('resources/adjectives.json', 'w') as file:
    json.dump(strings, file, indent=4)