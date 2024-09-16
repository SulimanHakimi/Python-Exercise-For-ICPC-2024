n = int(input())

def fib(n):
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return fib(n - 1) + fib(n - 2)


for _ in range(n):
    data = int(input())
    # fibonacci of (n)
    print(fib(data))




'''
f(0) =
f(1) = 1
0, 1, 1, 2, 3, 5, 8, 13, ...
fib(n) = fib(n - 1) + fib(n - 2)


'''