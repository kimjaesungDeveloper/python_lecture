## 2026-01-21 python lecture_2
# ==================================================================
import numpy as np

"""
command 창에 pip install numpy 설치 후 사용

numpy 란 - 다차원 배열을 만드는데 빠르거 효율적인 방법 제공

1. import numpy as np
    - 임포트 해서 사용가능하며  as np 별칭으로 많이들 쓴다.

2. array 만들기

      a = np.array([1, 2, 3, 4, 5])
      print(a)

      [1 2 3 4 5]

3. array의 추가 , 삭제
      x = np.array([[1, 1], [2, 2]])
      y = np.array([[5, 6]])
      np.concatenate((x, y), axis=0)

      array([[1, 1],
            [2, 2],
            [5, 6]])

4. array의 모양과 크기
      ndarray.ndim 
       - 배열의 축 수 또는 치수를 알려준다.
       
      ndarray.size 
       - 배열의 총 요소 수를 알려준다. 이 는 배열 모양의 요소의 곱이다.
       
      ndarray.shape 의 수를 나타내는 정수 튜플을 표시한다. 
       - 배열의 각 차원을 따라 저장된 요소. 예를 들어, 2개의 행과 3개의 열이 있는
         2차원 배열인 경우 배열의 모양(2, 3)이다.
         
      arr.reshape()
       - 를 이용한 array의 모양 변경

5. array의 인덱싱과 슬라이싱
      data = np.array([1, 2, 3, 4, 5])
      data[1]

      2

      data[0:2]
      array([1, 2])
6. 데이터의 생성

      (1) ones()
      np.ones((3, 5))

      array([[1., 1., 1., 1., 1.],
            [1., 1., 1., 1., 1.],
            [1., 1., 1., 1., 1.]])
      (2) zeros()
      np.zeros((3, 5))

      array([[0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0.]])
      (3) random()
      np.random.random((3, 2)) 

      array([[0.31035939, 0.0573622 ],
            [0.61758234, 0.5474854 ],
            [0.89271177, 0.86629414]])

"""
# ndArray ? N-dismensional Array의 약자, 다차원 배열
# ndArray 생성
# numpy.array([1,2,3,4])
# np.array([1,2,3,4])

# arr = [1,2,3,4] # 파이썬 리스트
arr1 = np.array([1, 2, 3, 4])  # 넘파이 ndArray

# print(type(arr))
# print(type(arr1))

# print(arr)
# print(arr1)

# 2차원 ndArray 생성
arr2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# 3차원 ndArray 생성
arr3 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[1, 2, 3, 4], [5, 6, 7, 8]]])

# print(arr1)
# print("================")
# print(arr2)
# print("================")
# print(arr3)

# ndArray.ndim => 배열의 차원을 알 수 있다
# print("== ndArray.ndim ==")
# print(arr1.ndim)
# print(arr2.ndim)
# print(arr3.ndim)

# ndArray.shape => 모양
# print("== ndArray.shape ==")
# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)

# ndArray.size => 크기
# print("== ndArray.size ==")
# print(arr1.size)
# print(arr2.size)
# print(arr3.size)

# ndArray.dtype => 타입
# print("== ndArray.dtype ==")
# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)

""" arr1
[1 2 3 4]
================
arr2
[[1 2 3 4]
 [5 6 7 8]]
================
arr3
[[[1 2 3 4]
  [5 6 7 8]]

 [[1 2 3 4]
  [5 6 7 8]]] """

# 배열 생성 함수
# 0으로 채워진 행렬
# np.zeros((3,4))
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.],
#        [0., 0., 0., 0.]])
# 1로 채워진 행렬
# np.ones((2,3,4))
# array([[[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]],

#        [[1., 1., 1., 1.],
#         [1., 1., 1., 1.],
#         [1., 1., 1., 1.]]])
# # i로 채워진 행렬
# np.full((2,2), 5)
# array([[5, 5],
#        [5, 5]])

# like => 다른 배열의 모양을 본따서
# print(np.zeros_like(arr1))
# print("=======================")
# print(np.ones_like(arr2))
# print("=======================")
# print(np.full_like(arr3, 5))

# random => 난수
# np.random.seed(1) # 최초 난수생성 기준
# random_arr = np.random.randint(-100, 100, (2,3))
# # -100 ~ 100 사이에 있는 정수로 2 * 3 행렬 생성

# print(random_arr)
