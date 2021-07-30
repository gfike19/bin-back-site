def conv(string):
    string = string[1:]
    lst = []
    lst.append(string[0:2])
    lst.append(string[2:4])
    lst.append(string[4:6])
    rgb = (int(lst[0],16), int(lst[1],16), int(lst[2],16))
    return rgb