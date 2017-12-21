import pprint

from mashop.gmtss.utils import rbo_results2dict
from mashop.gmtss.webde import WebDE

pp = pprint.PrettyPrinter(depth=6, indent=4)

rbo = WebDE()

host = 'http://dev-dsb.marketamerica.com'
port = '80'
base_resource = 'dataEngine/rest/dataretrieval/redback/dmc'
rbo_module = 'TRAINING'
rbo_class = 'NMTSS'
rbo_method = 'getTrainingMemberType'
body = '{"siteCountry": "", "siteType": "I", "langCode": "ENG"}'
rbo_results = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
pp.pprint(rbo_results)
rbo_properties = rbo_results['results']['results']


conversion_map = {}
conversion_map['sv'] = {'country_count': {'rbo_name': 'countryCnt', 'json_type': 'int'},
                        'member_type_count': {'rbo_name': 'memberTypeCnt', 'json_type': 'str'}
                        }
conversion_map['mv_groups'] = {'member_type_id': {'rbo_name': 'memberTypeID', 'json_type': 'str',
                                                  'associations': {
                                                      'member_name': {'rbo_name': 'memberName', 'json_type': 'str'},
                                                      'category': {'rbo_name': 'category', 'json_type': 'str'},
                                                      'display_pin': {'rbo_name': 'displayPin', 'json_type': 'str'},
                                                      'expiration_length': {'rbo_name': 'expirationLength',
                                                                            'json_type': 'str'},
                                                      'history_date': {'rbo_name': 'histDate', 'json_type': 'str'},
                                                      'history_time': {'rbo_name': 'histTime', 'json_type': 'str'},
                                                      'history_name': {'rbo_name': 'histName', 'json_type': 'str'},
                                                      'is_country_selected': {'rbo_name': 'isCountrySelected',
                                                                              'json_type': 'str',
                                                                              'associations': {'rbo_name': 'country'}},
                                                      'show_in_search': {'rbo_name': 'showInSearch',
                                                                         'json_type': 'str'},
                                                      'type_abbreviation': {'rbo_name': 'typeAbbrev',
                                                                            'json_type': 'str'},
                                                      'type_abbreviation_SPA': {'rbo_name': 'typeAbbrevSPA',
                                                                                'json_type': 'str'},
                                                      'type_name_SPA': {'rbo_name': 'typeNameSPA', 'json_type': 'str'}
                                                  }}}
result = rbo_results2dict(rbo_properties, conversion_map)
print('----------------------------')
pp.pprint(result)
