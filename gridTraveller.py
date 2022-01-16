dict={'1,2':1}

def gridTraveller(m,n):
    key=f"{m},{n}"
    if key in dict:
        return dict[key]
    if (m==1 and n==1):
        return 1
    if (m==0 or n==0):
        return 0
    
    dict[key]=gridTraveller(m-1,n)+gridTraveller(m,n-1)
    
    print(type(key))
    
    return dict[key]

print(gridTraveller(10,10))