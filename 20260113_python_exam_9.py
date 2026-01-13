## 2026-01-13 python lecture

# 데이터 여러개를 저장할 때
# 리스트
# 딕셔너리

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
