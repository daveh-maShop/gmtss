import pprint

from mashop.scratch.da_cb import get_bucket, upsert
from mashop.scratch.utils import rbo_results2dict
from mashop.scratch.webde import WebDE

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
v1_doc = {'_id': 'gmtss::member_categories::v1', 'doc_type': 'gmtss_v1_member_categories', 'version': '1.0'}
v1_doc['dsb_payload'] = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
upsert(bucket, v1_doc['_id'], v1_doc)

rbo_properties = v1_doc['dsb_payload']['results']['results']
pp.pprint(v1_doc)

conversion_map = {}
conversion_map['sv'] = {'member_cat_count': {'rbo_name': 'memberCatCnt', 'json_type': 'int'}}
conversion_map['mv_groups'] = {'category_id': {'category_id': {'rbo_name': 'categoryID', 'json_type': 'int'},
                                               'active_status': {'rbo_name': 'activeStatus', 'json_type': 'bool'},
                                               'hist_name': {'rbo_name': 'histName', 'json_type': 'str'},
                                               'hist_date': {'rbo_name': 'histDate', 'json_type': 'str'},
                                               'hist_time': {'rbo_name': 'histTime', 'json_type': 'str'},
                                               'cat_abbrev': {'rbo_name': 'catAbbrev', 'json_type': 'str'},
                                               'cat_name_SPA': {'rbo_name': 'catNameSPA', 'json_type': 'str'},
                                               'cat_abbrev_SPA': {'rbo_name': 'catAbbrevSPA', 'json_type': 'str'}
                                               }
                               }
v2_doc = {}
v2_doc['doc_type'] = 'gmtss_member_categories'
v2_doc['_id'] = 'gmtss::member_categories::v2'
v2_doc['version'] = '2.0'
v2_doc['data'] = rbo_results2dict(rbo_properties, conversion_map)
upsert(bucket, v2_doc['_id'], v2_doc)
pp.pprint(v2_doc)
