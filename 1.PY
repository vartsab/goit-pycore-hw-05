def caching_fibbonaci():
    #declare an empty dictionary for caching the results
    cache = {}

    def fibbonacci(n):
        if n <= 0:
            return 0
        elif n ==1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            result = fibbonacci(n - 1) + fibbonacci(n - 2)
            cache[n] = result
            return result
    
    return fibbonacci

fib = caching_fibbonaci()
print(fib(10))
print(fib(15))
