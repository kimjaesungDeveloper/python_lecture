print("====================================================")
# 문제1 - 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.(개념 : 함수, 반복문, 리턴)
        # 소수란 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수 
def is_prime_number(num):
  if num == 1:
    return False
  #--------------------------------------
  # for i in range(2,num):  # for문 방식
  #   if num % i == 0:
  #     return False
  #   i+=1
  # return True
  #--------------------------------------
  # while문 방식
  i= 2
  while i < num:
    if num % i == 0:
      return False
    i+=1
  return True
    
print(f"1은 소수입니다 : {is_prime_number(1)}")
print(f"3은 소수입니다 : {is_prime_number(3)}")
print(f"4는 소수입니다 : {is_prime_number(4)}")
print(f"5는 소수입니다 : {is_prime_number(5)}")
print(f"6는 소수입니다 : {is_prime_number(6)}")
print(f"7는 소수입니다 : {is_prime_number(7)}")
print(f"1000은 소수입니다 : {is_prime_number(1000)}")

print("====================================================")
# 문제2 : 1부터 1000사이에 존재하는 소수들의 개수를 출력해주세요.

# 함수 안에서 함수를 호출해서 사용 예시
# def is_prim_number_sum(num):
#   i=1
#   sum =0
#   while i<=num:
#     if is_prime_number(i) == True:
#       sum+=1
#     i+=1
#   return sum

count =0
i= 1
while i<=1000:
  if is_prime_number(i):
    count +=1
  i+=1
print(f"1~ 1000 사이 소수의 총갯수 입니다 : {count}")

print("====================================================")
#문제3 : 입력받은 숫자가 10이라고 할때 1부터 10 사이에 존재하는 모든 소수를 출력하는 함수 구현
def print_1_to_n_prime_numbers(num1,num2):
  i=num1
  while i<=num2:
    if is_prime_number(i):
      print(f"{num1} ~ {num2} 사이 소수 : {i}")
    i+=1
  
print_1_to_n_prime_numbers(1,10)

print("====================================================")
# 문제4 : 1부터 n 사이의 수 중에서 소수의 개수 반환하는 함수 `get_1_to_n_prime_numbers_count` 를 구현해주세요.


#1부터 n 사이의 수 중에서 소수의 개수 반환하는 함수
def get_1_to_n_prime_numbers_count(n):
  #여기서 구현해주세요.
  count = 0
  i =1
  while i<=n:
    if is_prime_number(i):
      count+=1
    i+=1
  return count
  # i=1 
  # while i<= n:
  #   if i == 1:
  #     count = 0
  #   j=1
  #   while j <= i :  
  #     if i % j == 0:
  #       break
  #     j+=1
  #   count += 1
  #   i+=1
  # return count

number = 0

number = 1000
count = get_1_to_n_prime_numbers_count(number)
print(f"1부터 {number}사이에 존재하는 소수의 개수 : {count}개\n")
  # 출력 => 1부터 1000사이에 존재하는 소수의 개수 : 168개

number = 2000
count = get_1_to_n_prime_numbers_count(number)
print(f"1부터 {number}사이에 존재하는 소수의 개수 : {count}개\n")
  # 출력 => 1부터 2000사이에 존재하는 소수의 개수 : 303개

print("====================================================")
# 문제5 : 1부터 n 사이의 수 중에서 소수의 합을 반환하는 함수 `get_1_to_n_prime_numbers_sum` 를 구현해주세요.


# 1부터 n 사이의 수 중에서 소수의 합 반환하는 함수
def get_1_to_n_prime_numbers_sum(n):
  # 구현
  sum = 0
  i =1
  while i<=n:
    if is_prime_number(i):
      sum+=i
    i+=1
  return sum



sum = 0
number = 0

number = 1000
sum = get_1_to_n_prime_numbers_sum(number)
print(f"1부터 {number}사이에 존재하는 소수의 개수 : {sum}개\n")
  # 출력 => 1부터 1000사이에 존재하는 소수의 합 : 76127

