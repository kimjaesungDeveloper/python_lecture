print("====================================================")
# 문제1 - 입력받은 정수가 소수인지 아닌지 알려주는 함수를 구현해주세요.(개념 : 함수, 반복문, 리턴)
        # 소수란 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수 
def is_prime_number(num):
  if num == 1:
    return False
  for i in range(2,num):
    if num % i == 0:
      return False
  return True
    
  

print(f"1은 소수입니다 : {is_prime_number(1)}")
print(f"3은 소수입니다 : {is_prime_number(3)}")
print(f"4는 소수입니다 : {is_prime_number(4)}")
print(f"5는 소수입니다 : {is_prime_number(5)}")
print(f"6는 소수입니다 : {is_prime_number(6)}")
print(f"7는 소수입니다 : {is_prime_number(7)}")
print(f"1000은 소수입니다 : {is_prime_number(1000)}")