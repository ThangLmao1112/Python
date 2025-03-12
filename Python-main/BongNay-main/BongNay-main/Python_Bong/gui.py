import pygame
import random

# Khởi tạo pygame
pygame.init()

# Kích thước màn hình
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Màu sắc
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Kích thước thanh chắn
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10

# Kích thước bóng
BALL_RADIUS = 8

# Kích thước viên gạch
BRICK_WIDTH = 50
BRICK_HEIGHT = 20

# Danh sách vật phẩm
POWERUP_SIZE = 15

# Biến điều khiển trạng thái trò chơi
game_started = False
game_over = False
current_level = 1
max_levels = 3

def create_bricks(level):
    bricks = []
    for x in range(10):
        for y in range(3 + level):  # Tăng số hàng gạch theo cấp độ
            brick = pygame.Rect(x * (BRICK_WIDTH + 5) + 25, y * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
            bricks.append(brick)
    return bricks

def reset_game():
    global paddle, ball, ball_dx, ball_dy, bricks, power_ups, current_level, game_started, game_over
    game_started = False
    game_over = False
    current_level = 1
    paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_dx, ball_dy = 4 * random.choice((1, -1)), -4
    bricks = create_bricks(current_level)
    power_ups = []

def next_level():
    global current_level, game_started
    if current_level < max_levels:
        current_level += 1
        reset_game()
    else:
        print("You Win All Levels!")
        game_started = False

def draw_restart_button():
    font = pygame.font.Font(None, 32)
    text = font.render("Restart", True, BLACK)
    button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 + 40, 100, 40)
    pygame.draw.rect(screen, GRAY, button_rect)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + 57 - text.get_height() // 2))
    return button_rect

reset_game()

# Chạy trò chơi
running = True
while running:
    screen.fill(BLACK)
    
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over:
                mouse_x, mouse_y = event.pos
                if restart_button.collidepoint((mouse_x, mouse_y)):
                    reset_game()
            else:
                game_started = True
    
    if game_over:
        font = pygame.font.Font(None, 48)
        text = font.render("Game Over", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - 20))
        restart_button = draw_restart_button()
    elif not game_started:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Nhan chuot de bat dau voi cap {current_level}", True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    else:
        pygame.time.delay(20)
        
        # Điều khiển thanh chắn
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.move_ip(-6, 0)
        if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
            paddle.move_ip(6, 0)
        
        # Cập nhật vị trí bóng
        ball.move_ip(ball_dx, ball_dy)
        
        # Kiểm tra va chạm với tường
        if ball.left <= 0 or ball.right >= WIDTH:
            ball_dx = -ball_dx
        if ball.top <= 0:
            ball_dy = -ball_dy
        
        # Kiểm tra va chạm với thanh chắn
        if ball.colliderect(paddle):
            ball_dy = -ball_dy
        
        # Kiểm tra va chạm với gạch
        for brick in bricks[:]:
            if ball.colliderect(brick):
                bricks.remove(brick)
                ball_dy = -ball_dy
                # Tạo vật phẩm với xác suất 30%
                if random.randint(1, 10) <= 3:
                    power_ups.append(pygame.Rect(brick.centerx, brick.centery, POWERUP_SIZE, POWERUP_SIZE))
                break
        
        # Cập nhật vật phẩm
        for power_up in power_ups[:]:
            power_up.move_ip(0, 3)
            if power_up.colliderect(paddle):
                PADDLE_WIDTH += 20  # Làm thanh chắn to hơn khi nhận vật phẩm
                paddle.width = PADDLE_WIDTH
                power_ups.remove(power_up)
            elif power_up.top > HEIGHT:
                power_ups.remove(power_up)
        
        # Kiểm tra thua cuộc
        if ball.bottom >= HEIGHT:
            game_over = True
        
        # Kiểm tra chuyển sang cấp độ mới
        if not bricks:
            next_level()
        
        # Vẽ thanh chắn, bóng và gạch
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)
        for power_up in power_ups:
            pygame.draw.ellipse(screen, GREEN, power_up)
    
    pygame.display.flip()

pygame.quit()
