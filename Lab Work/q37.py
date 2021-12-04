def char_frequency(str1):
    d = {}
    for n in str1:
        keys = d.keys()
        if n in keys:
            d[n] += 1
        else:
            d[n] = 1
    return d
print(char_frequency('google.com'))