import pygame


def main():
    pygame.init()

    # create a window
    screen = pygame.display.set_mode((800, 600))

    # set the title of the window
    pygame.display.set_caption("Pygame GitHub Copilot Test Window")

    # create a background surface
    background = pygame.Surface(screen.get_size())
    background.fill((255, 255, 255))
    screen.blit(background, (0, 0))

    # update the display
    pygame.display.flip()

    # create a font
    font = pygame.font.SysFont("None", 48)
    font = pygame.font.SysFont("None", 48)

    # create a text
    text = font.render("Hello World", True, (0, 0, 0))

    # create a rectangle
    # set the position of the rectangle
    rect = text.get_rect()
    rect.center = (400, 300)

    # blit the text
    screen.blit(text, rect)

    # update the display
    pygame.display.flip()

    # create a vertical menu with 3 options out of Rect with text labels and a white background
    menu = pygame.Rect(0, 0, 200, 200)
    menu.center = (400, 300)
    menu_font = pygame.font.SysFont("None", 24)
    menu_text = menu_font.render("Menu", True, (0, 0, 0))
    menu_rect = menu_text.get_rect()
    menu_rect.center = (menu.centerx, menu.centery - 50)
    screen.blit(menu_text, menu_rect)

    # bounce a ball back and forth
    ball = pygame.Rect(0, 0, 50, 50)
    ball.center = (400, 300)
    ball_speed = [1, 1]
    ball_color = (0, 0, 0)

    # create a clock
    clock = pygame.time.Clock()

    # main loop
    # wait until user presses escape
    while True:
        # on every frame, check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

        # move ball
        ball.move_ip(ball_speed)
        # bounce ball off the walls
        if ball.left < 0 or ball.right > 800:
            ball_speed[0] = -ball_speed[0]
        if ball.top < 0 or ball.bottom > 600:
            ball_speed[1] = -ball_speed[1]

        # draw the ball
        pygame.draw.rect(screen, ball_color, ball)

        # draw the menu
        pygame.draw.rect(screen, (100, 100, 100), menu)

        # update the display
        pygame.display.flip()
        screen.fill((255, 255, 255))

        clock.tick(60)


if __name__ == "__main__":
    main()
