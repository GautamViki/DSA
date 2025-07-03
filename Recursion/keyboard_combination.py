def get_keyboard_combinations(keys,key_list):
    if len(keys)==0:
        return [""]
    num = keys[0]
    subkeys = keys[1:]
    constructed_str = get_keyboard_combinations(subkeys,key_list)
    res = []
    for char in key_list[int(num)]:
        for str in constructed_str:
            res.append(char+str)
    return res

key_list = ['?!','abc','def','ghi','ijk','lmn','opq','rst','uvw','xyz']
words = get_keyboard_combinations('03',key_list)
print(words)