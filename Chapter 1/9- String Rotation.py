def issubstring(s,ti):
    if s in ti:
        return True
    else:
        return False

def check(s,ti):
    n = len(s)

    if len(ti)>0 and n>0:
        new_s = s+s
        return issubstring(ti,new_s)
    else:
        return False
