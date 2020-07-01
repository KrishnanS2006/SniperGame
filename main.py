import pygame
pygame.init()
pygame.font.init()

W = 800
H = 600
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scarlett Inferno")
clock = pygame.time.Clock()

bg = pygame.image.load("sniper_bg.jpg")
bg_pos = [0, 0]
move_speed = 8

playerImg = pygame.image.load("player.png")
# person_img = pygame.image.load()

KILLS = 0


def redraw(win):
    win.blit(bg, bg_pos)
    pygame.display.flip()


def main():
    global bg_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            bg_pos[0] += move_speed
        if keys[pygame.K_RIGHT]:
            bg_pos[0] -= move_speed
        if keys[pygame.K_UP]:
            bg_pos[1] += move_speed
        if keys[pygame.K_DOWN]:
            bg_pos[1] -= move_speed
        redraw(win)
        clock.tick(30)


main()