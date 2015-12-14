import requests, json, re, sys
from time import sleep
from config import FMA_API

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

for page in range(1, 832):

    payload = { 'api_key' : str(FMA_API), 'page' : page }
    try:
        r = requests.get("https://freemusicarchive.org/api/get/artists.json?", params = payload)
        sleep(1)
    except:
        continue
    data = json.loads(r.text)
    #total: 16610, total_pages: 1108 (831?), limit: 20


    for l in data['dataset']:
        try:
            artist_id = int(l['artist_id'])
            artist_name = str(l['artist_name'])
            if artist_id not in ids:
                ids[artist_id] = []
            ids[artist_id].append(artist_name)
        except:
            print (data['errors'])

        uprint (artist_name)
with open('fma_ids.json', 'w') as outfile:
    json.dump(ids, outfile)
