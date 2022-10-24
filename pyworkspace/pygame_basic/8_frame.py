import pygame

#기본 초기화
pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("New Game")

clock = pygame.time.Clock()
##############################################################################

#1. 사용자 게임 초기화(배경화면, 게임 이미지, 좌표, 속도, 폰트 등등)
running = True

while running:
    dt = clock.tick(30)

    #2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #3. 가로 경계값 처리
    

    #4. 세로 경계값 처리

    #5. 게임 캐릭터 위치 정의

    #6. 충돌 처리

    #7. 화면에 그리기

    pygame.display.update()

pygame.quit()