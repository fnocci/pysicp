def factorial(n):
    if n<0: return None
    if n==0: return 0
    if n==1: return 1
    return n * factorial(n-1)

memo = {0:0, 1:1}

def mfact(n):
    if n<0: return None
    if n in memo: return memo[n]
    memo[n] = n * mfact(n-1)
    return memo[n]
    
