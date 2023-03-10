def func(l):
  for i in range(0,len(l)):
    for j in range(0,i):
      l[i][j],l[j][i]=l[j][i],l[i][j]
      
  for k in range(0,len(l)):
    l[k] = l[k][::-1]
    
    
