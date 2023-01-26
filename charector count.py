def most_frequent(str):
    d = dict()
    for key in str:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print(most_frequent('mississippi'))