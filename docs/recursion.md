## Factorial

```py linenums="1"
def factorial(n):
    if n in [0, 1]:
        return n
    return n * factorial(n-1)

print(factorial(5)) # 5! = 120
```

## Fibonacci

```py linenums="1"
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5)) # 0 1 1 2 3 5 = 5
```

## Product of two nums

```py linenums="1"    
def product(num):
    if num == 1:
        return num
    rem = num % 10
    return rem * product(num // 10)

print(product(123)) # 1*2*3 = 5
```

## GCD of two nums

```py linenums="1"   
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

print(gcd(48, 18))  # gcd(48, 18) = 6
```

## Decimal to Binary

```py linenums="1"
def decimal_to_binary(quot, rem):
    if quot == 0:
        return rem
    quot = num // 2
    rem = num % 2
    return decimal_to_binary(quot)

print(decimal_to_binary(10//2, 10 % 2))
```

## Power of number
```py linenums="1"
def pow(base, exponent):
    if exponent == 0:
        return 1
    return base * pow(base, exponent-1)

print(pow(2, 4))  # 2*2*2*2 = 16
```
 

