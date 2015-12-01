import re

def get_names(text):
    names = re.findall('[A-Z][a-z]+ [A-Z][a-z]+', text)
    nameset = list(set(names))
    for i in range(len(nameset)):
        nameset[i] = (names.count(nameset[i]), nameset[i])
    print nameset[0]
    return sorted(nameset, key=lambda name: name[0], reverse=True) 
    