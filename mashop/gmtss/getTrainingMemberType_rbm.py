import pprint

from mashop.gmtss.webde import WebDE

pp = pprint.PrettyPrinter(depth=6, indent=4)

rbo = WebDE()

# host = 'http://dev-dsb.marketamerica.com'
# port = '80'
# base_resource = 'dataEngine/rest/dataretrieval/redback/dmc'
# rbo_module = 'TRAINING'
# rbo_class = 'NMTSS'
# rbo_method = 'getTrainingMemberType'
# body = '{"siteCountry": "", "siteType": "U", "langCode": "ENG"}'
# rbo_results = rbo.call(host, port, base_resource, rbo_module, rbo_class, rbo_method, body)
# rbo_properties = rbo_results['results']['results']
rbo_properties = {'category': '1ý5ý4ý3ý5ý5ý5ý3ý5ý5ý1ý5ý4ý3ý3ý3ý3ý3ý5ý4ý9ý1ý4ý3ý5ý5ý3ý5ý1ý1ý12ý12ý2ý2ý11ý4ý1',
                  'country': 'USAýAUSýGBRýHKGýTWNýSGPýESPýMYS',
                  'countryCnt': '8',
                  'isCountrySelected': '1ü1ü1ü0ü0ü0ü0ü1ý1ü1ü0ü1ü0ü0ü1ü1ý1ü0ü0ü0ü0ü0ü0ü0ý0ü1ü1ü1ü1ü1ü1ü1ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü1ü1ü1ü1ü1ü0ü1ý1ü1ü1ü1ü1ü1ü1ü1ý1ü1ü1ü1ü1ü1ü0ü1ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü1ü0ü0ü1ü0ü1ý1ü1ü1ü1ü1ü1ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý0ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü1ü1ü1ü1ü1ü1ü0ý1ü1ü1ü1ü1ü1ü1ü1ý1ü0ü0ü0ü0ü0ü0ü0ý0ü0ü0ü0ü0ü0ü0ü1ý1ü1ü1ü1ü1ü1ü1ü0ý1ü0ü0ü1ü1ü1ü0ü0ý0ü0ü0ü0ü0ü0ü0ü0ý1ü1ü0ü0ü1ü0ü0ü0ý1ü0ü1ü0ü1ü1ü0ü0ý1ü0ü0ü0ü0ü0ü0ü0ý1ü1ü1ü1ü1ü1ü1ü1ý1ü1ü1ü1ü1ü1ü1ü1ý0ü1ü1ü1ü1ü1ü1ü1ý1ü1ü1ü1ü1ü1ü1ü1ý1ü0ü0ü0ü0ü0ü0ü0ý1ü0ü0ü0ü1ü0ü0ü0ý1ü1ü1ü1ü1ü1ü1ü0',
                  'memberName': 'AAA CANCELýALL MEAT, NO FILLERýANTI-AGING UMO '
                                'TRAINERýASDFASDFýCAD TRAINERýCERTIFIED NUTRAMETRIX '
                                'CERTIFIED TRAINERSýCERTIFIED TLS COACHýCERTIFIED '
                                'TRAINERýCERTIFIED WEB CENTER TRAINERýCORPORATE '
                                'SPEAKERSýDISTRICT COORDINATORýFIELD PRODUCT '
                                'SPECIALISTýHEALTH & NUTRITION UMOýHELLO ENGýHELLO '
                                'ENGýHELLO ENGýHELLO ENGýHELLO ENGýINTERNET SALES AND '
                                'MARKETING TRAINERSýINTERNET SALES AND MARKETING UMO '
                                'TRAINERýJOE TEST 0ýLOCAL COORDINATORýMA CAPITAL RESOURCES '
                                'UMO TRAINERýMALAYSIA CERTIFICATIONýMOTIVES CERTIFIED '
                                'TRAINER SINGAPORE AND WORLDWIDEýMOTIVES OVERVIEWýMY ENG '
                                'NAMEýPROBABLE TROLLýREGIONAL COORDINATORýREGIONAL '
                                'DIRECTORýSPEAKER BUREAU CATEGORY 3ýSPEAKER BUREAU TYPE '
                                '4ýSPEAKERS BUREAU CATEGORY 1 ENGýSPEAKERS BUREAU CATEGORY '
                                '2ýTESTINGýTLS UMO TRAINERýUBP COORDINATOR',
                  'memberTypeCnt': '37',
                  'memberTypeID': '7ý9ý13ý11ý22ý26ý19ý27ý21ý28ý2ý29ý15ý16ý20ý23ý24ý25ý30ý31ý33ý3ý32ý34ý17ý18ý14ý10ý8ý1ý36ý37ý5ý6ý35ý12ý4',
                  # for commit purposes
}
pp.pprint(rbo_properties)
print(rbo_properties['memberName'])
