def check(s):
    p = ""
    news =s.strip()

    for i in news:
        if i==" ":
            p+="%20"
        else:
            p+=i

    return p
