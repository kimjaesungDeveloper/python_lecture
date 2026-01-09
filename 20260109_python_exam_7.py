## 2026-01-09 python lecture
# while문, 0 ~ 9 까지 출력
# i = 0
# while i <= 9:
#     print(i)
#     i += 1

# for문 설명 시작
# range(끝값)
# range(시작, 끝)
# range(시작, 끝, 증가)

# for문, 0 ~ 9 까지 출력
# for i in range(10):
#     print(i)

# for문, 1 ~ 9 까지 출력
# for i in range(1, 10):
#     print(i)

# for문, 2 ~ 10 까지 출력, 2씩 증가
# for i in range(2, 11, 2):
#     print(i)

# 리스트 a셋팅
# a = [10, 20, 30, 40, 50]

# for, 리스트의 모든 요소 출력
# for v in a:
#     print(v)

# for, 리스트의 모든 요소의 번호 출력
# for v in range(len(a)):
#     print(v)

# for, 리스트의 모든 요소의 번호와 값 출력
# for i in range(len(a)):
#     print(f"a[{i}] : {a[i]}")

# ===========================================================================
# ===========================================================================
## 문자열 내장함수

# 1. .count() = 문자의 개수 세기
#               a = '아이스아메리카노'
#               a.count('아')  --> 출력 >> 2
# 2. .find() = 변수에 내가 찾고 싶은 문자 위치를 찾을 때 사용
#              값이 없을 경우 -1 출력 , 있을경우 문자의 index 번호 위치 출력
# 3. .join() = 문자열 삽입 ( list or tuple 에서도 사용)
#               각각의 문자를 쪼개서 사이에 특정값 삽입
#              *.join('안','녕','하',세요')
#              출력 >> 안*녕*하*세요
# 4. .lower()= 대문자 문자열을 소문자 문자열로 바꿔준다.
# 5. .upper()= 소문자 문자열을 대문자 문자열로 바꿔준다.
# 6. .strip()= "문자열 양쪽공백 지우기" *.strip()
#                 - .lstrip() : 왼쪽 공백
#                 - .rstrip() : 오른쪽쪽 공백
#               * strip () with chars : 원하는 문자를 입력하여 제거
#                     'www.example.com'.strip('cmowz.')
#                     'example'#

# lstrip()_ 선행문자만 지울 때 사용함

# >>> url = 'https://wikidocs.net'

# # strip() 을 사용했을 때, net 의 't'도 생략됨.
#             >>> url.strip('https://')
# rstrip()_ 후행문자만 지울 때 사용함
#             >>> url = 'https://wikidocs.net'
#            >>> url.rstrip('.net')

# lstrip() 을 사용했을 때,
#           >>> url.lstrip('https://')

# .replace() = 문자열 바꾸기
#  a = '저는 녹차를 좋아합니다.'
#  a.replace('좋아','싫어')
#  출력 >> 저는 녹차를 싫어합니다

# .split() = 문자열 나누기 > 공백을 기준으로 문자열 나누어 리스트 반환
#             특정값 기준으로 할시 ( ) 안에 값 입력하여 나누기

print("====================================================")
# 문제1 : for문으로 1부터 100까지 출력
for i in range(100):
    print(i + 1)

print("====================================================")
# 문제2 : for문으로 100부터 1까지 출력
# num = 100
# for i in range(num):
#     print(num - i)
for i in range(100, 0, -1):
    print(i)

print("====================================================")
# 문제3 : for문으로 1부터 100 사이의 짝수만 출력
# for i in range(101):
#     if i % 2 == 0:
#         print(i)
for i in range(0, 101, 2):
    print(i)

print("====================================================")
# 문제4 : for문으로 100부터 1 사이의 짝수만 출력
num = 100
# for i in range(num, 1, -1):
#     if i % 2 == 0:
#         print(i)
for i in range(100, 0, -2):
    print(i)

print("====================================================")
# 문제5 : for문으로 구구단 8단 출력
print("=== 8단 ===")
for i in range(1, 10):
    print(f"8 X {i}= {8*i}")

print("====================================================")
# 문제6 : for문으로 구구단 1단 ~ 9단 출력
print("=== 구구단 1~9단 ===")
for i in range(1, 10):
    print(f"=== {i}단 ===")
    for j in range(1, 10):
        print(f"{i} X {j} = {i*j}")

print("====================================================")


