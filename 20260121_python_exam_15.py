# ## 2026-01-21 python lecture
# # ==================================================================

# import pygame
# import pyautogui
# import random

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


# def Alert_Show(str):
#     pyautogui.alert(f"{str}")


# hero = Img_Object()
# hero.add_img("D:/KJS/PYTHON/image/airplane.jpg")
# hero.change_size(80, 80)
# hero.x = round(size[0] / 2) - round(hero.width / 2)
# hero.y = size[1] - hero.height - 100
# hero.move = 10
# k = 0
# left_move = False
# right_move = False
# space_on = False
# missile_list = []  # 미사일 객체를 저장할 리스트
# enemy_list = []  # 적기 객체를 저장할 리스트
# # 4.이벤트
# system_exit = 0
# while system_exit == 0:
#     clock.tick(60)  # fps설정 => 프레임속도
#     # 입력(키보드, 마우스)의 감지 => 활용
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             system_exit = 1
#         if event.type == pygame.KEYDOWN:  # 키가 눌렸을 때
#             if event.key == pygame.K_LEFT:  # 방향키 왼쪽
#                 left_move = True
#             if event.key == pygame.K_RIGHT:  # 방향키 오른쪽
#                 right_move = True
#             if event.key == pygame.K_SPACE:
#                 space_on = True
#         elif event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT:  # 방향키 왼쪽
#                 left_move = False
#             if event.key == pygame.K_RIGHT:  # 방향키 오른쪽
#                 right_move = False
#             if event.key == pygame.K_SPACE:
#                 space_on = False
#     # 변화(입력에 따른 변화, 시간에 따른 변화)
#     if left_move == True:
#         hero.x -= hero.move
#         if hero.x <= 0:
#             hero.x = 0
#     elif right_move == True:
#         hero.x += hero.move
#         if hero.x >= size[0] - hero.width:
#             hero.x = size[0] - hero.width

#     if space_on == True and k % 6 == 0:
#         missile = Img_Object()  # 미사일 객체 생성 => 위 if문에 조건이 True일 때
#         missile.add_img("D:/KJS/PYTHON/image/missile.jpg")
#         missile.change_size(45, 50)

#         # 미사일 위치 설정
#         missile.x = hero.x + hero.width / 2 - missile.width / 2
#         missile.y = hero.y - missile.height - 10
#         missile.move = 7  # 미사일 속도
#         missile_list.append(missile)  # 위에서 미리 만들어준 미사일 리스트에 append
#     k += 1

#     delete_missile_list = []  # 삭제할 미사일을 저장할 리스트 생성

#     for m in missile_list:
#         m.y -= m.move
#         if m.y <= -m.height:
#             delete_missile_list.append(m)

#     for m in delete_missile_list:
#         if m in missile_list:  # 리스트에 존재하는지 확인 후 삭제
#             missile_list.remove(m)
#             # print("미사일 제거")
#     if (
#         random.random() >= 0.98
#     ):  # 함수가 반환한 난수가 0.98보다 크거나 같은지 확인. 약 2%의 확률로 조건이 참이 된다
#         enemy = Img_Object()
#         enemy.add_img("D:/KJS/PYTHON/image/germ.jpg")
#         enemy.change_size(35, 35)
#         # enemy 의 x좌표를 화면 가로범위 내의 랜덤한 위치로 설정, 주인공의 중앙을 기준으로
#         # 한 범위내에서 랜덤한 위치를 선택
#         enemy.x = random.randrange(
#             0 + round(hero.width / 2), size[0] - enemy.width - round(hero.width / 2)
#         )
#         enemy.y = 15  # enemy의 y좌표를 15로 고정
#         enemy.move = 5
#         enemy_list.append(enemy)

#     delete_enemy_list = []  # 화면밖을 벗어난 enemy 객체를 저장할 리스트

#     for e in enemy_list:
#         e.y += e.move
#         if e.y > size[1]:
#             delete_enemy_list.append(e)
#     for e in delete_enemy_list:
#         if e in enemy_list:
#             enemy_list.remove(e)
#             # print("enemy 제거")

#     # missile과 enemy 충돌
#     crash_m_list = []
#     crash_e_list = []
#     for m in missile_list:
#         for e in enemy_list:
#             if (m.x - e.width <= e.x <= m.x + m.width) and (
#                 m.y - e.height <= e.y <= m.y + m.height
#             ):
#                 crash_m_list.append(m)
#                 crash_e_list.append(e)

#     # missile과 enemy 제거
#     for m in crash_m_list:
#         missile_list.remove(m)
#         print("충돌 missile 제거")

#     for e in crash_e_list:
#         enemy_list.remove(e)
#         print("충돌 enemy 제거")

