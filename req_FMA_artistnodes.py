import requests, json, re, sys, csv
from time import sleep
from config import FMA_API

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

with open('fma_nodes_network_fav.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['ID', 'Label', 'Favorites'])
    for page in range(1, 832):

        payload = { 'api_key' : str(FMA_API), 'page' : page }

        r = requests.get("https://freemusicarchive.org/api/get/artists.json?", params = payload)
        sleep(1)
        data = json.loads(r.text)

        for l in data['dataset']:

            try:
                artist_id = int(l['artist_id'])
                artist_name = str(l['artist_name'])
                artist_favorites = int(l['artist_favorites'])
                w.writerow([artist_id, artist_name, artist_favorites])
                uprint (artist_id, artist_name)
            except:
                continue
