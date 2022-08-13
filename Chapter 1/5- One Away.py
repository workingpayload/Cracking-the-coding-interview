def solve(s,t):
    if len(s)==len(t):
        return replace(s,t)
    elif len(t)+1==len(s):
        return insert(t,s)
    elif len(s)+1==len(t):
        return insert(s,t)
    else:
        return False

def replace(s,t):
    count = 0
    for i in range(0,len(s)):
        if s[i]!=t[i]:
            count+=1
    if count>1:return False
    else:return True

def insert(s,t):
    new_string = ""
    count = 0
    for i in range(0,len(s)):
        if s[i]==t[i]:
            new_string+=s[i]
        else:
            count+=1
            if count>1:
                return False
            new_string+=t[i]
    new_string+=t[-1]
    if new_string==t:return True
    return False



