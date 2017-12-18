import pprint

from utils import rbo_results2dict
from mashop.gmtss.webde import WebDE
pp = pprint.PrettyPrinter(depth=6, indent=4)

rbo = WebDE()

host = 'http://dev-dsb.marketamerica.com'
port = '80'
base_resource = 'dataEngine/rest/dataretrieval/redback/dmc'
rbo_module = 'TRAINING'
rbo_class = 'NMTSS'
rbo_method = 'getTrainingMemberCat'
body = '{"siteCountry": "", "siteType": "U", "langCode": "ENG", "categoryID": ""}'
rbo_results = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
rbo_properties = rbo_results['results']['results']
pp.pprint(rbo_properties)

#TODO can we automate this??? should we???
conversion_map = {}
conversion_map['sv'] = {'member_cat_count': {'rbo_name': 'memberCatCnt', 'json_type': 'int'}}
conversion_map['mv_groups'] = {'category_id': {'rbo_name': 'categoryID', 'json_type': 'str',
                                               'associations': {
                                                   'active_status': {'rbo_name': 'activeStatus', 'json_type': 'int'},
                                                   'hist_name': {'rbo_name': 'histName', 'json_type': 'str'},
                                                   'hist_date': {'rbo_name': 'histDate', 'json_type': 'str'},
                                                   'hist_time': {'rbo_name': 'histTime', 'json_type': 'str'},
                                                   'cat_abbrev': {'rbo_name': 'catAbbrev', 'json_type': 'str'},
                                                   'cat_name_SPA': {'rbo_name': 'catNameSPA', 'json_type': 'str'},
                                                   'cat_abbrev_SPA': {'rbo_name': 'catAbbrevSPA', 'json_type': 'str'}
                                               }
                                               }
                               }

result = rbo_results2dict(rbo_properties, conversion_map)
pp.pprint(result)
