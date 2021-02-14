from map_funk import *
import pygame

ll = ['38.205261', '44.419055']
z = 1
map_mode = 0
map_mods = ['map', 'sat', 'sat,skl']
map_mods_hrf = ['Карта', 'Сутник', 'Гибрид']
color_btn_map_mode = (51, 51, 51)

running = True
pygame.init()
screen = pygame.display.set_mode((450, 450))
change_map(screen, map_resopnse(ll, z, map_mods[map_mode]))
btn_map_mode = pygame.Rect(10, 10, 100, 30)

while running:
    key = pygame.key.get_pressed()
    if any(key):
        if key[pygame.K_PAGEDOWN] and z > 0:
            z -= 1

        if key[pygame.K_PAGEUP] and z < 17:
            z += 1
        if z:
            coef = 1 / (z * 4)
            if z < 3:
                coef *= 5
            elif z < 10:
                coef *= 3
            if key[pygame.K_UP]:
                ll[1] = str(float(ll[1]) + coef)
            if key[pygame.K_DOWN]:
                ll[1] = str(float(ll[1]) - coef)
            if key[pygame.K_LEFT]:
                ll[0] = str(float(ll[0]) - coef)
            if key[pygame.K_RIGHT]:
                ll[0] = str(float(ll[0]) + coef)
        change_map(screen, map_resopnse(ll, z, map_mods[map_mode]))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if btn_map_mode.collidepoint(event.pos):
                color_btn_map_mode = (81, 81, 81)
            else:
                color_btn_map_mode = (51, 51, 51)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if btn_map_mode.collidepoint(event.pos):
                map_mode += 1
                map_mode %= 3
                change_map(screen, map_resopnse(ll, z, map_mods[map_mode]))
    pygame.draw.rect(screen, color_btn_map_mode, btn_map_mode, border_radius=4)
    century_schoolbook = pygame.font.SysFont('Century Schoolbook', 25)
    map_mode_text = century_schoolbook.render(map_mods_hrf[map_mode], False, (102, 102, 102))
    screen.blit(map_mode_text, btn_map_mode[:2])
    pygame.display.flip()


pygame.quit()
