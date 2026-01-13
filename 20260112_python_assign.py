# 프로그램 만들기
# KOREA_IT_ACADEMY_ 12month vacation Class
# 작성자 : 김재성

list = []


def help():
    print("add : 데이터 추가")
    print("list : 데이터 조회")
    print("update : 데이터 수정")
    print("delete : 데이터 삭제")
    print("exit : 프로그램 종료")


def add():
    addNum = int(input("저장할 값을 입력 해주세요 : 10 (입력)"))
    list.append(addNum)
    print(f"{addNum}을 저장했습니다.")


def listCheck():
    print(list)


def update():
    res1 = int(input("몇번째 값을 수정하시겠습니까 : 1"))
    res2 = int(input("어떤 값으로 수정하시겠습니까 : 100"))
    # list.insert(int(res1) - 1, int(res2))
    list[res1 - 1] = res2
    print(f"{res1}번째 값이 {res2}으로 수정되었습니다.")


def delete():
    del1 = int(input("몇번째 값을 삭제 하시겠습니까 : 1"))
    del list[del1 - 1]
    print(f"{del1}번쨰 값을 삭제했습니다.")


def exit():
    print("프로그램을 종료합니다.")


while True:
    command = input("명령어를 입력 해주세요. :")
    if command not in ["help", "add", "list", "update", "delete", "exit"]:
        print("잘못 입력 하셨습니다. 명령어를 다시 입력 해주세요 : ")
        command = input("명령어를 입력 해주세요. help (입력) :")
    if command == "help":
        help()
    elif command == "add":
        add()
    elif command == "list":
        listCheck()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "exit":
        exit()
        break
