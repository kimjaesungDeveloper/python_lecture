# ## 2026-01-20 python lecture
# # ==================================================================
# import pygame, random

# # 1.초기화
# pygame.init()
# # 2.게임화면설정
# size = [400, 900]
# screen = pygame.display.set_mode(size)  # 게임화면의 크기
# title = "pygame_0120_KJS"  #  게임제목
# pygame.display.set_caption(title)  # 파이게임 실행 시 상단에 나오는 게임 제목
# # 3.게임내에서의 설정 => 변수
# clock = pygame.time.Clock()
# black_color = (0, 0, 0)


# class Img_Object:
#     def __init__(self):
#         self.x = 0
#         self.y = 0

#     def add_img(self, address):
#         if address[-3:] == "png":
#             self.img = pygame.image.load(address).convert_alpha()
#         else:
#             self.img = pygame.image.load(address)

#     def change_size(self, width, height):
#         self.img = pygame.transform.scale(self.img, (width, height))
#         self.width, self.height = self.img.get_size()

#     def show_img(self):
#         screen.blit(self.img, (self.x, self.y))


# hero = Img_Object()
# hero.add_img("D:\KJS\PYTHON\image/airplane.jpg")
# hero.change_size(80, 80)
# hero.x = round(size[0] / 2) - round(hero.width / 2)
# hero.y = size[1] - hero.height - 100

# k = 0

# #  비행기 변수
# hero.move = 15
# left_move = False
# right_move = False
# up_move = False
# down_move = False

# # 미사일 변수
# misl_insert = False
# missile_list = []
# missile_speed = 3

# # 적기 변수
# germ_list = []

# # def missile_moving():
# #     if misl_insert:
# #         missile.show_img()
# #         missile_list.append(missile)
# #         if (size[1] - size[1]) < missile.y:
# #             missile.y -= missile_speed


# # 4.이벤트
# system_exit = 0
# while system_exit == 0:
#     clock.tick(60)  # fps설정 => 프레임속도
#     # 입력(키보드, 마우스)의 감지 => 활용
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             system_exit = 1

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 print("왼쪽 키 눌림")
#                 left_move = True
#             if event.key == pygame.K_RIGHT:
#                 print("오른쪽 키 눌림")
#                 right_move = True
#             if event.key == pygame.K_DOWN:
#                 print("아래쪽 키 눌림")
#                 down_move = True
#             if event.key == pygame.K_UP:
#                 print("위쪽 키 눌림")
#                 up_move = True
#             if event.key == pygame.K_SPACE:
#                 print("스페이스바 눌림")
#                 misl_insert = True

#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:
#                 print("왼쪽 키 떼짐")
#                 left_move = False
#             if event.key == pygame.K_RIGHT:
#                 print("오른쪽 키 떼짐")
#                 right_move = False
#             if event.key == pygame.K_UP:
#                 print("위로 키 떼짐")
#                 up_move = False
#             if event.key == pygame.K_DOWN:
#                 print("아래로 키 떼짐")
#                 down_move = False
#             if event.key == pygame.K_SPACE:
#                 print("스페이스바 키 떼짐")
#                 misl_insert = False

#     if left_move == True:
#         if (size[0] - size[0]) <= hero.x:
#             hero.x -= hero.move
#     elif right_move == True:
#         if (size[0] - hero.img.width) >= hero.x:
#             hero.x += hero.move
#     elif up_move == True:
#         if (size[1] - size[1]) <= hero.y:
#             hero.y -= hero.move
#     elif down_move == True:
#         if (size[1] - hero.img.height) >= hero.y:
#             hero.y += hero.move

#     if misl_insert == True and k % 6 == 0:
#         missile = Img_Object()
#         missile.add_img("D:\KJS\PYTHON\image/missile.jpg")
#         missile.change_size(35, 50)
#         missile.x = hero.x + hero.width / 2 - missile.width / 2
#         missile.y = hero.y - missile.height - 10
#         missile.move = 5
#         missile_list.append(missile)

#     # 변화(입력에 따른 변화, 시간에 따른 변화)
#     k += 1

