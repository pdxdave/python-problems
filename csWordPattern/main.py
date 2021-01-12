def csWordPattern(pattern, a):
    
    strs = a.split()
    
    if len(pattern) != len(strs):
        return False
        
    d = dict()
    for i, p in enumerate(pattern):
        if p not in d:
            d[p] = strs[i]
        else:
            if d[p] != strs[i]:
                return False
                
    for i, p in enumerate(strs):
        if p not in d:
            d[p] = pattern[i]
        else:
            if d[p] != pattern[i]:
                return False
    return True
    
    
pattern = "abba"
t = "lambda school school lambda"
print(csWordPattern(pattern, t))