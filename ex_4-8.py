def forte(passwd):
    if len(passwd) < 8:
        return False
    
    tem_upper = False
    tem_lower = False
    tem_numero = False
    
    for i in passwd:
        if i.isupper():
            tem_upper = True
        elif i.islower():
            tem_lower = True
        elif i.isdigit():
            tem_numero = True
    return tem_upper and tem_lower and tem_numero

print(forte("9EwL56"))
print(forte("ffu4G7Fghjk"))
