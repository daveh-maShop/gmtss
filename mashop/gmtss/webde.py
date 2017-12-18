import json

import requests


class WebDE():
    """
    Class for calling WebDE (RBO/Redback objects' methods.

    """
    def call(self, host='http://dev-dsb.marketamerica.com',
             port='80',
             base_resource='dataEngine/rest/dataretrieval/redback/dmc',
             rbo_module='UTIL',
             rbo_class='ValidateConnection',
             rbo_method='validateUtilServiceConnection',
             body='{"command": "READ"}'):
        """ Calls a WebDE/RedBack/RBO method and returns resulting payload ad a dictionary"""
        whack = '/'
        url = host + ':' + port + whack + base_resource + whack + rbo_module + whack + rbo_class + whack + rbo_method
        print(url)
        header = {"Content-Type": "application/json"}
        # try:
        r = requests.post(url, headers=header, data=body)
        # except Exception:
        #     return {'error': 'RBO call failed'}
        r.encoding = 'UTF-8'
        return json.loads(r.text)
        # rbo_properties = payload['results']['results']

    def dsb2dict(rbo_properties, cm):
        # TODO: convert smv items
        """
        Takes a dictionary of rbo_properites (key:value (sv, mv & svm) and a conversion map (cm) and converts:
            1. single value rbo properties to a simple key:value (converting string to json type as indicated in the cm
            2. groups of associated multi-value properties based on the structure in the cm (convertibg string to json
                   type as indicated in the cm)
        """
        rbo_vm = 'ý'
        cd = {}  # converted data to be returned
        for key in cm['sv']:
            # note: the eval funtion will evaluate a '12/12/17' as a math division and not as a string
            if cm['sv'][key]['json_type'] != 'str':
                cd[key] = eval(cm['sv'][key]['json_type'] + '(' + rbo_properties[cm['sv'][key]['rbo_name']] + ')')
            else:
                cd[key] = rbo_properties[cm['sv'][key]['rbo_name']]

        for group_master_key in cm['mv_groups']:
            uv_values = {}
            uv_values[group_master_key] = rbo_properties[cm['mv_groups'][group_master_key]['rbo_name']] \
                .split(rbo_vm)
            for assoc_item_key in cm['mv_groups'][group_master_key]['associations']:
                uv_values[assoc_item_key] = rbo_properties[cm['mv_groups'][group_master_key]['associations']
                [assoc_item_key]['rbo_name']].split(rbo_vm)
            cd[group_master_key] = {}
            for i, val in enumerate(uv_values[group_master_key]):
                group_master_key_val = str(uv_values[group_master_key][i])
                cd[group_master_key][group_master_key_val] = {}
                for assoc_item_key in cm['mv_groups'][group_master_key]['associations']:
                    uv = uv_values[assoc_item_key][i]
                    jt = cm['mv_groups'][group_master_key]['associations'][assoc_item_key]['json_type']
                    if cm['mv_groups'][group_master_key]['associations'][assoc_item_key]['json_type'] != 'str':
                        # note: the eval funtion will evaluate a '12/12/17' as a math division and not as a string
                        json_type_value = eval(cm['mv_groups'][group_master_key]['associations'][assoc_item_key]
                                               ['json_type'] + '(' + uv_values[assoc_item_key][i] + ')')
                        cd[group_master_key][group_master_key_val][assoc_item_key] = json_type_value
                    else:
                        cd[group_master_key][group_master_key_val][assoc_item_key] = uv_values[assoc_item_key][i]
        return cd

