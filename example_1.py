def set_default_example():
    std_dict = dict()
    for k, v in enumerate(range(5)):
        std_dict.setdefault(k, []).append(v)
    return std_dict

new_dict = set_default_example()

print(new_dict)