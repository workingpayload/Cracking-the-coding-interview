def issubstring(s,t):
    if s in t:
        return True
    else:
        return False

def check(s,t):
    n = len(s)

    if len(t)>0 and n>0:
        new_s = s+s
        return issubstring(t,new_s)
    else:
        return False
