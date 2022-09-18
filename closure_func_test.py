def in_cache(func):
    cache = {}
    def wrapper(n):
        print(cache) ## !!!!
        if n in cache:
            return cache[n]
        else:
            cache[n] = func(n)
            return cache[n]
    return wrapper


def factorial(n):
    ret = 1
    for i in range(1, n+1):
        ret *= i
    return ret

factorial = in_cache(factorial)
# cache의 변수를 저장


print(factorial(3))
print(factorial(5))
print(factorial(10))
print(factorial(11))