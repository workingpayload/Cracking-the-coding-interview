def check(s):
    new_s = ""
    stack = []
    for i in range(0,len(s)):

        if i == len(s)-1:
            if s[i]==s[i-1]:
                stack.append(s[i])
                new_s+=str(len(stack))
                new_s+=s[i]
            else:
                new_s+="1"
                new_s+=s[i]
            break

        if s[i]==s[i+1]:
            stack.append(s[i])
        else:
            stack.append(s[i])
            new_s+=str(len(stack))
            new_s+=s[i]
            stack = []

    if len(s)==new_s:
        return s
    else:
        return new_s
