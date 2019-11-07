import requests

service_url = input("Service URL: ")
service_url += "/query"
number_of_records = int(input("Number of records: "))

obj_str = ','.join(map(str, [i for i in range(number_of_records + 1)]))

payload = {
    'where': '1=1',
    'objectIds': obj_str,
    'geometryType': 'esriGeometryEnvelope',
    'spatialRel': 'esriSpatialRelIntersects',
    'returnGeometry': 'true',
    'returnTrueCurves': 'false',
    'returnIdsOnly': 'true',
    'returnCountOnly': 'false',
    'returnDistinctValues': 'false',
    'featureEncoding': 'esriDefault',
    'f': 'json'
}

response = requests.post(service_url, payload, verify=False)
r = response.json()
print(r)