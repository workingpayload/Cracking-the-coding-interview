def check(s):
    l = s.split()
    new_s = "".join(l)
    dicti = {}

    for i in new_s:
        if i in dicti:
            dicti[i]+=1
        else:
            dicti[i]=1

    count = 0

    for values in dicti.values():
        if values%2!=0:
            count+=1

    if count>1:
        return False
    else:
        return True
