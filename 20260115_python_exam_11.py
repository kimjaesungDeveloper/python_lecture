## 2026-01-13 python lecture

# class - 속성 설명 및 정의
# 파이썬 => 객체지향 프로그래밍 언어(OOP)
# OOP의 특징 정리
# 클래스(설계도) => 객체를 표현하기 위한 문법, 프로그래밍에서 객체를 만들 때 사용
# 전사, 궁수, 자동차, 비행기, 사람, 강아지, 고양이 => Object 현실, 가상 개념
# 속성(특징) => attribute
# 전사 클래스
# 체력, 마나, 공격력, 방어력 => 속성
# 공격하다, 방어하다 => 기능

# 객체가 객체를 지칭할 때 => 객체
# 객체가 클래스와 연관지어서 대상을 지칭할 때 => 인스턴스(instance)

# 파이썬 => 객체(object)는 데이터와 데이터를 처리하는 메서드(함수)를 함께 묵어놓은 것을 말한다.
# 객체 => 데이터를 추상화하고, 캡슐화 해서 프로그램을 조직화 하고, 모듈화 하는데 사용 된다.

# 자동차 객체
# 속성 => 색상, 속도, 모델 등을 가질 수 있다.
# 메서드(함수) => 가속, 감속, 방향전환 등의 행동을 수행할 수 있다.
# 파이썬 => 거의 모든 것이 객체로 표현이 된다.
# 숫자, 문자열, 리스트, 함수 등 모두 객체로 취급이 된다.
# 객체들은 각각의 특정과 기능을 가지고 있고, 필요에 따라서 새로운 클래스를 정의해서 객체를 만들 수 있다.


# class Person:
#     # 일반적으로 함수 정의 시 첫 번째 매개변수로 self 사용해서 현재 인스턴스를 나타낸다.
#     # 함수 내에서는 self 통해서 해당 인스턴스의 속성에 접근 할 수 있다.
#     def hello(self):
#         print("안녕하세요")


# Jin = Person()  # Person의 인스턴스를 생성해서 변수 Jin에 할당하겠다.
# # 즉 객체를 만들었다라는 의미.
# Jin.hello()
# print(type(Jin))


# a = int(10)
# print(a)

# b = list(range(10))
# b.append(40)
# print(b)

# c = dict(x = 10, y = 20)
# print(c)

# print(type(a))
# print(type(b))
# print(type(c))

# a = list(range(10))
# b = list(range(20))
# a, b => 객체, list 클래스의 인스턴스

# 파이썬에서 클래스를 정의하는 간단한 예제
# class 라는 키워드를 사용해서 Person이라는 클래스를 정의
# class Person:
#     pass # 클래스 내부에서 pass는 아무런 동작을 하지 않고, 그냥 넘어가는 것을 말한다.

# 하나의 기능에서 다른 기능을 실행하고 싶을 때 self
# class Person:
#     def Hello(self):
#         print("Hello")

#     def Hi(self): # Hi 함수는 self.Hello()를 호출하는 함수
#         self.Hello()

# Jin1 = Person()
# Jin1.Hello()
# Jin1.Hi()

# 속성 => 객체가 가지는 데이터 상태를 나타낸다. 객체의 특징이나 상태를 표현하기 위해서 사용됨
# 자동차 객체 => 색상, 속도, 모델 등은 해당 자동차의 속성
# 사람 객체 => 이름, 나이, 성별 등은 해당 사람의 속성
# 클래스 내부에서 self.attribute_name 형식으로 자신만의 속성을 가질수가 있다.
# 속성 => 해당 클래스의 모든 인스턴스에서 공유된다.
# 객체를 생성할 때마다 각각의 객체는 자신만의 속성을 가질 수가 있다.
# self => 클래스의 인스턴스 객체를 가리킨다.
# 클래스의 내부의 함수(메서드)에서 self를 통해서 인스턴스의 속성에 접근하거나 다른 메서드를 호출 할 수 있다.

# 속성
# class Person():
#     def __init__(self): # __init__ 함수는 클래스의 생성자 => 객체가 생성될 때 자동으로 호출이 된다.
#         print("__init__(생성자) 실행")
#         self.hello = "안녕하세요" # "안녕하세요"라는 문자열을 갖는 hello라는 속성을 객체에 추가한다.

#     def Hi(self):
#         print(self.hello)

# Jin = Person()
# Jin.Hi()


# class Person:
#     def __init__(self, name, age):
#         self.hello = "안녕하세요"
#         self.name = name
#         self.age = age
#         self.성별 = "남"

#     def introduce(self):
#         print(
#             f"{self.hello} 저는 {self.age}살 이고, 성별은 {self.성별}, 이름은 {self.name}입니다."
#         )


# Jin = Person("진", 22)
# Jin.introduce()

# print(f"이름 : {Jin.name}")
# print(f"나이 : {Jin.age}")
# print(f"성별 : {Jin.성별}")

