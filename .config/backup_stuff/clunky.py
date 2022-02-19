def update_cfg(cfg, host):
    f = open(host, 'r')
    lines = f.readlines()
    cfg_arr = []
    for line in lines:
        key = line.split('=')[0]
        value = line.split('=')[1]
        cfg_arr.append([key.strip('\n'), value.strip('\n')])
    for key in cfg.keys():
        for line in cfg_arr:
            if key == line[0]:
                cfg[key] = line[1]
    return cfg
