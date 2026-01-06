# python lecture 4일차
# 함수 개념 및 정의

# 함수지정은 def 를 사용하고 함수명은 사용의도를 명확히
# 표현 할 수 있는 이름으로 지정한다.
# 변수명 선언 규칙과 같다.
print("====================================================")
def print_1_to_10():
    i=1
    while i<=10:
        print(i)
        i+=1
        
print_1_to_10()

# 문제1 : 함수를 사용해서 코드량을 확 줄여주세요.

dan = 8

# print("== 1번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 2번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 3번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 4번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 5번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 6번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 7번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 8번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1

# print("== 9번째 구구단 8단 출력 ==")
# i = 1
# while i <= 9:
#   print("{} * {} = {}".format(dan, i, dan * i))
#   i += 1
  

# 함수를 만들어서 8단 구구단 출력 함수 코드를 작성하여
# 함수 정의 다음에 while 문을 통해서 9번 반복 시킨다.
def print_gugudan():
    dan=8
    i=1
    while i <= 9:
        print("{} * {} = {}".format(dan, i, dan * i))
        i += 1

i=1
while i <=9:
    print(f"== {i}번째 구구단 8단 출력 ==")
    print_gugudan()
    i+=1

print("====================================================")
# 매개변수 => 함수 외부에서 값을 가져온다.
# 함수 내부랑 외부를 연결해주는 매개체 그래서 매개변수
# 즉 a와 b를 연결하는 매개체
# 함수 정의 후 내용 작성 중 잠시 코드작성을 멈추고 싶을 때
#   함수 내 정의를 하지 않는다면 에러가 발생한다. 방지하기 위해 "pass" 를 입력한다.
def print_gugudan(dan):
    i=1
    while i <= 9:
        print(f"{dan} * {i} = {dan * i}")
        i += 1

print_gugudan(1)
# 위에 ( ) 안쪽에 있는 숫자들을 보고 인자 또는 인수 또는 args(아규먼트) 라고 한다.

print("====================================================")
# 문제2 : 함수를 사용해서 코드량을 확 줄여주세요.

dan = 1
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 2
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 3
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 4
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 5
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 6
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 7
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 8
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

dan = 9
print("== {}단 ==".format(dan))
i = 1
while i <= 9:
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1

print("====================================================")
def print_dan(dan):
    i=1
    while i <= 9:
        print(f"{dan} * {i} = {dan*i}")
        i += 1

dan=1
while dan <=9:
    print(f"== {dan}단 ==")
    print_dan(dan)
    dan+=1

# 매개변수는 하나만 쓸수 있지 않고 필요한 상황에 따라 더 추가할 수 있다.
#  2단인데 7 곱하기 원하는 요청이 있다면 매개변수 하나 추가하여 변수 대입을 해준다.
# ex  def function
def print_dan_limit(dan,limit):
    i=1
    while i <= limit:
        print(f"{dan} * {i} = {dan*i}")
        i += 1

dan=2
limit = 7
print(f"== {dan}단 ==")
print_dan_limit(dan,limit)




     
