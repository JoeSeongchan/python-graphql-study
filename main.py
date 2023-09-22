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
