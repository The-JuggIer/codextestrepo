import pygame
import sys
import random

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
ROAD_WIDTH = 200
LINE_HEIGHT = 40
LINE_SPACING = 20
LINE_SPEED = 5
CAR_WIDTH, CAR_HEIGHT = 40, 80
CAR_SPEED = 5
ENEMY_SPEED = 5


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Endless Car Drive")
    clock = pygame.time.Clock()

    car = pygame.Rect(
        WINDOW_WIDTH // 2 - CAR_WIDTH // 2,
        WINDOW_HEIGHT - CAR_HEIGHT - 10,
        CAR_WIDTH,
        CAR_HEIGHT,
    )

    car_image = pygame.image.load(
        "75-750271_car-top-view-png-audi-transparent-png.png"
    ).convert_alpha()
    car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

    font = pygame.font.SysFont(None, 24)
    enemy_image = pygame.Surface((CAR_WIDTH, CAR_HEIGHT), pygame.SRCALPHA)
    enemy_image.fill((255, 255, 255))
    text = font.render("BMW", True, (0, 0, 0))
    text_rect = text.get_rect(center=(CAR_WIDTH // 2, CAR_HEIGHT // 2))
    enemy_image.blit(text, text_rect)

    enemies = []
    next_spawn = pygame.time.get_ticks() + 5000

    lines = []
    y = -LINE_HEIGHT
    while y < WINDOW_HEIGHT:
        lines.append(
            pygame.Rect(WINDOW_WIDTH // 2 - 2, y, 4, LINE_HEIGHT)
        )
        y += LINE_HEIGHT + LINE_SPACING

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.x -= CAR_SPEED
        if keys[pygame.K_RIGHT]:
            car.x += CAR_SPEED

        car.x = max(
            WINDOW_WIDTH // 2 - ROAD_WIDTH // 2,
            min(car.x, WINDOW_WIDTH // 2 + ROAD_WIDTH // 2 - CAR_WIDTH),
        )

        now = pygame.time.get_ticks()
        if now >= next_spawn:
            spawn_x = (
                WINDOW_WIDTH // 2 - ROAD_WIDTH // 2
                + random.randint(0, ROAD_WIDTH - CAR_WIDTH)
            )
            enemies.append(
                pygame.Rect(spawn_x, -CAR_HEIGHT, CAR_WIDTH, CAR_HEIGHT)
            )
            next_spawn = now + random.randint(3000, 7000)

        for line in lines:
            line.y += LINE_SPEED
            if line.y > WINDOW_HEIGHT:
                line.y = -LINE_HEIGHT

        for enemy in enemies[:]:
            enemy.y += ENEMY_SPEED
            if enemy.y > WINDOW_HEIGHT:
                enemies.remove(enemy)

        screen.fill((0, 150, 0))
        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (WINDOW_WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, WINDOW_HEIGHT),
        )

        for line in lines:
            pygame.draw.rect(screen, (255, 255, 255), line)

        for enemy in enemies:
            screen.blit(enemy_image, enemy)

        screen.blit(car_image, car)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
