def capitalize (str):
    new_str = list(str)
    for i in range(len(new_str)):
        if i == 0 or (new_str[i] == 'i' and new_str[i-1] == ' ' and new_str[i+1] == ' '):
            new_str[i] = new_str[i].upper()
        if (new_str[i-2] == ('!') or new_str[i-2] == ('.') or new_str[i-2] == ('?')) and (new_str[i-1] == ' '):
            new_str[i] = new_str[i].upper()
        if (new_str[i-1] == ('!') or new_str[i-1] == ('.') or new_str[i-1] == ('?')):
            new_str[i] = new_str[i].upper()

    return ''.join(new_str)

print(capitalize("huh?hahaha"))