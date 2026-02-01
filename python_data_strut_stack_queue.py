# 파이썬에서 스택, 큐 , 데크 => 데이터를 저장하고 관리하는 선형 자료구조
# 선형 자료구조? => 데이터가 한줄로 나열된 구조
# 데이터가 순차적으로 이어져있는 형태

# 선형 자료구조 : 배열, 연결리스트, 스택, 큐, 데크
# 비선형 자료구조 : 트리, 그래프, 힙
# 비선형 자료구조? => 데이터가 트리 형태나 네트워크 형태로 연결

# 스택(LIFO => Last in, First Out : 후입선출) : 나중에 들어온 데이터가 먼저나감.
# push() : 데이터를 스택에 추가
# pop() : 스택에서 데이터를 제거하고 ,반환
# peek() : 스택의 가장 위에 있는 데이터 조회
# is_empty() : 스택이 비어있는지 확인

# stack = []
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# 모듈 => 여러 클래스, 함수, 변수를 가지고있는 파이썬 파일
# 기본적으로 파이썬에 내장되어있는 내장모듈
# 다른사람들이 만든 외부모듈

# 패키지 => 모듈의 집합 => 대표적인 패키지 => 넘파이, 판다스
# 라이브러리 => 재사용 가능한 코드 모음집

from collections import deque
# import deque => collections 모듈에 포함된 자료구조(클래스)
# collections 모듈에서 deque 클래스를 가져온다.

# stack = deque()
# stack.append(10)
# stack.append(20)
# stack.append(30)
# print(stack.pop())
# print(stack.pop())
# print(stack.pop())

# 큐 => FIFO(Frist in , First Out : 선입선출) 먼저 들어온 데이터가 먼저 나감.
# enqueue() : 데이터를 큐의 끝에 추가
# dequeue() : 큐의 앞에서 데이터를 제거하고 반환
# peek() : 큐의 맨 앞 데아터를 조회
# is_empty() : 큐가 비어있는지 확인

# queue = []
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue.pop(0))
# print(queue.pop(0))
# print(queue.pop(0))

# queue = deque()
# queue.append(10)
# queue.append(20)
# queue.append(30)

# print(queue.popleft())
# print(queue.popleft())
# print(queue.popleft())


# 데크 => 양쪽에서 데이터를 추가하거나 제거할 수 있는 자료구조
# 스택과 큐의 기능을 모두 포함
# append(x) : 오른쪽 끝에 x 추가
# appendleft(x) : 왼쪽 끝에 x 추가
# pop() : 오른쪽 끝에서 데이터 제거
# popleft() : 왼쪽 끝에서 데이터 제거

dq = deque()
dq.append(10)
dq.append(20)

print(dq)

dq.appendleft(5)
dq.appendleft(7)
print(dq)

print(dq.popleft())
print(dq.pop())
print(dq)

# 데크활용
# 스택처럼 사용 : append(), pop()
# 큐처럼 사용 : append(), popleft()