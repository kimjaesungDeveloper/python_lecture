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

print("====================================================")
# 문제1 : for문으로 1부터 100까지 출력
for i in range(100):
    print(i + 1)

print("====================================================")
# 문제2 : for문으로 100부터 1까지 출력
num = 100
for i in range(num):
    print(num - i)

print("====================================================")
# 문제3 : for문으로 1부터 100 사이의 짝수만 출력
for i in range(101):
    if i % 2 == 0:
        print(i)

print("====================================================")
# 문제4 : for문으로 100부터 1 사이의 짝수만 출력
num = 100
for i in range(num, 1, -1):
    if i % 2 == 0:
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
        i += 1
    return True


def get_1_to_n_prime_numbers_sum(num):
    # 구현
    sum = 0
    for i in range(num + 1):
        if is_prime_number(i):
            sum += 1
    return sum


print(get_1_to_n_prime_numbers_sum(100))

print("====================================================")
# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력

arr = [2, 1, 5, 6, 7]

for i in arr:
    print(i)