#     # 전사작업(그리기)
#     screen.fill(black_color)
#     hero.show_img()
#     # missile_moving()
#     for m in missile_list:
#         m.y -= m.move
#         m.show_img()
#         if m.y == 0:
#             missile_list.remove(m)
#     print(len(missile_list))

#     # 적기 생성
#     if random.random() >= 0.98:
#         germ = Img_Object()
#         germ.add_img("D:\KJS\PYTHON\image/germ.jpg")
#         germ.change_size(40, 40)
#         germ.x = random.randrange(0, size[0])
#         germ.y = 100
#         germ.move = 5
#         germ_list.append(germ)
#         germ.show_img()

#     for g in germ_list:
#         g.y += g.move
#         g.show_img()
#         if g.y == 0:
#             germ_list.remove(m)

#     # 업데이트
#     pygame.display.flip()
# # 종료
# pygame.quit()


# =================================================================================
# =================================================================================
# pygame 풀이

import pygame, random

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
hero.move = 10
k = 0
left_move = False
right_move = False
space_on = False
missile_list = []  # 미사일 객체를 저장할 리스트
enemy_list = []
# 4.이벤트
system_exit = 0
while system_exit == 0:
    clock.tick(60)  # fps설정 => 프레임속도
    # 입력(키보드, 마우스)의 감지 => 활용
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system_exit = 1
        if event.type == pygame.KEYDOWN:  # 키가 눌렸을 때
            if event.key == pygame.K_LEFT:  # 방향키 왼쪽
                left_move = True
            if event.key == pygame.K_RIGHT:  # 방향키 오른쪽
                right_move = True
            if event.key == pygame.K_SPACE:
                space_on = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:  # 방향키 왼쪽
                left_move = False
            if event.key == pygame.K_RIGHT:  # 방향키 오른쪽
                right_move = False
            if event.key == pygame.K_SPACE:
                space_on = False
    # 변화(입력에 따른 변화, 시간에 따른 변화)
    if left_move == True:
        hero.x -= hero.move
        if hero.x <= 0:
            hero.x = 0
    elif right_move == True:
        hero.x += hero.move
        if hero.x >= size[0] - hero.width:
            hero.x = size[0] - hero.width

    if space_on == True and k % 6 == 0:
        missile = Img_Object()  # 미사일 객체 생성 => 위 if문에 조건이 True일 때
        missile.add_img("D:/KJS/PYTHON/image/missile.jpg")
        missile.change_size(45, 50)

        # 미사일 위치 설정
        missile.x = hero.x + hero.width / 2 - missile.width / 2
        missile.y = hero.y - missile.height - 10
        missile.move = 7  # 미사일 속도
        missile_list.append(missile)  # 위에서 미리 만들어준 미사일 리스트에 append
    k += 1

    delete_missile_list = []
    for m in missile_list:
        m.y -= m.move
        if m.y <= m.height:
            delete_missile_list.append(m)
    for m in delete_missile_list:
        if m in missile_list:
            missile_list.remove(m)
            print("미사일 제거")

    if random.random() >= 0.98:
        enemy = Img_Object()
        enemy.add_img("D:\KJS\PYTHON\image\germ.jpg")
        enemy.change_size(35, 35)
        enemy.x = random.randrange(
            0 + round(hero.width / 2), size[0] - enemy.width - round(hero.width / 2)
        )
        enemy.y = 15
        enemy.move = 5
        enemy_list.append(enemy)

    delete_enemy_list = []

    for e in enemy_list:
        e.y += e.move
        if e.y > size[1]:
            delete_enemy_list.append(e)

    for e in delete_enemy_list:
        if e in enemy_list:
            enemy_list.remove(e)
            print("enemy 제거")

    # 전사작업(그리기)
    screen.fill(black_color)
    hero.show_img()
    for m in missile_list:
        m.show_img()  # 미사일을 게임 화면에 표시
    for e in enemy_list:
        e.show_img()
    # 업데이트
    pygame.display.flip()
# 종료
pygame.quit()
