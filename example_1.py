from collections import defaultdict


def set_default_example():
    dflt_dict = defaultdict(list)
    for k, v in enumerate(range(5)):
        dflt_dict[k].append(v)
    return dflt_dict

new_dict = set_default_example()

print(new_dict)