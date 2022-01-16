dict_fact={0:1,1:1,2:2,3:6}

def recFact(n):
    
    if (n in dict_fact):
        return dict_fact[n]
    
    if n==1:
        return 1
    
    dict_fact[n]=n*recFact(n-1)
    
    print(dict_fact)
    
    return dict_fact[n]

print(recFact(10))