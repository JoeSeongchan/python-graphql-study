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

'''
flask로 REST API 구현하기
HTTP는 Connectionless한 프로토콜이다. 1회성 Request, Response
TCP, IP socket을 이용해서 연결된다.
 
- Http method | Path | Http 버전 -> Http Request Line 
- Host | Connection -> Http Request Header
    서버에 요청을 하고, 응답을 받는다. 1회성 연결을 한다. Request를 많이 할 때마다
    연결을 계속 만들면 비효율적이다. 연결을 재사용할 수도 있다. 
    Connection: keep-alive 로 연결을 재사용한다. 
Request Line + Request Header = Header (택배의 송장 역할)
 
Http Request Body

Response 
Http 버전 | Status Code | Status Message | Server-> Http Response Line
Content-type | Content-length -> Http Response Header
Http Response Body

Http Method = 요청을 하는 방법
요즘 대부분은 REST API 방식으로 데이터를 제공한다. 
rest api는 http method를 쓴다. 
create : 생성 (post)
read : 조회 (get)
update : 수정 (put)
delete : 삭제 (delete)
crud를 구현할 줄 알아야 한다. 기본적인 제한 사항을 알고 있어야 한다. 
마이크로 서비스, OpenAPI (누구나 사용하도록 공개된 API) 에서 많이 사용된다. 
REST = Representational State Transfer
'''

'''
특정한 URI를 요청하면 JSON 형식으로 데이터를 반환하도록 만든다. 
Flask에서는 dict(사전) 데이터를 응답 데이터로 만들고, 이를 jsonify()
메소드를 활용해서 JSON 응답 데이터로 만들 수 있다. json은 RESTAPI와 뗄레야
뗄 수 없다. httpie 설치해서 REST API 테스트해보자
예전에는 Postman을 많이 썼다. 요즘에는 이런 간단한 Tool을 쓴다.
pip install --upgrade httpie

http GET http://localhost:8080/json_test

http -v GET http://localhost:8080/json_test 
 => 요청 헤더까지 같이 볼 수 있다. `-v` 옵션
flask의 jsonify 메서드에 Dict를 제공하면 자동으로 JSON으로 변환한다. 
from flask import Flask, jsonify
jsonify(Dict 객체)
'''

'''
파이썬 virtual env
파이썬이 불안정했을 때, 각 라이브러리의 파이썬 버전별 호환성 이슈가 많았다. 
안에서만 동작할 수 있도록 하는 가상 환경
'''

'''
백엔드와 프론트엔드를 Flask로 개발
Flask 안에서 파라미터를 가져오려면 request 객체를 써야 한다. 
'''
from flask import request,jsonify
@app.route("/login")
def login():
    username = request.args.get("user_name")
    if username == "dave":
        return_data = {'auth':'success'}
    else:
        return_data = {'auth':'failed'}
    return jsonify(return_data)
'''
query string의 맨 처음에는 ?를 넣는다. 
'''

'''
flask cors 지원 
pip install flask_cors
from flask_cors import CORS
CORS(app)

CORS : Cross Origin Resource Sharing
웹에서 사용하는 HTTP Request는 다른 웹 사이트의 자원을 요청할 수 있다. 
태그로 이미지는 보여줄 수 있지만 스크립트 태그로 둘러싸인 스크립트 코드에서
실행되는 HTTP request는 동일한 서버에만 할 수 있다. 
정확히는 프로토콜, 호스트명, 포트가 동일해야 한다. Same Origin Policy라고 부른다. 
CORS 메서드 : 전 요청 / 응답 헤더에 CORS 지원 헤더 정보를 넣는다. 
'''

'''
make_response(jsonify(success=True), 200) 
성공 여부만 표현해도 될 때, 이렇게 쓴다. 
200 : 정상
400 : 유효하지 않은 파라미터
401 : 승인되지 않은 액세스. 401 vs 403
403 : 액세스 금지
404 : 리소스를 찾을 수 없음 
500 : 내부 서버 오류

make_response를 사용해서 status code를 지정하여 넣을 수 있다. 
'''

'''
@app.route("/test", methods=["GET","POST","PUT","DELETE"])
=> 라우팅 경로로 들어오는 method를 위와 같이 제한할 수 있다. 
HTML에서는 put과 delete가 아예 지원이 안 됨 (form으로...)
request.method로 요청의 HTTP METHOD를 확인할 수 있다. 
post method의 데이터는 request.get_json()으로 가져온다.
data = request.get_json()
value = data["key"]
'''

