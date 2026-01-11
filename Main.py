import pygame, sys, random, ctypes, platform
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)
        self.new_block = False

        def load_scaled_image(path):
            return pygame.transform.scale(
                pygame.image.load(path).convert_alpha(), (cell_size, cell_size)
            )

        # HEADS
        self.head_right = load_scaled_image("images/snake_head_1.png")
        self.head_down = load_scaled_image("images/snake_head_2.png")
        self.head_left = load_scaled_image("images/snake_head_3.png")
        self.head_up = load_scaled_image("images/snake_head_4.png")

        # TAILS
        self.tail_right = load_scaled_image("images/snake_tail_1.png")
        self.tail_down = load_scaled_image("images/snake_tail_2.png")
        self.tail_left = load_scaled_image("images/snake_tail_3.png")
        self.tail_up = load_scaled_image("images/snake_tail_4.png")

        # BODY STRAIGHTS
        self.body_horizontal = load_scaled_image("images/snake_body_1.png")
        self.body_vertical = load_scaled_image("images/snake_body_2.png")

        # BODY CURVES
        self.body_br = load_scaled_image("images/snake_curve_1.png")  
        self.body_bl = load_scaled_image("images/snake_curve_2.png")  
        self.body_tl = load_scaled_image("images/snake_curve_3.png")  
        self.body_tr = load_scaled_image("images/snake_curve_4.png")  

        self.crunch_sound = pygame.mixer.Sound("sound/crunch.wav")

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

        for index, block in enumerate(self.body):
            x_pos = block.x * cell_size
            y_pos = block.y * cell_size
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                game_surface.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                game_surface.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    game_surface.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:
                    game_surface.blit(self.body_horizontal, block_rect)
                else:
                    if (
                        previous_block.x == -1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == -1
                    ):
                        game_surface.blit(self.body_tl, block_rect)
                    elif (
                        previous_block.x == -1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == -1
                    ):
                        game_surface.blit(self.body_bl, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == -1
                        or previous_block.y == -1
                        and next_block.x == 1
                    ):
                        game_surface.blit(self.body_tr, block_rect)
                    elif (
                        previous_block.x == 1
                        and next_block.y == 1
                        or previous_block.y == 1
                        and next_block.x == 1
                    ):
                        game_surface.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1, 0):
            self.head = self.head_left
        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right
        elif head_relation == Vector2(0, 1):
            self.head = self.head_up
        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right
        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up
        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:
    def __init__(self):
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(
            self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size
        )
        game_surface.blit(apple, fruit_rect)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if (
            not 0 <= self.snake.body[0].x < cell_number
            or not 0 <= self.snake.body[0].y < cell_number
        ):
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()

    def draw_grass(self):
        grass_color = (157, 199, 55)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size
                        )
                        pygame.draw.rect(game_surface, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size
                        )
                        pygame.draw.rect(game_surface, grass_color, grass_rect)

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 72, 12))
        score_x = (cell_size * cell_number) - 60
        score_y = (cell_size * cell_number) - 40
        score_rect = score_surface.get_rect(center=(score_x, score_y))
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(
            apple_rect.left,
            apple_rect.top,
            apple_rect.width + score_rect.width + 6,
            apple_rect.height,
        )

        pygame.draw.rect(game_surface, (167, 209, 61), bg_rect)
        game_surface.blit(score_surface, score_rect)
        game_surface.blit(apple, apple_rect)
        pygame.draw.rect(game_surface, (56, 72, 12), bg_rect, 2)


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.display.set_caption("Snake Game")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)
cell_size = 40
cell_number = 20
display_info = pygame.display.Info()
screen = pygame.display.set_mode(
    (display_info.current_w - 30, display_info.current_h - 60), pygame.RESIZABLE
)

if platform.system() == "Windows":
    hwnd = pygame.display.get_wm_info()["window"]
    ctypes.windll.user32.ShowWindow(hwnd, 3)  # 3 = SW_MAXIMIZE
game_width = cell_number * cell_size
game_height = cell_number * cell_size
game_surface = pygame.Surface((game_width, game_height))  # Fixed-size game surface
hwnd = pygame.display.get_wm_info()["window"]
# ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002)
clock = pygame.time.Clock()
apple = pygame.transform.scale(
    pygame.image.load("images/apple.png").convert_alpha(),
    (cell_size, cell_size),
)
game_font = pygame.font.Font("font/PoetsenOne-Regular.ttf", 25)

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)

    game_surface.fill((175, 215, 50))  # Background fill for game area
    main_game.draw_elements()

    # Center game_surface on the full screen
    screen.fill((0, 0, 0))  # Black bars
    x = (screen.get_width() - game_width) // 2
    y = (screen.get_height() - game_height) // 2
    screen.blit(game_surface, (x, y))

    pygame.display.update()
    clock.tick(60)
