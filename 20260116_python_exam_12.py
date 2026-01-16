## 2026-01-16 python lecture

# 예외처리 try -except - else - finally

# 예외처리

# 예를 들어서 음식을 만들어주기로 했는데 재료를 안사왔다면?
# 중요한 사진촬영을 해주는 날인데 메인 카메라를 두고왔다면?
# 우리가 살다보면 위와 같이 다양한 상황을 마주하고, 예상하지 못한 상황을 마주하게 됩니다.
# 컴퓨터도 마찬가지다.
# 어떤 수를 0으로 나눈다거나.
# 문자를 숫자로 바꾸려고 한다거나.
# 값을 2개만 가지고 있는 리스트에 인덱스번호 99번에 접근하려고 하거나.

# 이런 상황을 프로그래밍에서는 에러 라고 한다.
# 이 에러를 처리하지 않는다면 프로그램의 동작이 멈춘다.
# 이런 상황에서도 프로그램이 올바르게 동작 할 수 있도록 해주는걸 예외처리라고 한다.

# try:
# 수행문장 => 에러가 발생할 가능성이 있는 문장
# except:
# 수행문장 => 에러 상황이 발생했을 때만 수행할 문장(에러가 나지 않는다면 수행x)
# else:
# 정상동작시 수행할 문장(에러가 발생하지 않았을 때만 수행)
# finally:
# 마지막으로 수행할 문장(에러 여부와 상관없이 항상 수행이 되는 문장)

# num1 = 3
# num2 = 0
# # 만약에 num2가 3이라고하면 ? 문제는x
# try:
#     result = num1 / num2
#     print(f"연산결과 : {result}")
# except:
#     print("연산결과 처리중 에러발생")
# else:
#     print("연산결과 정상적으로 처리됨")
# finally:
#     print("모든 수행을 종료함.")

# 에러처리 4가지 유형
# try - except : 에러가 발생하면 에러를 처리함.
# try - finally : 에러가 발생하면 따로 에러처리x, 마지막으로 수행할 문장을 실행하고 넘어간다.
# try => 위에 2개중에서 하나와 쌍을 이뤄야 한다.
# try - except - else : 에러가 발생하면 에러처리, 에러가 발생하지 않으면 정상동작에 따른 처리
# try - except - else - finally : 위에서 더해서 에러가 발생하거나 말거나 마지막으로 수행하고 종료.

num1 = 3
num2 = 0
try:
    result = num1 / num2
    print(f"연산결과 : {result}")
except ZeroDivisionError:  # 0으로 나눴을 때 발생하는 에러를 처리
    print("0으로 나눌 수 없습니다.")
except TypeError:  # 만약에 num2가 문자열이라면?
    print("타입이 일치하지 않습니다.")
except Exception as error:
    print("에러가 발생 했습니다. : ", error)

# Exception => 모든 에러의 기본이 되는 클래스
# 모든 에러에 대한 확인은 가능하다.
# 서로 다른상황에 대한 처리가 필요한 경우도 존재한다.


# Exception 예외종류 및 설명

"""
1. NameError : 정의 되지 않은 변수를 호출 할 떄   ( i =10 -> print( j ))
2. IndexError : 이미 정의된 리스트의 index 범위를 넘겨서 접근할 때 
3. ValueError : 변환 할수 없는 문자나 숫자를 변환하려고 할 때
4. FileNotFoundError: 존재하지 않는 파일을 호출 할때
5. ZeroDivisionError: 0으로 숫자를 나누려고 할 때
"""

## Module 모듈  설명

# 모듈 => 코드들이 작성되어 있는 하나의 파이썬 파일
# 변수, 함수, 클래스 등등.. 정의 되어 있을 수 있다.

# 대표적인 모듈 중 하나 : random
import random

menu = ["김밥", "짜장면", "떡볶이", "치킨"]
print(random.choice(menu))  # import한 random 모듈의 choice라는 함수를 사용
# 출력이 매번 달라지는 결과를 볼 수 있다.

# 하나의 파이썬 파일을 모듈
# 그런 모듈이 여러개 모인것 => 패키지
# 패키지는 하나의 폴더 => 그 안에 여러 모듈들이 존재하는 형태


## python collection 종류

# 리스트, 튜플, 세트, 딕셔너리
# 리스트 list
# 선언 : list1 = []
# 순서보장 : O
# 중복허용 : O
# 접근 : list1[idx]
# 수정 : O
# 추가 : append(), insert(), extend()
# 삭제 : remove(), pop(), clear()

# 튜플 tuple
# 선언 : t = ()
# 순서보장 : O
# 중복허용 : O
# 접근 : t[idx]
# 수정 : X
# 추가 : X
# 삭제 : X

# 세트 set
# 선언 : s = {}
# 순서보장 : X
# 중복허용 : X
# 접근 : X
# 수정 : X
# 추가 : add(), update()
# 삭제 : remove(), clear(), disacrd()

# 딕셔너리
# 선언 : dict = {key : value}
# 순서보장 : O
# 중복허용 : X(key)
# 접근 : dict[dict], dict.get(key)
# 수정 : O(value)
# 추가 : dict[key] = value, update()
# 삭제 : pop(), popitem(), clear

# 언제 써야되나?

# 여러 값들을 순서대로 관리 해야한다 ? => 리스트
# 한번 만들고나면 바뀔일이 없거나, 프로그램 실행 중에 실수라도 값이 바뀔 수 없는 그런상황을 막아야한다? 튜플
# 값의 존재여부가 중요하거나, 중복이 안된다면? => 세트
# key, value 통해서 효율적으로 데이터를 관리해야한다 => 딕셔너리

# 튜플
# 추가, 수정, 삭제 => 모두 불가능한 읽기전용
# => 수정하는 방법이 존재한다.
# tuple(), list()로 감싸면 된다.
print("튜플 => 리스트, 리스트 => 튜플")
t = ("귤", "사과")
print(t)
list1 = list(t)  # 이렇게하면 리스트 형태로 바뀐다.
list1.append("포도")  # 리스트에서 제공하는 append() 함수로 값을 추가.
print(list1)
t = tuple(list1)
print(t)

# 리스트
# 중복된 값이 허용된다. 만약에 어떤 상황에서 중복값들을 제거해야 할 때가 있다.
print("리스트 => 세트, 세트 => 리스트")
m_list = ["귤", "사과", "배", "배", "배"]  # 과일 상자 => 배는 총 3개
print(m_list)
m_set = set(m_list)  # set()로 바꿀 수가 있다.
print(m_set)
m_list = list(m_set)
print(m_list)

# 딕셔너리 : 순서보장O, 중복X(key)
print("리스트 => 딕셔너리, 딕셔너리 => 리스트")
m_list2 = ["귤", "사과", "배", "배", "배"]
print(m_list2)
m_dict = dict.fromkeys(m_list2)
print(m_dict)
m_list2 = list(m_dict)
print(m_list2)
