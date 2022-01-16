dict={0:0,1:1}

def fib(n):
    if n in dict:
        return dict[n]
    dict[n]=fib(n-1)+fib(n-2)
    
    print(dict)
    
    return dict[n]

print(fib(7))