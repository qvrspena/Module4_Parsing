# Vhan Randolp Pena
import json

course = []
name = []

with open('sample.json', 'r') as json_file:
    x = json.load(json_file)

    for courses in x['certifications']:
        print(courses['courses'])
        print(courses['name'])