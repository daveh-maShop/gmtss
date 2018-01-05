import json
import pprint

from mashop.gmtss.da_cb import get_bucket, upsert
from mashop.gmtss.utils import rbo_results2dict
from mashop.gmtss.webde import WebDE

pp = pprint.PrettyPrinter(depth=6, indent=4)

rbo = WebDE()
bucket = get_bucket('dev_MotherBucket')

host = 'http://dev-dsb.marketamerica.com'
port = '80'
base_resource = 'dataEngine/rest/dataretrieval/redback/dmc'
rbo_module = 'TRAINING'
rbo_class = 'NMTSS'
rbo_method = 'getTrainingMemberCat'
body = '{"siteCountry": "", "siteType": "U", "langCode": "ENG", "categoryID": ""}'
# rbo_results = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
v1_doc = {'_id': 'gmtss_v1_member_categories', 'doc_type': 'gmtss_v1_member_categories', 'version': '1.0'}
v1_doc['dsb_payload'] = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
upsert(bucket, v1_doc['_id'], v1_doc)

rbo_properties = v1_doc['dsb_payload']['results']['results']
pp.pprint(v1_doc)

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
result['doc_type'] = 'gmtss_member_categories'
result['_id'] = 'gmtss_v2_member_categories'
result['version'] = '2.0'
upsert(bucket, result['_id'], result)
pp.pprint(result)
