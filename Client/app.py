import json
import http.client

conn = http.client.HTTPConnection("localhost:5000")
seed = json.dumps(
  {'ime': 'Velibor',
  'prezime': 'Krivokuca',
  'username': 'velibor',
  'smer': 'IT',
  'predmeti':
    [{'ime': 'Organizacija racunara', 'espb': 8},
     {'ime': 'PARIOS', 'espb': 6}
    ]}
)
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", seed, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
