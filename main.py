from map_funk import *

ll = ['38.205261', '44.419055']
z = 5
pygame.init()
screen = pygame.display.set_mode((450, 450))
change_map(screen, map_resopnse(ll, z))
while pygame.event.wait().type != pygame.QUIT:
    key = pygame.key.get_pressed()
    if any(key):
        if key[pygame.K_PAGEDOWN] and z > 1:
            z -= 1
        if key[pygame.K_PAGEUP] and z < 17:
            z += 1
        change_map(screen, map_resopnse(ll, z))
pygame.quit()
