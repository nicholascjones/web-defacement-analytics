import requests
import json

z = requests.get("http://archive.org/wayback/available?url=facebook.com")
q = z.json()

print q['archived_snapshots']['closest']['available']

