import pygame
import os

# game setup
WIDTH = 1600	# 1280 x 720 - full is 1600x900
HEIGHT = 900
FPS      = 60
TILESIZE = 32

# colours
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)

def import_folder(path):
    surface_list = []

    for _,__,img_files in os.walk(path):
        for image in img_files:
            full_path = path + '/' + image		
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list

def extract_number(filename):
    return int(filename.split(".")[0])

def import_folder(path):
    surface_list = []

    for root, dirs, img_files in os.walk(path): 
        sorted_file_names = sorted(img_files, key=extract_number)  

    for img_name in sorted_file_names:
        full_path = path + '/' + img_name
        image_surf = pygame.image.load(full_path).convert_alpha()
        surface_list.append(image_surf)

    return surface_list
        

monster_data = {
    "necromancer": {"health": 100, "attack_damage": 20, "roaming_speed": 2, "hunting_speed": [4,4,7,7,7], "image": pygame.image.load("necromancer/roam/0.png"), "image_scale": 1.5, "hitbox_rect": pygame.Rect(0,0,75,100), "animation_speed": 0.2, "roam_animation_speed": 0.05, "death_animation_speed": 0.12, "notice_radius": 500},
    "nightborne": {"health": 100, "attack_damage": 40, "roaming_speed": 4, "hunting_speed": [4,4,6,6,6], "image": pygame.image.load("nightborne/hunt/1.png"), "image_scale": 1.9, "hitbox_rect": pygame.Rect(0,0,75,90), "animation_speed": 0.1, "roam_animation_speed": 0.12, "death_animation_speed": 0.2, "notice_radius": 400},
}

game_stats = {
    "enemies_killed_or_removed": 0, "necromancer_death_count": 0, "nightborne_death_count": 0, "coins": 0, "health_potion_heal": 20, "current_wave": 1, "number_of_enemies": [3, 6,7], "wave_cooldown": 6000, "num_health_potions": 3
}

items = {
    "health potion": {"image": pygame.image.load("items/health potion/10.png"), "has_animation": False},
    "coin": {"image": pygame.image.load("items/coin/0.png"), "has_animation": True}

}








# monster_data = {
#     "necromancer": {"name": "necromancer", "health": 100, "attack_damage": 20, "roaming_speed": 2, "hunting_speed": [4,4,7,7,7], "image": pygame.image.load("necromancer/animations/0.png").convert_alpha(), "image_scale": 1.9, "hitbox_rect": pygame.Rect(0,0,75,100), "animation_speed": 0.2, "roam_animation_speed": 0.05, "death_animation_speed": 0.12, "move_sprites": necromancer_move_sprites, "notice_radius": 500, "idle_sprites": necromancer_idle_sprites, "death_sprites": necromancer_death_sprites},
#     "nightborne": {"name": "nightborne", "health": 100, "attack_damage": 40, "roaming_speed": 4, "hunting_speed": [4,4,6,6,6], "image": pygame.image.load("nightborne/run/1.png").convert_alpha(), "image_scale": 2.5, "hitbox_rect": pygame.Rect(0,0,75,90), "animation_speed": 0.1, "roam_animation_speed": 0.12, "death_animation_speed": 0.225, "move_sprites": nightborne_move_sprites, "notice_radius": 400, "idle_sprites": nightborne_idle_sprites, "death_sprites": nightborne_death_sprites},
#     }

# game_stats = {
#     "necromancer_death_count": 0, "nightborne_death_count": 0
# }










# Animations

# necromancer_dying_sprites = []
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/1.png"))
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/2.png")) 
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/3.png")) 
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/4.png")) 
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/5.png")) 
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/6.png")) 
# necromancer_dying_sprites.append(pygame.image.load("necromancer/dying/7.png")) 

# necromancer_move_sprites = []
# necromancer_move_sprites.append(pygame.image.load("necromancer/animations/sprite_10.png"))
# necromancer_move_sprites.append(pygame.image.load("necromancer/animations/sprite_11.png"))
# necromancer_move_sprites.append(pygame.image.load("necromancer/animations/sprite_12.png"))
# necromancer_move_sprites.append(pygame.image.load("necromancer/animations/sprite_13.png"))
# necromancer_move_sprites.append(pygame.image.load("necromancer/animations/sprite_14.png"))
# necromancer_move_sprites.append(pygame.image.load("necromancer/animations/sprite_15.png"))

# necromancer_idle_sprites = []
# necromancer_idle_sprites.append(pygame.image.load("necromancer/roaming/51.png"))
# necromancer_idle_sprites.append(pygame.image.load("necromancer/roaming/52.png"))


# nightborne_move_sprites = []
# nightborne_move_sprites.append(pygame.image.load("nightborne/run/1.png"))
# nightborne_move_sprites.append(pygame.image.load("nightborne/run/2.png"))
# nightborne_move_sprites.append(pygame.image.load("nightborne/run/3.png"))
# nightborne_move_sprites.append(pygame.image.load("nightborne/run/4.png"))
# nightborne_move_sprites.append(pygame.image.load("nightborne/run/5.png"))
# nightborne_move_sprites.append(pygame.image.load("nightborne/run/6.png"))

# nightborne_idle_sprites = []
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/0.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/1.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/2.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/3.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/4.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/5.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/6.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/7.png"))
# nightborne_idle_sprites.append(pygame.image.load("nightborne/idle/8.png"))

# nightborne_death_sprites = []
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/31.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/32.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/33.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/34.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/35.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/36.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/37.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/38.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/39.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/40.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/41.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/42.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/43.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/44.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/45.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/46.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/47.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/48.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/49.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/50.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/51.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/52.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/53.png"))
# nightborne_death_sprites.append(pygame.image.load("nightborne/death/54.png"))







# Ctrl + Shift + P opens command palette

























