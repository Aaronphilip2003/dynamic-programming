dict_sum={0:0,1:1,2:3}


def recSum(n):
    
    if n in dict_sum:
        return dict_sum[n]
    
    if n==1:
        return n
    
    dict_sum[n]=n+recSum(n-1)
    
    print(dict_sum)
    
    return dict_sum[n]

print(recSum(4))