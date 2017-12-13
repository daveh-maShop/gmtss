import pprint

from mashop.gmtss.webde import WebDE
pp = pprint.PrettyPrinter(depth=6, indent=4)
rbo = WebDE()

host = 'http://dev-dsb.marketamerica.com'
port = '80'
base_resource = 'dataEngine/rest/dataretrieval/redback/dmc'
rbo_module = 'TRAINING'
rbo_class = 'NMTSS'
rbo_method = 'getTrainingMemberType'
body = '{"siteCountry": "", "siteType": "U", "langCode": "ENG"}'
rbo_results = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
rbo_properties = rbo_results['results']['results']

pp.pprint(rbo_results)
