######################################
# fibonacci series
######################################

# recursive 
def fib(n):
    if n < 0: return None
    if n == 0: return 0
    elif n == 1: return 1
    else: return fib(n-1)+fib(n-2)

# memoized recursive
memo = {0:0, 1:1}
def mfib(n):
    if n < 0: return None
    if n in memo: return memo[n] 
    memo[n] = mfib(n-1)+mfib(n-2)
    return memo[n]
