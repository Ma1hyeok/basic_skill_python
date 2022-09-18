### 기본 형태

def hello(world):
    val = "Hello" + str(world)
    return val 



### 다중 리턴

def multiple(x):
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000

    return y1,y2,y3

# val1, val2, val3 = multiple(11)
# print(val1,val2,val3)



### *args, *kwargs 의 사용
### *args 의 경우 tuple 형태로 반환함
def args_func(*args):

    for i, v in enumerate(args):
        # index 를 붙여주는 함수
        print(i,v)

# args_func('jo','a','kim','me')


### **kwargs 의 경우, dict 형태로 반환함
def kwargs_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)


#kwargs_func(name1 = 'ma', name2 = "park")

### 정리 - 조합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

# example_mul(10,20)
# example_mul(10,20,"park","kim",age1= 24, age2 =29)



### 중첩 함수(클로저 = closure)
### = 함수안에 함수가 있는 것

def nested_func(num):
    def func_in_func(num):
        print('>>>>>',num)
    # print("in_func")
    # func_in_func(num+10000)


#nested_func(10000)


### hint 만들기
def multiple_2(x : int) -> list:#입력값과 출력값이 나오는 것을 이렇게 줄 수 있음.
    y1 = x * 100
    y2 = x * 1000
    y3 = x * 10000
    return y1,y2,y3

#print(multiple_2(5))


# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_fucn = mul_10

# print(var_fucn)
# print(type(var_fucn))
#val_fucn에 메모리가 할당됨을 확인 가능


#람다식
lambda_mul_10 = lambda num: num*10

print(">>>",lambda_mul_10(10))


# 함수의 조합
def func_final(x,y,func):#매게변수로 함수를 받는 함수
    print( x * y * func(10))

#func_final(10,10,lambda_mul_10)#labmda_mul_10의 리턴값인 100을 받아온다.


#print(func_final(10,10,lambda x : x * 1000)) #함수안에 바로 람다함수를 만들 수도 있음.
#93줄 func(10)을 받아 1000*10을 반환하고, 10*10*10000 하여 100만이 나온다.
#참고로 none은 프린트문에 더 출력할게 없을때 나옴


z = 3

def outer(x):
        y = 10
        def inner():
            x = 1000
            return x

        return inner()

print('<<<<',outer(10))