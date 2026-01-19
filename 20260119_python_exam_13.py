## 2026-01-16 python lecture

# pygame
import pygame

# # 1.초기화
# pygame.init()
# # 2.게임화면설정
# size = [500, 600]
# screen = pygame.display.set_mode(size)  # 게임화면의 크기
# # 3.게임내에서의 설정 => 변수
# clock = pygame.time.Clock()
# black_color = (0, 0, 0)
# # 4.이벤트
# system_exit = 0
# while system_exit == 0:
#     clock.tick(5)  # fps설정 => 프레임속도
#     # 입력(키보드, 마우스)의 감지 => 활용
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             system_exit = 1
#     # 변화(입력에 따른 변화, 시간에 따른 변화)
#     # 전사작업(그리기)
#     screen.fill(black_color)
#     # 업데이트
#     pygame.display.flip()
# # 종료
# pygame.quit()
# ==================================================================
# # 1.초기화
# pygame.init()
# # 2.게임화면설정
# size = [500, 600]
# screen = pygame.display.set_mode(size)  # 게임화면의 크기
# # 3.게임내에서의 설정 => 변수
# clock = pygame.time.Clock()
# black_color = (0, 0, 0)
# r_color = (124, 45, 32)
# k = 0
# # 4.이벤트
# system_exit = 0
# while system_exit == 0:
#     clock.tick(60)  # fps설정 => 프레임속도
#     # 입력(키보드, 마우스)의 감지 => 활용
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             system_exit = 1
#     # 변화(입력에 따른 변화, 시간에 따른 변화)
#     k += 1
#     if k % 2 == 0:
#         color = black_color
#     else:
#         color = r_color
#     # 전사작업(그리기)
#     screen.fill(color)
#     # 업데이트
#     pygame.display.flip()
# # 종료
# pygame.quit()
# ==================================================================
# # 1.초기화
# pygame.init()
# # 2.게임화면설정
# size = [400, 900]
# screen = pygame.display.set_mode(size)  # 게임화면의 크기
# title = "pygame_0119"  #  게임제목
# pygame.display.set_caption(title)  # 파이게임 실행 시 상단에 나오는 게임 제목
# # 3.게임내에서의 설정 => 변수
# clock = pygame.time.Clock()
# black_color = (0, 0, 0)

# # 게임 내에서 사용할 이미지를 불러온다. 경로는 본인의 해당 이미지 파일이 있는 곳에 맞게 해야된다.
# hero = pygame.image.load(
#     "D:/KJS/PYTHON/image/airplane.jpg"
# ).convert_alpha()  # 이미지 최적화

# # 불러온 이미지의 크기를 100,100 픽셀로 조정
# hero = pygame.transform.scale(hero, (100, 100))
# hero_wid, hero_hei = hero.get_size()
# hero_x = round(size[0] / 2) - round(hero_wid / 2)
# hero_y = size[1] - hero_hei - 100
# k = 0
# # 4.이벤트
# system_exit = 0
# while system_exit == 0:
#     clock.tick(60)  # fps설정 => 프레임속도
#     # 입력(키보드, 마우스)의 감지 => 활용
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             system_exit = 1
#     # 변화(입력에 따른 변화, 시간에 따른 변화)
#     k += 1

#     # 전사작업(그리기)
#     screen.fill(black_color)
#     # 화면에 hero 이미지를 그린다 위치는 200, 300 위치에 그린다.
#     screen.blit(hero, (hero_x, hero_y))
#     # 업데이트
#     pygame.display.flip()

# # 종료
# pygame.quit()
# ==================================================================
# 1.초기화
pygame.init()
# 2.게임화면설정
size = [400, 900]
screen = pygame.display.set_mode(size)  # 게임화면의 크기
title = "pygame_0119"  #  게임제목
pygame.display.set_caption(title)  # 파이게임 실행 시 상단에 나오는 게임 제목
# 3.게임내에서의 설정 => 변수
clock = pygame.time.Clock()
black_color = (0, 0, 0)


class Img_Object:
    def __init__(self):
        self.x = 0
        self.y = 0

    def add_img(self, address):
        if address[-3:] == "png":
            self.img = pygame.image.load(address).convert_alpha()
        else:
            self.img = pygame.image.load(address)

    def change_size(self, width, height):
        self.img = pygame.transform.scale(self.img, (width, height))
        self.width, self.height = self.img.get_size()

    def show_img(self):
        screen.blit(self.img, (self.x, self.y))


hero = Img_Object()
hero.add_img("D:\KJS\PYTHON\image/airplane.jpg")
hero.change_size(80, 80)
hero.x = round(size[0] / 2) - round(hero.width / 2)
hero.y = size[1] - hero.height - 100

hero.move = 15
k = 0
left_move = False
right_move = False
up_move = False
down_move = False
# 4.이벤트
system_exit = 0
while system_exit == 0:
    clock.tick(60)  # fps설정 => 프레임속도
    # 입력(키보드, 마우스)의 감지 => 활용
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system_exit = 1

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("왼쪽 키 눌림")
                left_move = True
            if event.key == pygame.K_RIGHT:
                print("오른쪽 키 눌림")
                right_move = True
            if event.key == pygame.K_DOWN:
                print("아래쪽 키 눌림")
                down_move = True
            if event.key == pygame.K_UP:
                print("위쪽 키 눌림")
                up_move = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                print("왼쪽 키 떼짐")
                left_move = False
            if event.key == pygame.K_RIGHT:
                print("오른쪽 키 떼짐")
                right_move = False
            if event.key == pygame.K_UP:
                print("위로 키 떼짐")
                up_move = False
            if event.key == pygame.K_DOWN:
                print("아래로 키 떼짐")
                down_move = False

    if left_move == True:
        if (size[0] - size[0]) <= hero.x:
            hero.x -= hero.move
    elif right_move == True:
        if (size[0] - hero.img.width) >= hero.x:
            hero.x += hero.move
    elif up_move == True:
        if (size[1] - size[1]) <= hero.y:
            hero.y -= hero.move
    elif down_move == True:
        if (size[1] - hero.img.height) >= hero.y:
            hero.y += hero.move

    # 변화(입력에 따른 변화, 시간에 따른 변화)
    k += 1

    # 전사작업(그리기)
    screen.fill(black_color)
    hero.show_img()
    # 업데이트
    pygame.display.flip()
# 종료
pygame.quit()
