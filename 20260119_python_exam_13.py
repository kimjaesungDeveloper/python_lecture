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

# 게임 내에서 사용할 이미지를 불러온다. 경로는 본인의 해당 이미지 파일이 있는 곳에 맞게 해야된다.
hero = pygame.image.load("D:\KJS\image/airplane.jpg").convert_alpha()  # 이미지 최적화

# 불러온 이미지의 크기를 100,100 픽셀로 조정
hero = pygame.transform.scale(hero, (100, 100))

k = 0
# 4.이벤트
system_exit = 0
while system_exit == 0:
    clock.tick(60)  # fps설정 => 프레임속도
    # 입력(키보드, 마우스)의 감지 => 활용
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            system_exit = 1
    # 변화(입력에 따른 변화, 시간에 따른 변화)
    k += 1

    # 전사작업(그리기)
    screen.fill(black_color)
    # 화면에 hero 이미지를 그린다 위치는 200, 300 위치에 그린다.
    screen.blit(hero, (150, 700))
    # 업데이트
    pygame.display.flip()

# 종료
pygame.quit()
