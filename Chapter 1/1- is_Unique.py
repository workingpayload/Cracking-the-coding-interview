def check(s):
  if len(s)>128:
    return False
  
  new_l = [None]*128
  
  for i in s:
    if new_l[ord(i)]:
      return False
    else:
      new_l[ord(i)]=i
      
  return True   
    
