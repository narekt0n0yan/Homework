def str_to_dict(string):
    string_to_dict = {}
    for i in string:
        if i in string_to_dict:
            string_to_dict[i] += 1
        else:
            string_to_dict[i] = 1
    return string_to_dict


print(str_to_dict("hello"))  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
