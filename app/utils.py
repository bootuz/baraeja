def replace_chars(string, to_be_replaced = 'iIlL1|'):
    if string[0] in to_be_replaced:
        string = 'Ӏ' + string[1:]
    for i in to_be_replaced:
        if i in string:
            string = string.replace(i, 'ӏ')
    return string
