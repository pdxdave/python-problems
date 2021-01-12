def csIsomorphicStrings(a, b):
    
    if len(a) != len(b):
        return False
    dic={}
    for i,x in enumerate(a):
        if x in dic.keys() and dic[x]!=b[i]:
            return  False
        elif x not in dic.keys() and b[i] in dic.values():
            return False
        else:
            dic[x]=b[i]
                
    return True
    
  
a = "add"
b = "egg"
print(csIsomorphicStrings(a, b))