"""The Fibonacci sequence is a series of numbers in which each number is the sum of the two 
preceding ones, usually starting with 0 and 1. It is often used in algorithm examples, and 
is defined by the following formula: F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1.

Your task is to implement the Fibonacci algorithm in three different methods: 1. Recursively 2. Iteratively 3. Using Memoization"""

n = 2
# Using recursive function
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

print(f"F({n}) =", fibonacci_recursive(n))

# Using Iterative function
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n]

print(f"F({n}) =", fibonacci_iterative(n))

#Using Memoization
def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 0:
        memo[n] = 0
    elif n == 1:
        memo[n] = 1
    else:
        memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]

print(f"F({n}) =", fibonacci_memoization(n))

# Using Memoization
"""> if value is in cache, return it
    > compute the nth term 
    > cache the value and return it"""
def fibonacci_memoization2(n):
    # create cache
    fibonacci_cache = {}
    
    # check cache for n
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    
    # Compute Fibonacci for n
    if n <= 0:
        value = 0
    elif n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci_memoization2(n-1) + fibonacci_memoization2(n-2)
        
    # Add Value to Cache and return
    fibonacci_cache[n] = value
    return value
print(f"F({n}) =", fibonacci_memoization2(n))