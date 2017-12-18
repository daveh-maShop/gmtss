def dsb2dict(refmap, refvals, cd):
    x = refvals  # for debug purposes, debug window doesn't show refmap
    for k, v in refmap.items():
        if k == 'association' and isinstance(v, dict):
            dsb2dict(refmap, refvals, v)
        else:
            print(k, v)
        cd[k] = refvals[map[k]['rbo_name']]
    return cd

    result = process(refmap, {})
    print(result)
