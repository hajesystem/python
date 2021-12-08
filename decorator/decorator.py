# decorator를 한마디로 얘기하자면, 대상 함수를 wrapping 하고,
# 이 wrapping 된 함수의 앞뒤에 추가적으로 꾸며질 구문 들을 정의해서 손쉽게 재사용 가능하게 해주는 것이다

from functools import wraps


def decorator_normal(fn):
    def wrapper():
        print("decorator_normal ==> start")
        fn()
        print("decorator_normal ==> end")
    return wrapper


#  @wraps어노테이션
# 데코레이터 내부에서 인자로 전달받은 함수가 익명함수 처럼 취급되어 버리므로 디버깅이 난해해지는 단점이 있었기 때문이다.


def decorator_wraps():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            print("decorator_wraps ==> start")
            w_value = False
            if(w_value):
                return fn(*args, **kwargs)
            else:
                return print("decorator_wraps ==> false")
        return decorator
    return wrapper
