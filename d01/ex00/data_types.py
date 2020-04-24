def data_types():
    types_ = [int, str, float, bool, list, dict, tuple, set]
    ar_of_types = [x() for x in types_]
    print(ar_of_types)
    return ar_of_types

if __name__ == "__main__":
    data_types()