number = 2000
sum = get_1_to_n_prime_numbers_sum(number)
print(f"1부터 {number}사이에 존재하는 소수의 개수 : {sum}개\n")
 # 출력 => 1부터 2000사이에 존재하는 소수의 합 : 277050

print("====================================================")
print("====================================================")
## 자료 형변환

# str( )  ->  인자로 들어온 값을 문자열로 변환 시켜서 반환 (정수,실수,boolean 가능)

# chr( )  ->  인자로 들어온 x를 문자로 변환시켜서 반환
#             캐릭터를 그것에 맞는 unicode(유니코드) 문자로 변환하여 반환

# bool( ) ->  인자로 들어온 x를 bool 타입으로 변환시켜서 반환
#             숫자의 경우(정수 실수 둘다)에는 0인지 0이 아닌지에 따라서 True,False가 결정 되고
#             문자의 경우에는 문자열이 비었는지(empty), 비어있지 아닌지에 따라 True, False가 결정

# int( ) ->   인자로들어온 x를 정수 타입으로 반환
#             "123" 문자열 숫자는 변환 가능 하지만 , 한글은 불가능
#             실수도 가능, boolean도 가능한데 True =1 , False = 0 으로 반환 해준다.

# 문제1 : 두개의 숫자를 연결해서 새로운 문장을 만들어주세요.
a = 10
b = 20
# c = (str(a)+str(b))
# print(c)
print(str(a)+str(b))
# 출력 => 1020

# 문제2 : 두개의 숫자문장를 더해서 새 정수를 만들어주세요.
a = '3'
b = '6'
# a = int(a)
# b = int(b)
print(int(a) + int(b))
# 출력 9

# 문제3 : 두개의 숫자문장를 더해서 새 실수를 만들어주세요.
a = '3.1'
b = '6.1'
# a = float(a)
# b = float(b)
print(float(a) + float(b))
# 출력 9.2

# 문제4 : 2개 실수문장을 정수화 하여 더해주세요.
a = '3.1'
b = '6.1'
# a = int(float(a))
# b = int(float(b))
print(int(float(a))+int(float(b)))
# 출력 9

print("====================================================")
## List 객체 정의

# 나이 10,20,30 살은 변수에 다 담지 못한다.
age = 10
age = 20
age = 30
# 이렇게 age 변수에 담아도 마지막에 대입한 30의 값만 존재한다.
# 변수에 값을 여러개 넣을수 있게 만들어진 객체가 List 다

ages = [] # 빈 리스트 객체를 하나 만들었다.
# 객체를 조종 할 수 있는 리모콘 ages라는 변수에 들어간다.

ages2 = ages # ages 변수 안에 들어있는 리모콘이 복사가 되어서 ages2 변수에 들어간다.
             # 객체는 여기서 1개다 ! 그저 ages 객체의 주소만 복사하여 가져다 쓰기에 객체는 1개!

ages.append(10)
ages.append(20)
ages.append(30)

print(ages)

# append( ) 함수는 파이썬에서 리스트의 끝에 새로운 요소를 추가하는 메서드(함수)
#      -> 추가 시 리스트의 끝(맨 마지막)에 추가가 된다.
#리스트 생성
fruits = ['apple','banana','cherry']
print(fruits)
fruits.append('orange')
print(fruits)

# 리스트 내 각 개별의 값을 가져오고 싶을때는 index로 불른다.
# 리스트 객체 안에 요소 접근 => 인덱스
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])

print("====================================================")
# 문제1 : 리스트에 순서대로 2, 1, 5, 6, 7를 한번에 담아주세요.

list = [2,1,5,6,7]
print(list)

print("====================================================")
# 문제2 : 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7를 하나씩 담아주세요.

list = []
list.append(2)
list.append(1)
list.append(5)
list.append(6)
list.append(7)
print(list)

print("====================================================")
# 문제3 : 리스트에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요.
# 그리고 '토', '일' 을 순서대로 추가해주세요.

days = ['월', '화', '수', '목', '금']

days.append('토')
days.append('일')
print(days)