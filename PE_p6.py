import numpy as np

#Problem 6

n = 3

def sumofsquares(n):
    if n == 1:
        return 1
    return n*n + sumofsquares(n-1)

def squareofsums(n):
    sum = n*(n+1)//2
    return sum*sum

number = 100
answer = squareofsums(number) - sumofsquares(number)
print("Square of sum minus sum of squares : ", answer)
