
from map_funk import *

ll = ['38.205261', '44.419055']
z = 1
pygame.init()
screen = pygame.display.set_mode((450, 450))
change_map(screen, map_resopnse(ll, z))

while pygame.event.wait().type != pygame.QUIT:
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
        change_map(screen, map_resopnse(ll, z))

pygame.quit()
