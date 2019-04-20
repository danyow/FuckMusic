import json

jsonString = ""
with open('music.json') as f:
    jsonString = f.read()

musics = json.loads(jsonString)

for music in musics:
    print(music['title'])