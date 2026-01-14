## 2026-01-13 python lecture

# 데이터 여러개를 저장할 때
# 리스트
# 딕셔너리

# Dictionary 함수
"""
.keys()
.values()
.items()
.get()
.clear()
in
empty()
claer()  = 딕셔너리 전체 비우기


"""


# 리스트의 장점?
# 데이터를 넣을 때 편하다.
# 데이터를 넣으면 키가 자동으로 정해진다.

# 영희, 영수, 철수
# ages = [10, 20, 30]
# print(ages[0])  # 영희
# print(ages[1])  # 영수
# print(ages[2])  # 철수

ages1 = {"영희": 10, "영수": 20, "철수": 30}
# print(ages1["영희"])
# # 민희 나이추가
# ages1["민희"] = 40

# print(ages1)

# 딕셔너리 장점
# 데이터를 가져올 때 편하다.
# 단점 => 딕셔너리에 데이터를 넣을 때는 키값을 내가 직접 넣어줘야된다.
# ages1["영수"] = 50 => 위 딕셔너리에 키 값이 존재하면 추가가 아니고, 수정

# 반복출력
print("== 딕셔너리 반복1 ==")  # 키 값만 나온다.
for name in ages1:  # 기본적으로 딕셔너리를 순회하면 key값만 얻을 수 있다.
    print(name)

# == key값 순회 다른 방법 ==
for name in ages1.keys():
    print(name)
# keys() 를 사용하여 반복 없이 key값만 가져오고 싶을때 사용한다.
# type : dict.keys 로 출력 됨  --> list로 바꾸고 싶다면 list() 괄호안에 넣어 변환
print(f"키값만 바로 보고싶을 떄 keys() 함수 사용 : {ages1.keys()}")

print("== 딕셔너리 반복2 ==")
# for문을 사용해서 딕셔너리에 key를 순회한다. name 딕셔너리의 key => 영희, 영수, 철수
# for문 안쪽 age 변수 => ages1 딕셔너리에 해당하는 이름에 벨류가 할당이 된다.
for name in ages1:
    age = ages1[name]
    print(f"{name} : {age}")

print("== 딕셔너리 반복3 ==")  # 누구의 나이인지 모른다.
for age in ages1.values():  # values() 해당 딕셔너리의 벨류값만 얻고 for을 순회한다.
    print(f"{age}")

print("== 딕셔너리 반복4 ==")  # 가장 깔끔한 방법
for name, age in ages1.items():  # items() 사용하면 키와 벨류값을 동시에 얻는다.
    # name => 키값, age => 벨류값
    print(f"이름은 {name} 이고, 나이는 {age}살")

# 삭제
del ages1["철수"]

print("== 딕셔너리 반복4 ==")
for name, age in ages1.items():
    print(f"이름은 {name} 이고, 나이는 {age}살")

print("==============================================================================")

# 딕셔너리를 이용해서 회원 정보를 저장해주세요. 회원 정보는 아이디, 비밀번호, 이름으로 하겠습니다.
# 아이디가 hong123, 비밀번호가 1234, 이름이 홍길동인 회원
# 아이디가 sony7, 비밀번호가 7777, 이름이 손흥민인 회원
# 아이디가 ryu99, 비밀번호가 9999, 이름이 류현진인 회원
# 위 세명의 회원을 딕셔너리를 이용해 만들고 출력해주세요. 회원의 정보를 모두 출력해주세요.

"""

아이디 : hong123
비밀번호 : 1234
이름 : 홍길동
================
아이디 : sony7
비밀번호 : 7777
이름 : 손흥민
================
아이디 : ryu99
비밀번호 : 9999
이름 : 류현진
================

"""
# 모든 회원 정보 출력

