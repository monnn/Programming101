def group_by(func, seq):
    dictionary = {}
    for element in seq:
        dictionary.update({func: element})
