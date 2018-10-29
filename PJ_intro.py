import numpy as np
#Problem 1
sum1 = 0

for x in range(0,1000):
  if (x%3 == 0) or (x%5 == 0):
    sum1+=x

print("Sum is equal to:", sum1)

#Problem2

sum2 = 2
fib1 = 1
fib2 = 2
fib = 0
while fib <= 4E+6:
    fib = fib1 + fib2
    if fib%2 == 0:
        sum2+=fib

    fib1 = fib2
    fib2 = fib

print("Fib sum is:", sum2)

#Problem3

def isPrime(n):
    result  = True
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while (i*i) <= n + 5:
        if n % i == 0:
            result = False
            return result
        i = i + 2
    return result

def primefactor(n1):
    n1_part = n1
    maxprimefactor = 0
    idx = 2
    while idx <= n1_part // 2 + 1:
        if isPrime(n1_part):
            if n1_part > maxprimefactor:
                maxprimefactor = n1_part
                return maxprimefactor
        if n1_part % idx == 0 and isPrime(idx):
            n1_part = n1_part//idx
            if idx > maxprimefactor:
                maxprimefactor = idx
            idx = 1
        idx = idx + 1
    return maxprimefactor

nbr = 600851475143
res = primefactor(nbr)
print("Is ", nbr, " prime? ", isPrime(nbr))
print("Greatest prime factor of ", nbr, " is: ", res)
