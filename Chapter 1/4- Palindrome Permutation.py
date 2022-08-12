def check(s):
    l = s.split()
    new_s = "".join(l)
    dic = {}

    for i in new_s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1

    count = 0

    for values in dic.values():
        if values<2:
            count+=1

    if count>1:
        return False
    else:
        return True
