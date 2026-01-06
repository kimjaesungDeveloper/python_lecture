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

print("====================================================")
# 문제3 : 매개변수의 개수를 맞춰주세요.
# 조건 : 함수호출 시 사용한 인자에 따라 함수를 적절하게 잘 만들어 주세요.
# 조건 : 오류가 나지 않으면 성공입니다.

# a () 함수 정의
def a():
    print ("a 함수 매개변수는 : 0")
# b () 함수 정의
def b(a,b,c):
    print ("b 함수 매개변수는 : 3개")
    sum = a*b*c
    print (f"매개변수의 합곱 : {sum}")

# c () 함수 정의
def c(hello,boolean,cnt1,cnt2):
    print ("c 함수 매개변수는 : 4개")
    print (f"2번 1 == 1 사용 : {boolean}")
    if (boolean) :
      print (f"안녕 인자값 출력: {hello}")
      sum= cnt1+cnt2
      print (f"args 550 + args 600 합 : {sum}")
        
a()
b(1, 2, 3)
c("안녕", 1 == 1, 550, 600)


print("====================================================")
# 문제4 : 입력받은 정수의 모든 약수를 출력하는 함수를 구현해주세요.
# 약수란 => 나눴을 때 나머지가 0인 수
''' 출력
1
2
4
5
8
10
20
25
40
50
100
125
200
250
500
1000
''' 

def print_divisors(num):
  i = 1
  cnt = 0
  # 구현
  while i<=num :
    if num%i == 0:
      print(f"{num}의 약수 출력 : {i}")
      cnt += 1
    i+=1
  print(f"총 약수의 개수 : {cnt}")

print_divisors(1000)

print("====================================================")
#함수 ==> 자판기
#매개변수 ==> 데이터 투입구
#인자 => 동전(데이터)
#리턴 => 데이터 배출구   --> return 뒤에 소스들은 진행 되지 않는다. 
#                        --> return 1회만 가능한데 조건문에서는 나누어 가능
#                        --> (조건여부에 따라 1회 실행 되기 때문에) 
  
     
# 문제5 : 5칙연산을 수행하는 함수를 만들어주세요.

# plus 함수 구현
def plus (a,b,) :
  # print(f"{a} 더하기 {b}는 {a+b} 입니다.")
  return a+b

print("3 더하기 5는 {} 입니다.".format(plus(3, 5)))
# 출력 => 3 더하기 5는 8 입니다.\
# plus(3,5)

# plus_3_nums 함수 구현
def plus_3_nums (a,b,c) :
  # print(f"{a} 더하기 {b} 더하기 {c}는 {a+b+c} 입니다.")
  return a+b+c

print("3 더하기 5 더하기 7은 {} 입니다.".format(plus_3_nums(3, 5, 7)))
# 출력 => 3 더하기 5 더하기 7은 15 입니다.
# plus_3nums(3,5,7)

# minus 함수 구현
def minus(a,b):
  # print(f"{a} 빼기 {b} 는 {a-b} 입니다.")
  return a-b

print(f"10 빼기 5 는 {minus(10,5)} 입니다.")  
# 출력 => 10 빼기 5 는 5 입니다.
# minus(10,5)

# multiply 함수 구현
def multiply(a,b):
  # print(f"{a} 곱하기 {b} 는 {a*b} 입니다.")
  return a*b
print("10 곱하기 5 는 {} 입니다.".format(multiply(10, 5)))
# 출력 => 10 곱하기 5 는 50 입니다.
multiply(10,5)

# mod 함수 구현
def mod (a,b):
  # print(f"{a}를 {b}으로 나눈 나머지는 {a%b} 입니다.")
  return a%b
  
print("4를 3으로 나눈 나머지는 {} 입니다.".format(mod(4, 3)))
# 출력 => 4를 3으로 나눈 나머지는 1 입니다
# mod(4,3)

# div 함수 구현
def div (a,b):
  # print(f"{a}를 {b}으로 나눈 몫은 {a//b} 입니다.")
  return a//b
print("4를 3으로 나눈 몫은 {} 입니다.".format(div(4, 3)))
# 출력 => 4를 3으로 나눈 몫은 1 입니다.
# div(4,3)

# div2 함수 구현
def div2(a,b):
  # print(f"{a}를 {b}으로 나눈 결과는 {a/b} 입니다.")
  return a/b
print("4를 3으로 나눈 결과는 {} 입니다.".format(div2(4, 3)))
# 출력 => 4를 3으로 나눈 결과는 1.3333333333333333 입니다.
# div2(4,3)

print("====================================================")
# 문제6 : 온도단위 섭씨를, 화씨로 바꿔주는, 함수 c_to_f 를 구현해주세요.
# 조건 : 공식 = 섭씨온도 * (9 / 5) + 32 => 화씨온도

def c_to_f(c):
  f = 0 # 구현
  f = c * (9/5) +32
  return f

print(c_to_f(10))
# 출력 => 50.0
print(c_to_f(20))
# 출력 => 68.0
print(c_to_f(30))
# 출력 => 86.0

print("====================================================")
# 문제7 : 입력받은 정수가 짝수인지 아닌지 판별해주는 함수 구현

def is_even(a):
  if a % 2 == 0:
    return True
  else :
    return False
  # return a % 2 == 0
   
print(f"10은(는) 짝수인가요? : {is_even(10)}\n")
print(f"11은(는) 짝수인가요? : {is_even(11)}\n")

print("====================================================")
# 문제8 : 입력받은 정수가 3의 배수인지 알려주는 함수 구현
def is_3_multiple (num):
  return num % 3 == 0
print(f"10은(는) 3의 배수인가요? : {is_3_multiple(10)}\n")
print(f"12은(는) 3의 배수인가요? : {is_3_multiple(12)}\n")

print("====================================================")
#문제9 : 입력받은 정수가 100보다 큰지 알려주는 함수 구현
def is_bigger_than_100(num):
  return num > 100
print(f"128은(는) 100보다 큽니다. : {is_bigger_than_100(128)}\n")
print(f"28은(는) 100보다 큽니다. : {is_bigger_than_100(28)}\n")

print("====================================================")
# 문제10 : 입력받은 정수의 모든 약수의 합을 리턴하는 함수를 구현해주세요.
def get_divisors_sum(num):
  s = 0
  i = 1

  ''' 구현 '''
  while i<=num :
    if num%i == 0:
      s += i
    i+=1
  return s

s = get_divisors_sum(1000)

print(f"정수 1000의 약수의 합 : {s}")
# 출력 => 정수 1000의 약수의 합 : 2340