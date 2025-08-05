import pygame
import sys

# 초기화
pygame.init()
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("블럭깨기 게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# 패들 설정
PADDLE_WIDTH, PADDLE_HEIGHT = 300, 15  # 기존 100에서 3배로 증가
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 8

# 공 설정
BALL_RADIUS = 10
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed = [3, -3]  # 속도를 5에서 3으로 낮춤

# 블럭 설정
BLOCK_ROWS, BLOCK_COLS = 6, 10
BLOCK_WIDTH = WIDTH // BLOCK_COLS
BLOCK_HEIGHT = 30
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * BLOCK_WIDTH + 1, row * BLOCK_HEIGHT + 60, BLOCK_WIDTH - 2, BLOCK_HEIGHT - 2)
        blocks.append(block)

font = pygame.font.SysFont(None, 48)
game_over = False
game_clear = False

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, RED, ball)
    for block in blocks:
        pygame.draw.rect(screen, GREEN, block)
    if game_over:
        msg = font.render("게임 오버!", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - msg.get_height() // 2))
    elif game_clear:
        msg = font.render("클리어!", True, WHITE)
        screen.blit(msg, (WIDTH // 2 - msg.get_width() // 2, HEIGHT // 2 - msg.get_height() // 2))
    pygame.display.flip()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over and not game_clear:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.x += paddle_speed

        ball.x += ball_speed[0]
        ball.y += ball_speed[1]

        # 벽 충돌
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_speed[0] = -ball_speed[0]
        if ball.top <= 0:
            ball_speed[1] = -ball_speed[1]

        # 패들 충돌
        if ball.colliderect(paddle):
            ball_speed[1] = -abs(ball_speed[1])
            # 공이 패들 왼쪽/오른쪽에 맞으면 방향 조정
            offset = (ball.centerx - paddle.centerx) / (PADDLE_WIDTH // 2)
            ball_speed[0] += int(offset * 2)
            ball_speed[0] = max(-8, min(8, ball_speed[0]))

        # 블럭 충돌
        hit_index = ball.collidelist(blocks)
        if hit_index != -1:
            hit_block = blocks.pop(hit_index)
            # 충돌 방향 보정
            if abs(ball.bottom - hit_block.top) < 10 and ball_speed[1] > 0:
                ball_speed[1] = -ball_speed[1]
            elif abs(ball.top - hit_block.bottom) < 10 and ball_speed[1] < 0:
                ball_speed[1] = -ball_speed[1]
            else:
                ball_speed[0] = -ball_speed[0]

        # 바닥에 닿으면 게임 오버
        if ball.bottom >= HEIGHT:
            game_over = True

        # 모든 블럭을 깼을 때
        if not blocks:
            game_clear = True

    draw()