# Paul = Person("폴", 32)
# Paul.introduce()

# 비공개 속성(private attribute)
#    비공개 속성으로 할 경우 클래스 외부에서는 접근 불가능


# class Person:  # 비공개 속성 => 클래스 외부에서 접근이 불가, 클래스 내부에서만 사용가능 => private attribute
#     def __init__(self, name, age, weight):
#         self.hello = "안녕하세요"
#         self.name = name
#         self.age = age
#         # self.weight = weight
#         self.__weight = weight  # 변수 앞에 `__`를 붙혀서 비공개 속성으로 변경


# Jin = Person("진", 22, 72)
# print(Jin.name)
# print(Jin.age)
# print(Jin.weight)


# 문제 1
class Warrior:
    def __init__(self, hp, mp, attack_point):
        self.hp = hp
        self.mp = mp
        self.attack_point = attack_point

    def attack(self):
        print("공격!")


x = Warrior(1000, 500, 30)

print(x.hp, x.mp, x.attack_point)

x.attack()
# 출력 : 공격!


## 인스턴스, 스태틱(정적), 클래스 메서드

print("== 인스턴스 메서드 ==")


# 인스턴스 메서드
#   그냥 정의 => 첫 번째 인자에 self => 호출은 인스턴스를 통해서 호출
class Person:
    def hi(self):
        print("hi")


Jin = Person()
Jin.hi()

print("== 스태틱(정적) 메서드 ==")


# 정적 메서드 => 첫 번째 매개변수로 self는 필요없다.
#   주로 class 내부에서 self 사용없이 쓸 때
#   @staticmethod => 첫 번째 인자x => 클래스 또는 인스턴스를 통해서 호출


class Calc:
    @staticmethod  # 스태틱(정적) 메서드
    def add(a, b):
        print(a + b)


Calc.add(10, 20)  # 클래스에서 바로 메서드(함수) 호출(실행)이 가능하다.

print("== 클래스 메서드 ==")


# 클래스 메서드
#   주로 class 내부에서 self 인자 사용없이 따로 사용할 때
#   @classmethod => 첫 번째 인자에 cls => 호출은 클래스 또는 인스턴스를 통해서 호출
class Person2:
    count = 0  # 클래스 속성

    def __init__(self):
        Person2.count += 1

    @classmethod
    def print_count(cls):  # 클래스메서드
        print(f"사람이 총 {cls.count}명 있습니다.")  # cls로 클래스 속성에 접근한다.


Person2.print_count()
Jin2 = Person2()

Person2.print_count()
Jin2 = Person2()

Person2.print_count()


## 클래스 상속 (부모,자식 간 오버로딩 및 super() 설명)
# 상속 => 물려받다, 물려받은 기능을 유치한채 다른 기능을 추가
# 물려주는 클래스 => 부모클래스
# 물려받는 클래스 => 자식클래스


# 부모클래스
class Person:
    def hi(self):
        print("하이")

    def hello(self):
        print("헬로")


# 자식클래스 => 자식클래스의 메서드(함수) 갯수는 부모클래스보다 같거나 많다.
class Student(Person):
    def study(self):
        print("공부")

    def hello(self):  # 메서드 오버라이딩
        print("안녕~~")

    def hello2(self):
        super().hello()

    # hello2 함수에 super().hello() 호출하게 되면 부모클래스의 hello 메서드가 호출이 된다.
    # Student 클래스 => 만들어진 객체는 2개의 hello 메서드를 현재 가지고 있는 상태.


# 자식 클래스가 부모 클래스의 메서드를 가져다 쓸수 있다
Jin = Student()
Jin.hi()
Jin.hello()
Jin.study()
Jin.hello2()

# 부모 클래스는 자식의 클래스 내 메서드를 사용 할수 없다. (상속 받은게 없기에)
print("=======")
Paul = Person()
Paul.hi()
Paul.hello()
Paul.study()

# ==========================================================================
# 개별 class 이론 추가 내용

# @classmethod 사용 (클래스 자체 호출, 클래스 변수 접근)
# @classmethod 데코레이터를 사용하고 첫 번째 인자를 cls (관례)로 받으면,
# 바인딩되어 인스턴스 없이도 호출 가능
# class MyClass:
#     @classmethod
#     def my_class_method(cls, arg):
#         print(f"클래스 메서드 호출됨. cls: {cls}, 인자: {arg}")


# # 호출 방법: 클래스명.메서드명()
# MyClass.my_class_method("Hello")


# 클래스 이름으로 직접 호출 (self가 없는 메서드)
# 메서드 정의 시 self를 인자로 받지 않도록 만들고 클래스 이름으로 직접 호출하면
# self 없이 사용 가능하지만, 이는 일반적인 인스턴스 메서드 호출 방식이 아닙니다.
# class Car:
#     @staticmethod
#     def color(blue):
#         print("color : blue")


# sonata = Car()
# sonata.color("블루")
