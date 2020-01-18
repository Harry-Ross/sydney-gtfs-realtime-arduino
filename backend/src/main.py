import models.gtfs_realtime_pb2
from google.protobuf.json_format import MessageToJson

import requests

url = "https://api.transport.nsw.gov.au/v1/gtfs/realtime/buses?debug=true"

payload = {}
headers = {
  'Authorization': 'apikey XMJAzun3zrbIWQwRzvdd6WfpbwHUs7FBGnSw'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text)