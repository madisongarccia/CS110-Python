def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
       

def sum_recursively(n):
    if n ==0:
        return 0
    else:
        return n+sum_recursively(n-1)

def sumlist_recursively(l):
    if len(l)==1:
        return l[0]
    else:
        return l[0] + sumlist_recursively(l[1:])

def multiply_recursively(x, y):
    if y==1:
        return x
    else:
        return x+multiply_recursively(x,y-1)


def reverse_recursively(l):
    if len(l) == 0: 
        return []
    else:
        return [l[-1]] + reverse_recursively(l[:-1])

    
