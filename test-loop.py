#a = [1,2,3,4,5]
#a.pop([0])
#메인함수 - 프로그램이 실행될때 제일 먼저 실행되는 함수
#콜러 - 메인함수
#콜리 -
#메인함수가 실행이 되면
def test(): #콜리
    print("hello world 1") #주체가 테스트로 바뀜 #프린트라는 함수를 통해서 헬로우 월드를 콜한다.

test()

#인자값을 받아서 출력해 준다.
def test2(word):#word 라는 파라미터를 가지고 있는 test2라는 이름을 가진 함수를 선언한다
    word = "hello world 2" #word 라는 변수에 "hello world 2" 라는 값을 넣는다
    return word  #메인함수 한태 word 가 가지고 있는 값을 돌려준다

print(test2('word'))

#test2("hello world 2")

#test2를 실행하는 상태의 context는 메인이다

