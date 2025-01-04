import pygame
#########################################################################
# 초기화
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")
# FPS
clock = pygame.time.Clock()
#########################################################################


# 이미지 로딩
background = pygame.image.load("background.png")
character = pygame.image.load("C:/Users/User/PycharmProjects/pygamebasic/char1.png")

character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2 - character_width / 2
character_y_pos = screen_height - character_height

character_rect = character.get_rect()
character_rect.left = character_x_pos
character_rect.top = character_y_pos


to_x = 0
to_y = 0

enemy = pygame.image.load("C:/Users/User/PycharmProjects/pygamebasic/enemy1.png")

enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = screen_width / 2 - enemy_width / 2
enemy_y_pos = screen_height / 2 - enemy_height / 2


character_speed = 0.6

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 10

# 시작 시간
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(60)

    # 이벤트 처리 (키보드, 마우스)


    # 캐릭터 위치 정의


    # 충돌 처리


    # 화면 그리기

pygame.time.delay(2000)
pygame.quit()