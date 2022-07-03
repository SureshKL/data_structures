def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    if n in [0, 1]:
        return n
    return n * factorial(n-1)
    
def product(num):
    if num == 1:
        return num
    rem = num % 10
    return rem * product(num // 10)
        
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


def decimal_to_binary(quot, rem):
    if quot == 0:
        return rem
    quot = num // 2
    rem = num % 2
    return decimal_to_binary(quot)

print(decimal_to_binary(10//2, 10 % 2))
    
    
print(product(123)) # 1*2*3 = 5
print(factorial(5)) # 5! = 120
print(fibonacci(5)) # 0 1 1 2 3 5 = 5
print(gcd(48, 18))  # gcd(48, 18) = 6

"""
Recursion

Factorial n * n-1
Fibonacci
Product of numbers
GCD of two numbers

"""