list = [
    {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"},
    {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"},
    {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"},
]
print("=== 모든회원 정보 출력 ===")

for i in list:
    print(f"아이디 : {i["아이디"]}")
    print(f"비밀번호 : {i["비밀번호"]}")
    print(f"이름 : {i["이름"]}")
    print("================")

# # 모든 회원 아이디를 출력

print("=== 모든회원 아이디 출력 ===")
for i in list:
    print(f"아이디 : {i["아이디"]}")

# hong123 아이디를 가진 회원의 이름 출력
print("=== 아이디를 가진 회원의 이름 출력 ===")
for i in list:
    if i["아이디"] != "":
        print(f"이름 : {i["이름"]}")
# hong123 아이디를 가진 회원의 비밀번호를 3333으로 수정 후 모든 회원 정보 출력
for i in list:
    if i["아이디"] == "hong123":
        i["비밀번호"] = "3333"


for i in list:
    print(f"아이디 : {i["아이디"]}")
    print(f"비밀번호 : {i["비밀번호"]}")
    print(f"이름 : {i["이름"]}")
# 아이디가 hong124, 이름 홍길순, 비밀번호 h1234 인 회원추가
list.append({"아이디": "hong124", "이름": "홍길순", "비밀번호": "h1234"})

for i in list:
    print(f"아이디 : {i["아이디"]}")
    print(f"비밀번호 : {i["비밀번호"]}")
    print(f"이름 : {i["이름"]}")

# 아이디가 중복될 시 추가 거부.

# while True:
#     id = input("기존 아이디 입력 : ")
#     id2 = input("변경 할 아이디 입력 : ")
#     for i in list:
#         if i["아이디"] == id2:
#             print("중복 아이디입니다. 다시 입력해주세요 ")
#             continue
#         elif id2 == id:
#             print("기존 아이디와 중복. 다시 입력해주세요 ")
#             continue
#         else:
#             if i["아이디"] == id:
#                 i["아이디"] = id2
#                 print("중복 되지 않는 아이디입니다 ! , 등록완료")
#                 break


print("==============================================================================")
# 문제풀이

user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}

user_list = [user1, user2, user3]


# 모든 회원 정보 출력
def print_all_users():
    for user in user_list:
        for key, value in user.items():
            print(f"{key} : {value}")
        print("================")


# print_all_users()
# # 모든 회원 아이디를 출력
# for user in user_list:
#     print(user["아이디"])

# hong123 아이디를 가진 회원의 이름 출력
# for user in user_list:
#     if user["아이디"] == "hong123":
#         print(user["이름"])

# hong123 아이디를 가진 회원의 비밀번호를 3333으로 수정 후 모든 회원 정보 출력
# for user in user_list:
#     if user["아이디"] == "hong123":
#         user["비밀번호"] = "3333"
# print_all_users()

# 아이디가 hong124, 이름 홍길순, 비밀번호 h1234 인 회원추가
user5 = {"아이디": "hong124", "비밀번호": "h1234", "이름": "홍길순"}
user_list.append(user5)
# print_all_users()

# 아이디가 중복될 시 추가 거부.
# user5 = {}
# user5["아이디"] = "hong123"
# user5["비밀번호"] = "h1234"
# user5["이름"] = "홍길"

# flag = True
# for user in user_list:
#     if user["아이디"] == user5["아이디"]:
#         flag = False
#         print("이미 존재하는 아이디 입니다.")
#         break
# if flag:
#     user_list.append(user5)

# print_all_users()

print("==============================================================================")

# 회원리스트를 이용해 로그인 기능 만들기

user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}

user_list = [user1, user2, user3]

login_id = input("아이디를 입력해주세요 : ")
login_pw = input("비밀번호를 입력해주세요 : ")

# 아이디와 비밀번호를 모두 올바르게 입력하면 이름으로
# 1. '???님 반갑습니다!' 출력

# 입출력 예시
# 아이디를 입력해주세요 : hong123
# 비밀번호를 입력해주세요 : 1234
# 홍길동님 반갑습니다!

# 2. 아이디를 틀리면 '없는 아이디입니다'라고 출력
# 입출력 예시
# 아이디를 입력해주세요 : aaaa
# 비밀번호를 입력해주세요 : 1234
# 없는 아이디입니다


# 3. 아이디는 맞지만 비밀번호가 틀리면 '비밀번호를 틀렸습니다'라고 출력
# 입출력 예시
# 아이디를 입력해주세요 : hong123
# 비밀번호를 입력해주세요 : qwer
# 비밀번호를 틀렸습니다


# 게시판 명령어 입력 : help

# add : 게시물 추가
# list : 게시물 목록 조회

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실    작성자 : sony7
# 번호 : 2    제목 : 류뚱의 야구교실    작성자 : ryu99
# 번호 : 3    제목 : 길동의 도술교술    작성자 : hong123
# =================================

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : aaa
# 내용을 입력해주세요 : aaa

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : bbb
# 내용을 입력해주세요 : bbb

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : ccc
# 내용을 입력해주세요 : ccc

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실
# 번호 : 2    제목 : 류뚱의 야구교실
# 번호 : 3    제목 : 길동의 도술교술
# 번호 : 4    제목 : aaa
# 번호 : 5    제목 : bbb
# 번호 : 6    제목 : ccc
# =================================

board_list = []
flag = 0


def add_board():
    title = input("제목을 입력 해주세요 : ")
    content = input("내용을 입력 해주세요 : ")
    board_list.append(
        {
            "번호": len(board_list) + 1,
            "제목": title,
            "내용": content,
            "작성자": login_id,
        }
    )
    print("게시물이 등록 되었습니다.")


def list_board():
    if len(board_list) == 0:
        print("게시물이 없습니다.")
    else:
        print("게시물 출력.")
        print("==========  게시물 목록  =========")
        for i, board in enumerate(board_list):
            ty = board
            print(board.items())
            # print(f"번호 : {i+1}\t", end="")
            # print(f"제목 : {board["제목"]} \n내용 : {board["내용"]}")
            print(
                f"번호 : {board["번호"]} 제목 : {board["제목"]} 작성자 : {board["작성자"]}"
            )
        print("=================================")


for user in user_list:
    if user["아이디"] == login_id:
        flag = 1
        if user["비밀번호"] == login_pw:
            print(f"{user["이름"]}님! 안녕하세요")

            # 게시판 시작
            while True:
                comm = input("게시판 명령어 입력 : ")

                if comm == "help":
                    print("add : 게시물 추가")
                    print("list : 게시물 목록 조회")
                    print("update : 게시물 수정")
                    print("remove : 게시물 삭제")
                    print("exit : 게시물 프로그램 종료")
                elif comm == "add":
                    add_board()
                elif comm == "list":
                    list_board()
                elif comm == "exit":
                    print("게시물 프로그램 종료")
                    break
        else:
            print("비밀번호를 틀렸습니다.")
if flag == 0:
    print("없는 아이디입니다.")