'''
Flask에서 오류를 처리하기
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error</h1>", 404 # 이런 식으로 에러 코드를 보내줄 수 있다.


Flask에서 Logging 다루기
서버는 24시간 동작하므로, 문제가 있을 때 어떤 문제가 있는지 기록해두어야 한다.
사용자 모니터링, 해킹 확인 등 다양한 상용화시 문제에 대해 로깅한다.
Logging 라이브러리가 있다. 로깅 레벨이 있다. 
DEBUG > INFO > WARNING > ERROR > Critical 
심각한 문제를 일으킬 수 있는 부분에는 ERROR, Critical을 설정한다. 

import logging
logging.basicConfig(filename="test.log", level=logging.DEBUG)

logging.debug("debug") 파이썬에서 어떤 로그를 남기기 위해서 이 라이브러리를 
사용한다.
보통 로깅은 파일에 남긴다. 
에러가 발생하면 에러 로그를 우선 읽어라  
이 로그 기능을 어떻게 Flask에 적용할 수 있을까? 

logging 라이브러리와 함께 flask logging 기능 사용

logging Handler 의 종류 :
- FileHandler
- RotatingFileHandler : 하나의 최대 파일 사이즈를 지정한다. 파일이 정해진 사이즈
를 넘어가면 새로운 파일을 제공한다. 
    전체 파일을 다 쓰면, 다시 처음부터 쓴다. 이 옵션을 쓰는 게 일상적이다. 
app.run(...debug=...) -> 상용 프로그램에는 debug 값을 False로 설정한다. 
debug 값이 False이면 Production 환경이라고 콘솔 창에 뜬다. 
if not app.debug: 
    import logging
    from logging.handlers import RotatingFileHandler 
    # 이런 식으로 코드를 많이 작성한다. 디버깅 과정에서는 로그가 많이 필요하지 않기 때문
    ( 정말일까? )

에러 로그 파일은 Python을 실행한 위치에 저장이 된다. (꼭 명심할 것!)
'''

'''
다양한 데코레이터
- before_first_request : 웹 애플리케이션 기동 이후에 가장 처음에 들어오는
HTTP 요청에서만 실행 
- before_request : HTTP 요청이 들어올 때마다 실행 
    before_first_request, before_request는 인자를 전달할 수 없다. 
- after_request : HTTP 요청 처리가 끝나고 브라우저에 응답하기 전에 실행 
    response를 인자로 받아서 다시 response를 리턴해야 한다. 
Spring Framework의 AOP와 비슷하다. 
'''

'''
flask 자체만으로 백엔드, 프론트엔드를 다 서빙할 수 있다. 
지금까지는 하나의 파일에 모든 라우터를 넣었다. 
blueprint를 사용하자. blueprint = 여러 소스 파일에 flask 코드를 작성할 수 
있도록 하는 기능

from 하위 폴더 import 'python 파일'
app.register_blueprint(하위 폴더 소스파일명.블루프린트객체이름,url_prefix='/blog')
-> 블루 프린트를 등록하는 방법

from flask import Blueprint
blog_abtest = Blueprint('blog',__name__)
@blog_abtest.route('/blog1')
def blog():
    return "blue..."

main 플래스크 서버에 blueprint를 등록한다. 이렇게 MVC 패턴을 쓸 수 있다. 
'''

'''
로깅 정보는 NoSQL에 저장한다. 
SQLAlchemy, pymysql를 사용해서 DB에 접근한다.
SQLAlchemy는 객체로 데이터를 저장한다.  
'''

'''
파이썬의 객체지향
class와 상속
class Rect:
    pass
dir(SingleWord) : 객체의 클래스가 담고 있는 속성, 메서드 알아내기
클래스명은 첫글자를 대문자로 한다. 클래스명이 아닌 것은 소문자 with 언더바로 
이름을 붙인다. 
def __init__(self,...):
    xxx
indentation 유의! 파이썬 method는 항상 첫번째 파라미터로 self를 가진다. 
프로퍼티에는 self로 접근한다. 
super() 
자식 클래스에서 부모 클래스의 method를 호출할 때 사용한다. 
ex) super().work()
'''



