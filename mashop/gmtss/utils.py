def rbo_results2dict(rbo_properties, cm):
    """
    Takes a dictionary of rbo_properites (key:value (sv, mv & svm) and a conversion map (cm) and converts:
        1. single value rbo properties to a simple key:value (converting string to json type as indicated in the cm
        2. groups of associated multi-value properties based on the structure in the cm (convertibg string to json
               type as indicated in the cm)
        3. sub groups of associated sub-value properties for a given multi-value based on the structure in the cm
    """
    rbo_vm = 'ý'
    rbo_svm = 'ü'
    cd = {}  # converted data to be returned
    for key in cm['sv']:
        # note: the eval funtion will evaluate a '12/12/17' as a math division and not as a string
        if cm['sv'][key]['json_type'] != 'str':
            cd[key] = eval(cm['sv'][key]['json_type'] + '(' + rbo_properties[cm['sv'][key]['rbo_name']] + ')')
        else:
            cd[key] = rbo_properties[cm['sv'][key]['rbo_name']]

    # convert @vm dynamic arrays to python lists for each rbo property
    for group_master_key in cm['mv_groups']:
        uv_values = {}
        # uv_values[group_master_key] = rbo_properties[cm['mv_groups'][group_master_key]['rbo_name']] \
        #     .split(rbo_vm)
        for assoc_item_key in cm['mv_groups'][group_master_key]:
            uv_values[assoc_item_key] = rbo_properties[cm['mv_groups'][group_master_key]
            [assoc_item_key]['rbo_name']].split(rbo_vm)
        cd[group_master_key] = []
        group_dict = {}
        for i, val in enumerate(uv_values[group_master_key]):
            # group_master_key_val = str(uv_values[group_master_key][i])
            # cd[group_master_key][group_master_key_val] = {}
            for assoc_item_key in cm['mv_groups'][group_master_key]:
                # does this associated key have any associated sub values?
                # if so then using the base rbo_property assign this rbo_property's values as kv pairs under
                # this associated item.  (huh???????  :)  )
                if 'associations' in cm['mv_groups'][group_master_key][assoc_item_key]:
                    cd[group_master_key][group_master_key_val][assoc_item_key] = {}
                    keys_from_uv_property = rbo_properties[
                        cm['mv_groups'][group_master_key]['associations'][assoc_item_key]['associations'][
                            'rbo_name']].split(rbo_vm)
                    for keyj, valj in enumerate(keys_from_uv_property):
                        sub_values = uv_values[assoc_item_key][i].split(rbo_svm)
                        #TODO: cast rbo values (strings) to json_types as indicated in the cm
                        cd[group_master_key][group_master_key_val][assoc_item_key][valj] = sub_values[keyj]
                else:
                    uv = uv_values[assoc_item_key][i]
                    jt = cm['mv_groups'][group_master_key][assoc_item_key]['json_type']
                    if cm['mv_groups'][group_master_key][assoc_item_key]['json_type'] != 'str':
                        # note: the eval funtion will evaluate a '12/12/17' as a math division and not as a string
                        json_type_value = eval(jt + '(' + uv_values[assoc_item_key][i] + ')')
                        group_dict[assoc_item_key] = json_type_value
                    else:
                        group_dict[assoc_item_key] = uv_values[assoc_item_key][i]
            cd[group_master_key].append(group_dict)
    return cd
