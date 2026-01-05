# 문제 : 구구단 8단을 출력해주세요.
# 조건 : for, while문을 사용할 수 없습니다.

"""
출력 양식
== 8단 ==
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
"""

dan = 7
dan = dan + 1

# 수정가능 시작

i = 1

print("== {}단 ==".format(dan))

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i += 1

print("{} * {} = {}".format(dan, i, dan * i))
i = i + 1

# 수정가능 끝



s = 8
print("=== ver 1 ===")
for i in range(9) :
    print(f"8 * {i+1} = {s*(i+1)}")

print("=== ver 2 ===")
i = 1
while i < 10 :
    print(f"8 * {i} = {s*(i)}")
    i = i+1
     
