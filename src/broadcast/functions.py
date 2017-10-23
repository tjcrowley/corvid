import requests
from akamai.edgegrid import EdgeGridAuth
from urlparse import urljoin
from django.http import HttpResponse
from django.http.response import JsonResponse

baseurl = 'https://akab-pu2mdrv5mt5ejjcq-jm3uf3rvpzsdbvgo.luna.akamaiapis.net'
s = requests.Session()
s.auth = EdgeGridAuth(
    client_token='akab-hxtjvu576n5iuoph-lhh6lm7doebbvios',
    client_secret='yTr3c9RSs1qvyqQ9qsPhjkpv0odJ4fvtiVGC6VgSWZs=',
    access_token='akab-ojjalflpxesvtbdx-vbcnmez3y26fqhfj'
)


def createStream(name):
    
    payload = {
    "name": name,
    "format": "HLS",
    }

    result = s.post(urljoin(baseurl, '/config-media-live/v1/msl-origin/streams'),data=payload)
    return result

def readStream(name, cpcode):
    
    payload = {
    "cpcode": cpcode,
    "name": name,
    "format": "HLS",
    }

    result = s.post(urljoin(baseurl, '/config-media-live/v1/msl-origin/streams'),data=payload)
    return result

    
