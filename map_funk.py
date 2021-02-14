import sys
import requests
import pygame
import os


def map_resopnse(ll, z, map_mode):
    map_request = f"https://static-maps.yandex.ru/1.x/?l={map_mode}&ll={','.join(ll)}&z={z}&size=450,450"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file


def change_map(screen,map_file):
    screen.blit(pygame.image.load(map_file), (0, 0))
    os.remove(map_file)
