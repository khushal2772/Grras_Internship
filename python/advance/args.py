def sum(**args):  # args is a value that contain all the values in the form of tuple
    total = 0
    for item in args:
        total += item
    return total

print(sum(31,12,123))