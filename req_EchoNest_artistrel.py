import requests, json, sys, re, csv
from time import sleep
from config import Echo_API

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
with open('fma_ids.json') as into:
#FMA_ids is json file with artists and IDs list from FMA
#call artist list file and assign to python variable
    artdict = json.load(into)
#empty dictionary to fill with related artists

related = []
for fmaart in artdict:
#query EchoNest with artist names from FMA
    artist_name = artdict[fmaart][0]

    # print(str(artist_name))

    payload = { 'name' : str(artist_name), 'api_key' : str(Echo_API)}

    try:
        r = requests.get("http://developer.echonest.com/api/v4/artist/search?format=json&results=1", params = payload)
        # sleep(.5)
    except:
        continue

    data = json.loads(r.text)

    try:
        artists = data['response']['artists'][0]
        good_artist_name = artists['name']
        artist_echo_id = artists['id']
    except:
        print(data['response'])
        continue


    payload = { 'name' : str(artist_name), 'api_key' : str(Echo_API)}

    try:
        r = requests.get("http://developer.echonest.com/api/v4/artist/similar?format=json&bucket=id:fma&limit=true", params = payload)
    except:
        continue

    data = json.loads(r.text)

    artist_result = { "fma_id" : fmaart, "related" : []}
    #response structure = id, queried artist: related artist: id, related artist: id, etc.

    if "artists" in data['response']:
        for res in data['response']['artists']:
            related_artist_id = res['foreign_ids'][0]['foreign_id']
            try:
                artist_result['related'].append(related_artist_id)
            except:
                pass
    else:
        uprint (fmaaart)

    related.append(artist_result)

with open('echo_related_network.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Source', 'Target'])
    for relate_set in related:
        quer_id = relate_set['fma_id']
        for en_response in relate_set['related']:
            p = re.compile('(\d{1,5})')
            en_id = p.findall(en_response)
            en_id_num = en_id[0]
            w.writerow([quer_id, en_id_num])
