import pygame
import sys

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
ROAD_WIDTH = 200
LINE_HEIGHT = 40
LINE_SPACING = 20
LINE_SPEED = 5
CAR_WIDTH, CAR_HEIGHT = 40, 80
CAR_SPEED = 5


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

        for line in lines:
            line.y += LINE_SPEED
            if line.y > WINDOW_HEIGHT:
                line.y = -LINE_HEIGHT

        screen.fill((0, 150, 0))
        pygame.draw.rect(
            screen,
            (50, 50, 50),
            (WINDOW_WIDTH // 2 - ROAD_WIDTH // 2, 0, ROAD_WIDTH, WINDOW_HEIGHT),
        )

        for line in lines:
            pygame.draw.rect(screen, (255, 255, 255), line)

        pygame.draw.rect(screen, (255, 0, 0), car)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
