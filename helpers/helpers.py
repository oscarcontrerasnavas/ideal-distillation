def to_dict(items):
    dictionary = {}
    for item in items:
        dictionary[item.tag] = item
    return dictionary

def get_names(items):
    names = []
    for item in items:
        names.append(item.name)
    return names

def name_to_tag(name):
    return name.lower().replace(' ', '_')