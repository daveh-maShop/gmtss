import json
import requests
import pprint

pp = pprint.PrettyPrinter(depth=6)

host = 'http://dev-dsb.marketamerica.com:80/'
base_resource = 'dataEngine/rest/dataretrieval/redback/dmc/'
rbo_module = 'UTIL/'
rbo_class = 'ValidateConnection/'
rbo_method = 'validateUtilServiceConnection'
url = host + base_resource + rbo_module + rbo_class + rbo_method
print (url)
header = {"Content-Type": "application/json"}
body = '{"command": "READ"}'

r = requests.post(url , headers=header, data=body)
pp.pprint(r.status_code)
pp.pprint(json.loads(r.text))
