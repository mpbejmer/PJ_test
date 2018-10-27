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
