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
  while i <=num:
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