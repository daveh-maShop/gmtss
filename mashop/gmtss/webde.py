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
