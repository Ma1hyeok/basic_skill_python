# def in_cache(func):
#     cache = {}
#     def wrapper(n):
#         print(cache,n) ## !!!!
#         if n in cache:
#             return cache[n]
#         else:
#             cache[n] = func(n)
#             return cache[n], print(cache[n],"here",func(n),n) ## !!!!
#     return wrapper


# def factorial(n):
#     ret = 1
#     for i in range(1, n+1):
#         ret *= i
#     return ret

# factorial = in_cache(factorial)
# # cache의 변수를 저장


# factorial(3)
# factorial(5)
# # print(factorial(10))
# # print(factorial(11))



def times_multiply(n):
    def multiply(x):
        print(x)
        return n * x
    return multiply


times_3 = times_multiply(3)
times_4 = times_multiply(4)

print(times_3(5))
print(times_4(5))
