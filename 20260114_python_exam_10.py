# 회원리스트를 이용해 로그인 기능 만들기

# 코드작성은 1/13일자 파일에 추가 작성
# 1/14일자는 문제 풀이 및 수업 내용

user1 = {"아이디": "hong123", "비밀번호": "1234", "이름": "홍길동"}
user2 = {"아이디": "sony7", "비밀번호": "7777", "이름": "손흥민"}
user3 = {"아이디": "ryu99", "비밀번호": "9999", "이름": "류현진"}

user_list = [user1, user2, user3]


article1 = {
    "번호": 1,
    "제목": "소니의 축구교실",
    "내용": "소니의 축구강좌",
    "작성자": "sony7",
}
article2 = {
    "번호": 2,
    "제목": "류뚱의 야구교실",
    "내용": "류뚱의 야구강좌",
    "작성자": "ryu99",
}
article3 = {
    "번호": 3,
    "제목": "길동의 도술교술",
    "내용": "길동의 도술강좌",
    "작성자": "hong123",
}

article_list = [article1, article2, article3]

no = 4  # 게시물 번호 관리 변수

# 함수


# 게시물 번호를 받아서 해당 게시물을 반환해주는 함수
def get_article_by_article_no():
    ano = int(input("게시물 번호를 입력해주세요 : "))

    target = None

    for article in article_list:
        if article["번호"] == ano:
            target = article
            break
    return target


# 선택한 게시물을 수정하는 함수
def update_article():
    target = get_article_by_article_no()
    if target == None:
        print("없는 게시물 번호 입니다.")
    else:
        title = input("수정 할 제목 : ")
        body = input("수정 할 내용 : ")
        target["제목"] = title
        target["내용"] = body
        print(f"{target["번호"]}번 게시물이 수정이 완료되었습니다.")


# 선택한 게시물 상세보기 => 번호 제목 내용 작성자
def detail_article():
    target = get_article_by_article_no()
    if target == None:
        print("없는 게시물 번호 입니다.")
    else:
        print("===== 게시물 목록 =====")
        print("번호 : ", target["번호"])
        print("제목 : ", target["제목"])
        print("내용 : ", target["내용"])
        print("작성자 : ", target["작성자"])


# 선택한 게시물을 삭제하는 함수
def delete_article():
    target = get_article_by_article_no()
    if target == None:
        print("없는 게시물 번호 입니다.")
    else:
        article_list.remove(target)
        print(f"{target["번호"]}번 게시물이 삭제 되었습니다.")


# 게시물 목록을 출력해주는 함수
def printArticle():
    print("==========  게시물 목록  =========")

    for article in article_list:
        print(f"번호 : {article["번호"]} 제목 : {article["제목"]}")
    print("==================================")


# 게시물 추가
def addArticle():
    global no  # 전역변수 사용
    title = input("제목을 입력해주세요 : ")
    body = input("내용을 입력해주세요 : ")
    article = {"번호": no, "제목": title, "내용": body, "작성자": login_id}
    article_list.append(article)
    no += 1


# 로그인 성공여부 체크 함수
def loginCheck(id, pw):
    for user in user_list:
        if user["아이디"] == id:
            if user["비밀번호"] == pw:
                print(f"{user["이름"]}님 반갑습니다!")
                return True
            else:
                print("비밀번호를 틀렸습니다.")
                return False
    print("없는 아이디 입니다.")
    return False


# 게시판 명령어 도움말 함수
def printHelp():
    print("add : 게시물 추가")
    print("list : 게시물 목록 조회")
    print("update : 게시물 수정")
    print("delete : 게시물 삭제")
    print("detail : 게시물 상세보기")


login_id = input("아이디를 입력해 주세요 : ")
login_pw = input("비밀번호를 입력해 주세요 : ")


loginResult = loginCheck(login_id, login_pw)  # 성공 ? 실패?


# 정상적으로 로그인 시에 게시판 명령어를 입력할 수 있다.

if loginResult:
    while True:
        cmd = input("명령어를 입력해주세요 : ")
        if cmd == "exit":
            print("프로그램을 종료합니다")
            break
        elif cmd == "help":
            printHelp()
        elif cmd == "add":
            addArticle()
        elif cmd == "list":
            printArticle()
        elif cmd == "update":
            update_article()
        elif cmd == "delete":
            delete_article()
        elif cmd == "detail":
            detail_article()