# 문제7 : for문으로 1부터 n사이에 존재하는 소수의 합을 반환하는 함수 구현
def is_prime_number(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_1_to_n_prime_numbers_sum(num):
    sum = 0
    for i in range(1, num + 1):
        if is_prime_number(i):
            sum += 1
    return sum


# def get_1_to_n_prime_numbers_sum(num):
#     sum = 0
#     for i in range(num + 1):
#         if num == 1:
#             sum += 0
#         for i in range(2, i):
#             if num % i == 0:
#                 sum += 0
#         sum += 1
#     return sum

print(get_1_to_n_prime_numbers_sum(10))
print(get_1_to_n_prime_numbers_sum(100))

print("====================================================")
# 문제8 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력
arr = [2, 1, 5, 6, 7]
for i in arr:
    print(i)

print(
    "================================================================================"
)
print(
    "================================================================================"
)
## print 출력문 문의 옵션
# sep (separation) : 구분자로서 , 문자열 사이 구분값 입력
#   - print('S','E','P', sep='@')
#     출력 >>>>> S@E@P

# end : 사용하면 그 뒤의 출력값과 이어서 출력한다.
#       (즉, 줄바꿈을 하지 않게 된다.)
#       end=' ' 사이에 무언가를 입력하게되면, sep와 비슷한 기능

#       print("I like", end=" ")
#       print("money")
#       출력 >>>>> I like money

# format : 특정 서식에 따라 문자를 출력할 수 있다.
#          부분적으로 문자열을 바꾸어 반복적으로 출력할때 유용

#           print("{0}월{1}일 입니다.".format(10,31))
#           출력 >>>>> 10월31일 입니다.

#           print("%s을 %d개 주세요."%("아이스크림", 10))
#           출력 >>>>> 아이스크림을 10개 주세요.

# Escape : 파이썬 문법을 escape(탈출)하여 출력할 수 있도록 도와주는 문자들
#           \n  : 줄바꿈

#           \t :   탭(TAP)

#           \\  :  '\' 출력

#           \'  :  작은따옴표 출력

#           \"  :  큰따옴표 출력

#           \b  :  백스페이스

## input 입력문

# print() => 출력
# input() => 입력
# print("입력 : ", end = '') # end = '' 줄바꿈 안함.
# line = input()
# print("line : ", line)

print("====================================================")
# 문제1 - 사용자에게 문장 1개를 입력받아서, 출력해주세요.
# print(input("문장을 입력해주세요:"))

print("====================================================")
# 문제2 - 사용자에게 문장 1개를 입력받아서, ,를 기준으로 나눠주세요.

# print("문장을 입력해주세요:", end="")
# line = input()
# l = line.split(",")
# print(l)

print("====================================================")
# 문제3 - 사용자에게 문장 1개를 입력받아서, strip 한 결과를,
#         다시 ,를 기준으로 나눠주세요.
# print("문장을 입력해주세요:", end="")
# line = input()
# l = line.strip().split(",")
# print(l)

print("====================================================")
# 문제4 - 사용자에게 숫자 2개를 입력받아서, 더한 결과를 출력해주세요.
# str1 = input("숫자 입력 1 : ")
# str2 = input("숫자 입력 2 : ")

# sum = int(str1) + int(str2)
# print(f"입력 숫자 더한 값 : {sum}")

# s = input().strip().split(",")
# print(s)
# s[0] = int(s[0])
# s[1] = int(s[1])
# print(s[0] + s[1])

print("====================================================")
# 문제5 - 사용자에게 숫자 3개를 입력받아서,
#        더한 결과를 출력해주세요. map, strip를 사용해주세요.

"""
map 함수 기본 문법
 
map(function, iterable)

function: 각 요소에 적용할 함수입니다.
iterable: 함수를 적용할 데이터 집합입니다.
 
map() 함수는 iterable의 각 요소에 대해 function 함수를 적용한 결과를 새로운
iterator로 반환합니다. 
이때, function 함수는 각 요소를 인자로 받아서 처리하며,
함수의 반환값이 새로운 iterator의 각 요소가 됩니다.

def square(x):
    return x**2

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))  # [1, 4, 9, 16, 25]

map 함수 동작 원리
map() 함수의 동작 원리는 다음과 같습니다.

map() 함수가 호출되면, 입력으로 전달된 function 함수와 iterable 객체들을 파라미터로 받습니다.
map() 함수는 가장 짧은 길이를 가진 iterable 객체의 길이만큼 function 함수를 반복적으로 적용합니다.
function 함수는 각 iterable 객체에서 해당하는 인덱스의 요소들을 인자로 받아 처리합니다.
function 함수의 실행 결과는 새로운 이터레이터 객체에 저장됩니다.
map() 함수가 반환하는 값은 iterator 객체입니다.
즉, map() 함수는 입력된 iterable 객체들의 각 요소를 하나씩 가져와 function 함수에 적용하고, 그 결과를 새로운 iterator 반환합니다.
map() 함수는 generator 객체를 반환하며, iterator와 비슷한 역할을 합니다.

"""

# str = map(int, input("숫자 입력 3개 (,구분) : ").split(","))

# print(list(str))
# a = int(list(str)[0])
# b = int(list(str)[1])
# c = int(list(str)[2])
# print(a + b + c)

a, b, c = map(int, input().strip().split(","))
print(f"a:{a}")
print(f"b:{b}")
print(f"c:{c}")
print(int(a) + int(b) + int(c))
