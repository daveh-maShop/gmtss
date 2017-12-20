def dsb2dict(refmap, refvals, cd):
    # x = refvals  # for debug purposes, debug window doesn't show refmap
    for k, v in refmap.items():
            print(k, v)
            if isinstance(v, dict):
                dsb2dict(v, refvals, cd)
            else:
                cd[k] = refvals[refmap[k]['rbo_name']]