#     for e in enemy_list:
#         if (hero.x - e.width <= e.x <= hero.x + e.width) and (
#             hero.y - e.height <= e.y <= hero.y + e.height
#         ):
#             Alert_Show("게임종료")
#             pygame.quit()

#     # 전사작업(그리기)
#     screen.fill(black_color)
#     hero.show_img()
#     for m in missile_list:
#         m.show_img()  # 미사일을 게임 화면에 표시
#     for e in enemy_list:
#         e.show_img()  # enemy 게임 화면에 표시
#     # 업데이트
#     pygame.display.flip()
# # 종료
# pygame.quit()

# ==================================================================================================
# ==================================================================================================
# pygame 풀이

import pygame
import random
import time  # 시간과 관련된

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
hero.add_img("C:/Users/admin/Desktop/pyhon_25_12/pygame/hero.jpg")
hero.change_size(80, 80)
hero.x = round(size[0] / 2) - round(hero.width / 2)
hero.y = size[1] - hero.height - 100
hero.move = 10
k = 0
left_move = False
right_move = False
space_on = False
missile_list = []  # 미사일 객체를 저장할 리스트
enemy_list = []  # 적기 객체를 저장할 리스트
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
        missile.add_img("C:/Users/admin/Desktop/pyhon_25_12/pygame/missile.png")
        missile.change_size(45, 50)

        # 미사일 위치 설정
        missile.x = hero.x + hero.width / 2 - missile.width / 2
        missile.y = hero.y - missile.height - 10
        missile.move = 7  # 미사일 속도
        missile_list.append(missile)  # 위에서 미리 만들어준 미사일 리스트에 append
    k += 1

    delete_missile_list = []  # 삭제할 미사일을 저장할 리스트 생성

    for m in missile_list:
        m.y -= m.move
        if m.y <= -m.height:
            delete_missile_list.append(m)

    for m in delete_missile_list:
        if m in missile_list:  # 리스트에 존재하는지 확인 후 삭제
            missile_list.remove(m)
            # print("미사일 제거")
    if (
        random.random() >= 0.98
    ):  # 함수가 반환한 난수가 0.98보다 크거나 같은지 확인. 약 2%의 확률로 조건이 참이 된다
        enemy = Img_Object()
        enemy.add_img("C:/Users/admin/Desktop/pyhon_25_12/pygame/enemy.png")
        enemy.change_size(35, 35)
        # enemy 의 x좌표를 화면 가로범위 내의 랜덤한 위치로 설정, 주인공의 중앙을 기준으로
        # 한 범위내에서 랜덤한 위치를 선택
        enemy.x = random.randrange(
            0 + round(hero.width / 2), size[0] - enemy.width - round(hero.width / 2)
        )
        enemy.y = 15  # enemy의 y좌표를 15로 고정
        enemy.move = 5
        enemy_list.append(enemy)

    delete_enemy_list = []  # 화면밖을 벗어난 enemy 객체를 저장할 리스트

    for e in enemy_list:
        e.y += e.move
        if e.y > size[1]:
            delete_enemy_list.append(e)
    for e in delete_enemy_list:
        if e in enemy_list:
            enemy_list.remove(e)
            # print("enemy 제거")

    # missile과 enemy 충돌
    crash_m_list = []
    crash_e_list = []
    for m in missile_list:
        for e in enemy_list:
            if (m.x - e.width <= e.x <= m.x + m.width) and (
                m.y - e.height <= e.y <= m.y + m.height
            ):
                crash_m_list.append(m)
                crash_e_list.append(e)

    # missile과 enemy 제거
    for m in crash_m_list:
        missile_list.remove(m)
        # print("충돌 missile 제거")

    for e in crash_e_list:
        enemy_list.remove(e)
        # print("충돌 enemy 제거")

    # hero와 missile 충돌
    crash_h_e_list = []
    for e in enemy_list:
        if (hero.x - e.width <= e.x <= hero.x + hero.width) and (
            hero.y - e.height <= e.y <= hero.y + hero.height
        ):
            crash_h_e_list.append(e)

    # hero와 충돌한 enemy 제거
    for e in crash_h_e_list:
        if e in enemy_list:
            enemy_list.remove(e)
            # print("hero 충돌한 enemy 제거")

    if crash_h_e_list:
        system_exit = 1
        time.sleep(2)  # 주어진 시간(초)만큼 프로그램의 실행을 일시중지

    # 전사작업(그리기)
    screen.fill(black_color)
    hero.show_img()
    for m in missile_list:
        m.show_img()  # 미사일을 게임 화면에 표시
    for e in enemy_list:
        e.show_img()  # enemy 게임 화면에 표시
    # 업데이트
    pygame.display.flip()
# 종료
pygame.quit()
