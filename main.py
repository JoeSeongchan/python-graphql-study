from flask import Flask

# __name__ : 모듈의 이름
# 실행하는 코드에서는 __main__ 값이 들어간다.
# 모듈로서 실행하는 게 아니라면 __main__이 출력된다.
# 다른 파이썬 코드에 import해 온다면 파일 이름이 __name__이 들어간다.
# 파일 자체를 실행시킨다면 메인 코드로, 스크립트로 실행된다.
# Python에서 디폴트로 설정해주는 값이다.
# 스크립트 언어 = Unix 운영체제에서 온 언어. 목적에 맞는 아주 간단한 프로그래밍 언어
# 스크립트 언어는 전통적으로 시작점이 없다. (main 같은 함수가 없다.)
# 모듈로 실행될 때 vs 스크립트로 실행될 때
# 가장 기본적으로 Flask에는 __name__ 이 넘어간다.
app = Flask(__name__)


# URL : 인터넷 상의 자원 표기를 위한 규약.
# WWW 주요 요소 중 하나 : HTML, URL, HTTP
# 웹 상의 자원을 URL로 지칭한다.
# URI = 통합 자원 식별자
# 전체를 나타내는 것은 uri
# 라우팅까지 들어가는 건 url, 쿼리 문자열까지 포함하는 건 uri
# 웹 애플리케이션 서버에는 라우팅이 필요하다.

@app.route('/hello') # 파이썬의 데코레이터
def hello():
    return "<h1>Hello World</h1>"

# 웹 서버를 어떻게 구동시킬 것인가? 자체적으로 웹 서버를 지원한다.
# run(host=None, port=None, debug=True) 상용화 프로그램에서는 별도의 웹 서버를 둔다

host_addr = "0.0.0.0"
port_num = "8080"
if __name__ == "__main__":
    app.run(host=host_addr,port=port_num,debug=True)

'''
웹 서버는 정적인 html 페이지를 반환한다. 미리 작성되어 있는 페이지를 리턴한다. 
동적으로 데이터를 반환하기 위해서는 was 프레임워크가 필요하다
flask는 was 프레임워크이다. 웹 서버도 가지고 있다. 
python xxx.py 로 실행한다. 
'''

'''
데코레이터는 단지 파이썬 flask 뿐만 아니라 다양한 언어 전반에 걸쳐서 많이 사용된다. 
언어 절반에 걸친 데코레이터 관련 기술을 이해해야 한다. 
중첩 함수에 대해 이해해야 한다. 함수 정의를 함수 안에서 한다. 
중첩 함수는 정의된 함수 내에서만 호출될 수 있다. 밖에서는 직접 호출할 수 없다. 
Stack, Heap, Data, Code 영역으로 메모리를 나눈다.
Data : 변수
Code : 코드
Heap : 동적으로 생성되는 객체
Stack : 함수 호출 스택 

중첩 함수를 밖에서 호출할 수 있는 방법이 있다. First-class와 closure에 대해
이해하고 있어야 한다. 함수 안에서 정의한 함수를 리턴할 수 있다. 
First-class function과 Closure 호출에 대한 개념을 이해해야 한다. 
'''

'''
일급 함수 
- 함수 자체를 변수에 저장 가능 
- 함수의 인자에 다른 함수를 인수로 전달 가능 
- 함수의 반환 값으로 함수를 전달 가능
파이썬에서 함수는 객체이기 때문이다! 파이썬의 함수는 First-Class 함수가 되기 위한 
모든 조건을 만족한다. 함수형 프로그래밍에서부터 고안된 기법이다.
중첩 함수 안에 들어간 로컬 변수는 그대로 살아있다. (클로저)
이런 걸 응용할 수 있다. '{0} {1} {2}'.format(req1,req2)
'''

'''
클로저 함수
- 함수와 해당 함수가 가지고 있는 데이터를 함께 복사, 저장해서 별도 함수로 활용
- 외부 함수가 소멸되더라도, 외부 함수 안에 있는 로컬 변수값과 중첩 함수를 사용할 수 있다. 
언제 클로저를 사용할까? 
제공해야 하는 메서드가 적은 경우. Java의 람다와 비슷하구나!
핵심 : 파이썬에서 함수는 객체이다! 일급 객체

데코레이터 문법 : 일급 함수 + 클로저 함수 
'''

'''
파이썬 데코레이터
First class Function과 Closure Function을 조합해서 구현
함수 앞 뒤에 기능을 추가해서 손쉽게 함수를 활용할 수 있는 기법
Spring의 AOP와 같은 기능. 
'''

# def datetime_decorator(func):
#     def wrapper():
#         print('time '+str(datatime.datetime.now()))
#         func()
#         print('exit')
#     return wrapper;

'''
한번에 데코레이터로 작성할 수 있다.
@outer_func
def log_func():
    print()

데코레이터가 붙은 함수의 파라미터가 outer_function 안에 있는 inner_function
에 전달된다. 
유효성 검사와 같은 것을 데코레이터로 해결할 수 있다. 도메인 로직과 기타 로직을 분리한다. 
다양한 개수의 파라미터를 받으려면 
*args, **kwargs 를 써라. 
Method Decoator : 클래스의 메서드에도 데코레이터를 붙일 수 있다. 
모든 파이썬 클래스의 메서드는 첫번째 인자가 self이기 때문에 데코레이터의 파라미터에도
self 인자를 꼭 넣어줘야 한다. 
'''

'''
python format 함수
print('{} {}'.format(10,100))
print('{aa} {bb}'.format(aa=10, b==20))
'''

'''
데코레이터 자체에도 인자를 줄 수 있다. 중첩 단계를 하나 더 추가한다. 
def decorator1(num):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            ...
            return function(*args, **kwargs)
            
@decorator(1)으로 데코레이터를 붙일 수 있다.

** 정리 : first class function과 closure function을 조합해서 만들었다.  
'''

@app.route("/")
def hello1():
    return "<h1>Hello World! 1</h1>"

# path variable
@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello "+username+"</h3>"

# data 타입 지정 가능
@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" %message_id # 독특한 문법. format




