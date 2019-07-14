#!/usr/bin/env python3
#
###########################################
# primes -- multiple ways of calculating lists of primes up to N
###########################################
#

import argparse
parser = argparse.ArgumentParser()

parser.add_argument("N")
args = parser.parse_args()
print (args.N)


###########################################
# Sieve of Eratosthenes
#..........................................
#
# make a table of non-primes up to sqrt(N)
# it will have repeats, so cast as set
#
# pop quiz: what is the computational complexity of the sieve?
#
###########################################

from math import sqrt

N = int(args.N) 

# calculate sieve with nested for loops
def sieve (N): 
    sieve_set = set()

    for i in range (2,int(sqrt(N))):

        for j in range (i*2, N,i):

            sieve_set.add (j)

    return sieve_set

sieve_set1 = sieve(N)

print([x for x in range (2,N) if x not in sieve_set1])

# if we were to call sieve(N) from the list comprehension, wouldn't it be called N times?
# calculate sieve with list comprehension

sieve_set2 = {j for i in range(2, int(sqrt(N))) for j in range (i*2, N, i)}

print([x for x in range (2,N) if x not in sieve_set2])


###########################################
# Algorithms from SICP
###########################################
# https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-11.html#%_sec_1.2
#..........................................
# 	Smallest Divisor
#..........................................
#
# (define (smallest-divisor n) (find-divisor n 2))
#
# (define (find-divisor n test-divisor)
#  (cond ((> (square test-divisor) n) n)
#        ((divides? test-divisor n) test-divisor)
#        (else (find-divisor n (+ test-divisor 1)))))
#
# (define (divides? a b) (= (remainder b a) 0))
#
# n is prime if and only if n is its own smallest divisor.
#
#(define (prime? n) (= n (smallest-divisor n)))
#
#  True or False?
#
#   cc = O(sqrt(n)) to test one prime n
#   cc = O(N sqrt(N)) to test N primes?
#
###########################################

def find_divisor (n, test_divisor):
    if (test_divisor**2 > n): return n

    elif (n%test_divisor == 0): return test_divisor

    else: return find_divisor (n, test_divisor + 1)

divisor_primes = [i for i in range(2,N) if find_divisor(i,2) == i] 

print ('primes from 2 to {} by find smallest divisor method'.format(N))
print (divisor_primes)

###########################################
#
#  Fermat's Little Theorem: If n is a prime number and a is any positive integer less than n, 
#                           then a raised to the nth power is congruent to a modulo n.
#
#..........................................
#          Fermat Test 
#..........................................
#
# Two numbers are said to be congruent modulo n if they both have the same remainder when divided by n. 
# The remainder of a number a when divided by n is also referred to as the remainder of a modulo n, or simply as a modulo n.
#
# If n is not prime, then, in general, most of the numbers a< n will not satisfy the above relation. 
# This leads to the following algorithm for testing primality: Given a number n, pick a random number a < n 
# and compute the remainder of an modulo n. If the result is not equal to a, then n is certainly not prime. 
# If it is a, then chances are good that n is prime. Now pick another random number a and test it with the 
# same method. If it also satisfies the equation, then we can be even more confident that n is prime. 
# By trying more and more values of a, we can increase our confidence in the result. Here w try 3 times.
#
#   cc = O(ln2 n)? Really? 
#
###########################################

from random import randint

def fermat_test (n):  
    a = randint (1,n)
    if (a**n)%n == a%n: return True
    else: return False

fermat_primes = [i for i in range(2,N) if fermat_test(i) and fermat_test(i) and fermat_test(i) and fermat_test(i)]

print ("Successive approximations to the primes between 2 and {}:".format(N))
print ("1 test:    ",[i for i in range(2,N) if fermat_test(i)])
print ("2 tests:   ",[i for i in range(2,N) if fermat_test(i) and fermat_test(i)])
print ("3 tests:   ",[i for i in range(2,N) if fermat_test(i) and fermat_test(i) and fermat_test(i)])
print ("4 tests:   ",fermat_primes)
print ("THE TRUTH: ",divisor_primes)

print ("Mistakes:  ",[i for i in fermat_primes if i not in divisor_primes])
