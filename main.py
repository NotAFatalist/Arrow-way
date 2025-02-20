import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1920, 1000))
pygame.display.set_caption('Arrow Way')
icon = pygame.image.load('image/Arrow Way.ico').convert_alpha()
pygame.display.set_icon(icon)

#bg
bg1 = pygame.image.load('image/bg/BG1.png').convert_alpha()
bg2 = pygame.image.load('image/bg/bg2.png').convert_alpha()
bg3 = pygame.image.load('image/bg/bg3.png').convert_alpha()
ground = pygame.image.load('image/bg/ground.png').convert_alpha()
stone = pygame.image.load('image/bg/stone.png').convert_alpha()
dark_stone = pygame.image.load('image/bg/dark_stone.png').convert_alpha()
door = pygame.image.load('image/bg/door.png').convert_alpha()
heart = pygame.image.load('image/bg/heart.png').convert_alpha()
arrow_right = pygame.image.load('image/bg/arrow.png').convert_alpha()
arrow_left = pygame.image.load('image/bg/arrow_left.png').convert_alpha()
spike = pygame.image.load('image/bg/spike.png').convert_alpha()
spikes = pygame.image.load('image/bg/spikes.png').convert_alpha()
arrow = True
life_counter = 3


#sounds

bg1_sound = pygame.mixer.Sound('sounds/bg1.mp3')
bg2_sound = pygame.mixer.Sound('sounds/bg2.mp3')
bg3_sound = pygame.mixer.Sound('sounds/bg3.mp3')



label = pygame.font.Font('image/fonts/LilitaOne-Regular.ttf', 100)
lose_label = label.render('You lose', False, (255, 255, 255))
restart_label = label.render('Restart', False, (255, 255, 255))
restart_label_rect = restart_label.get_rect(topleft=(750, 500))
win_label = label.render('Congratulations, you win!', False, (255, 255, 255))




#player
player_count = 0
speed_player = 4
player_x = 100
player_y = 880
afk_side = True
is_jump = False
jump_count = 22
gravity = False
gravity_count = 1
walk_right = [
    pygame.image.load('image/walk_right/1.png').convert_alpha(),
    pygame.image.load('image/walk_right/1.png').convert_alpha(),
    pygame.image.load('image/walk_right/1.png').convert_alpha(),
    pygame.image.load('image/walk_right/1.png').convert_alpha(),
    pygame.image.load('image/walk_right/2.png').convert_alpha(),
    pygame.image.load('image/walk_right/2.png').convert_alpha(),
    pygame.image.load('image/walk_right/2.png').convert_alpha(),
    pygame.image.load('image/walk_right/2.png').convert_alpha(),
    pygame.image.load('image/walk_right/3.png').convert_alpha(),
    pygame.image.load('image/walk_right/3.png').convert_alpha(),
    pygame.image.load('image/walk_right/3.png').convert_alpha(),
    pygame.image.load('image/walk_right/3.png').convert_alpha(),
    pygame.image.load('image/walk_right/4.png').convert_alpha(),
    pygame.image.load('image/walk_right/4.png').convert_alpha(),
    pygame.image.load('image/walk_right/4.png').convert_alpha(),
    pygame.image.load('image/walk_right/4.png').convert_alpha(),
    pygame.image.load('image/walk_right/5.png').convert_alpha(),
    pygame.image.load('image/walk_right/5.png').convert_alpha(),
    pygame.image.load('image/walk_right/5.png').convert_alpha(),
    pygame.image.load('image/walk_right/5.png').convert_alpha(),
    pygame.image.load('image/walk_right/6.png').convert_alpha(),
    pygame.image.load('image/walk_right/6.png').convert_alpha(),
    pygame.image.load('image/walk_right/6.png').convert_alpha(),
    pygame.image.load('image/walk_right/6.png').convert_alpha(),
    pygame.image.load('image/walk_right/7.png').convert_alpha(),
    pygame.image.load('image/walk_right/7.png').convert_alpha(),
    pygame.image.load('image/walk_right/7.png').convert_alpha(),
    pygame.image.load('image/walk_right/7.png').convert_alpha(),
    pygame.image.load('image/walk_right/8.png').convert_alpha(),
    pygame.image.load('image/walk_right/8.png').convert_alpha(),
    pygame.image.load('image/walk_right/8.png').convert_alpha(),
    pygame.image.load('image/walk_right/8.png').convert_alpha(),
    pygame.image.load('image/walk_right/9.png').convert_alpha(),
    pygame.image.load('image/walk_right/9.png').convert_alpha(),
    pygame.image.load('image/walk_right/9.png').convert_alpha(),
    pygame.image.load('image/walk_right/9.png').convert_alpha(),
    pygame.image.load('image/walk_right/10.png').convert_alpha(),
    pygame.image.load('image/walk_right/10.png').convert_alpha(),
    pygame.image.load('image/walk_right/10.png').convert_alpha(),
    pygame.image.load('image/walk_right/10.png').convert_alpha(),
    pygame.image.load('image/walk_right/11.png').convert_alpha(),
    pygame.image.load('image/walk_right/11.png').convert_alpha(),
    pygame.image.load('image/walk_right/11.png').convert_alpha(),
    pygame.image.load('image/walk_right/11.png').convert_alpha(),
    pygame.image.load('image/walk_right/12.png').convert_alpha(),
    pygame.image.load('image/walk_right/12.png').convert_alpha(),
    pygame.image.load('image/walk_right/12.png').convert_alpha(),
    pygame.image.load('image/walk_right/12.png').convert_alpha(),
]
walk_left = [
    pygame.image.load('image/walk_left/1.png').convert_alpha(),
    pygame.image.load('image/walk_left/1.png').convert_alpha(),
    pygame.image.load('image/walk_left/1.png').convert_alpha(),
    pygame.image.load('image/walk_left/1.png').convert_alpha(),
    pygame.image.load('image/walk_left/2.png').convert_alpha(),
    pygame.image.load('image/walk_left/2.png').convert_alpha(),
    pygame.image.load('image/walk_left/2.png').convert_alpha(),
    pygame.image.load('image/walk_left/2.png').convert_alpha(),
    pygame.image.load('image/walk_left/3.png').convert_alpha(),
    pygame.image.load('image/walk_left/3.png').convert_alpha(),
    pygame.image.load('image/walk_left/3.png').convert_alpha(),
    pygame.image.load('image/walk_left/3.png').convert_alpha(),
    pygame.image.load('image/walk_left/4.png').convert_alpha(),
    pygame.image.load('image/walk_left/4.png').convert_alpha(),
    pygame.image.load('image/walk_left/4.png').convert_alpha(),
    pygame.image.load('image/walk_left/4.png').convert_alpha(),
    pygame.image.load('image/walk_left/5.png').convert_alpha(),
    pygame.image.load('image/walk_left/5.png').convert_alpha(),
    pygame.image.load('image/walk_left/5.png').convert_alpha(),
    pygame.image.load('image/walk_left/5.png').convert_alpha(),
    pygame.image.load('image/walk_left/6.png').convert_alpha(),
    pygame.image.load('image/walk_left/6.png').convert_alpha(),
    pygame.image.load('image/walk_left/6.png').convert_alpha(),
    pygame.image.load('image/walk_left/6.png').convert_alpha(),
    pygame.image.load('image/walk_left/7.png').convert_alpha(),
    pygame.image.load('image/walk_left/7.png').convert_alpha(),
    pygame.image.load('image/walk_left/7.png').convert_alpha(),
    pygame.image.load('image/walk_left/7.png').convert_alpha(),
    pygame.image.load('image/walk_left/8.png').convert_alpha(),
    pygame.image.load('image/walk_left/8.png').convert_alpha(),
    pygame.image.load('image/walk_left/8.png').convert_alpha(),
    pygame.image.load('image/walk_left/8.png').convert_alpha(),
    pygame.image.load('image/walk_left/9.png').convert_alpha(),
    pygame.image.load('image/walk_left/9.png').convert_alpha(),
    pygame.image.load('image/walk_left/9.png').convert_alpha(),
    pygame.image.load('image/walk_left/9.png').convert_alpha(),
    pygame.image.load('image/walk_left/10.png').convert_alpha(),
    pygame.image.load('image/walk_left/10.png').convert_alpha(),
    pygame.image.load('image/walk_left/10.png').convert_alpha(),
    pygame.image.load('image/walk_left/10.png').convert_alpha(),
    pygame.image.load('image/walk_left/11.png').convert_alpha(),
    pygame.image.load('image/walk_left/11.png').convert_alpha(),
    pygame.image.load('image/walk_left/11.png').convert_alpha(),
    pygame.image.load('image/walk_left/11.png').convert_alpha(),
    pygame.image.load('image/walk_left/12.png').convert_alpha(),
    pygame.image.load('image/walk_left/12.png').convert_alpha(),
    pygame.image.load('image/walk_left/12.png').convert_alpha(),
    pygame.image.load('image/walk_left/12.png').convert_alpha(),
]
afk_player_right = pygame.image.load('image/afk/afk_right.png').convert_alpha()
afk_player_left = pygame.image.load('image/afk/afk_left.png').convert_alpha()



#enemy2
afk_enemy2 = pygame.image.load('image/afk_enemy2/afk.png').convert_alpha()
afk_enemy2_left = pygame.image.load('image/afk_enemy2/afk_left.png').convert_alpha()
shooting_enemy2 = [
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy2/5.png').convert_alpha()


]
shooting_enemy2_left = [
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/1.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/2.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/3.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/4.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha(),
    pygame.image.load('image/shooting_enemy 2_left/5.png').convert_alpha()
]
direction_of_the_enemy2 = True
direction_of_the_enemy3 = True
direction_of_the_enemy4 = True
shooting_enemy_count = 0
shooting_enemy_count1 = 0
shooting_enemy_count_2 = 0
shooting_enemy_count2 = 0
shooting_enemy_count_3 = 0


shells = []

Run = True

timer_enemy2 = pygame.USEREVENT
pygame.time.set_timer(timer_enemy2, 2000)
lvl1 = True
lvl2 = False
lvl3 = False
agr = False
agr1 = False
agr2 = False





while Run:

    pygame.display.update()
    if life_counter:

        if lvl1:
            bg1_sound.play()
            bg1_sound.set_volume(1)
            bg2_sound.play()
            bg2_sound.set_volume(0)
            bg3_sound.play()
            bg3_sound.set_volume(0)
        elif lvl2:
            bg1_sound.play()
            bg1_sound.set_volume(0)
            bg2_sound.play()
            bg2_sound.set_volume(1)
            bg3_sound.play()
            bg3_sound.set_volume(0)
        else:
            bg1_sound.play()
            bg1_sound.set_volume(0)
            bg2_sound.play()
            bg2_sound.set_volume(0)
            bg3_sound.play()
            bg3_sound.set_volume(1)




        if life_counter and lvl1:

            screen.blit(bg1, (0, 0))
            for i in range(6):
                screen.blit(ground, (330 * i, 950))
            screen.blit(ground, (1832, 800))
            for i in range(6):
                screen.blit(ground, (275 * i, 655))
            screen.blit(ground, (-250, 505))
            for i in range(6):
                screen.blit(ground, (182 + 330 * i, 360))
            for i in range(life_counter):
                screen.blit(heart, (50 + (i * 100), 100))
            screen.blit(door, (1854, 289))
            screen.blit(spike, (525, 923))
            screen.blit(spike, (1200, 923))
            screen.blit(spike, (1100, 626))
            screen.blit(spike, (766, 330))
            screen.blit(spike, (1458, 330))

        #add_enemies




            if shells:
                for i in shells:
                    screen.blit(arrow, i[0])
                    if i[1] == 1:
                        i[0].x += 5
                    else:
                        i[0].x -= 5
                    if hit_box_player.colliderect(i[0]):
                        life_counter -= 1
                        player_x = 100
                        player_y = 880
                for i in shells:
                    if i[0].x > 2000 or i[0].x < -50:
                        shells.remove(i)



        #HIT_BOX
            if afk_side:
                hit_box_player = pygame.Rect(player_x, player_y, 45, 83)
            else:
                hit_box_player = pygame.Rect((player_x + 15), player_y, 45, 83)

            ground_rect_1 = pygame.Rect(0, 950, 1920, 22)
            ground_rect_2 = pygame.Rect(1838, 800, 88, 22)
            ground_rect_3 = pygame.Rect(0, 655, 1700, 22)
            ground_rect_4 = pygame.Rect(0, 505, 75, 22)
            ground_rect_5 = pygame.Rect(187, 360, 1920, 22)
            ground_rect_3_side = pygame.Rect(1695, 660, 10, 43)
            ground_rect_4_side = pygame.Rect(70, 510, 10, 43)
            ground_rect_5_side = pygame.Rect(182, 365, 10, 43)
            ground_rect_2_side = pygame.Rect(1832, 805, 10, 43)
            ground_rect_2_down = pygame.Rect(1837, 827, 88, 22)
            ground_rect_3_down = pygame.Rect(0, 682, 1700, 22)
            ground_rect_4_down = pygame.Rect(0, 532, 75, 22)
            ground_rect_5_down = pygame.Rect(187, 387, 1920, 22)

            door_rect = pygame.Rect(1854, 289, 54, 81)
            spike_rect = pygame.Rect(525, 923, 28, 41)
            spike_rect2 = pygame.Rect(1200, 923, 28, 41)
            spike_rect3 = pygame.Rect(1100, 626, 28, 41)
            spike_rect4 = pygame.Rect(766, 330, 28, 41)
            spike_rect5 = pygame.Rect(1458, 330, 28, 41)



            hit_box_vision_right = pygame.Rect(600, 480, 1000, 183)
            hit_box_vision_left = pygame.Rect(600, 480, -1000, 183)



            if hit_box_player.colliderect(spike_rect):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect2):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect3):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect4):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect5):
                life_counter -= 1
                player_x = 100
                player_y = 880








            A = [
                hit_box_player.colliderect(ground_rect_1),
                hit_box_player.colliderect(ground_rect_2),
                hit_box_player.colliderect(ground_rect_3),
                hit_box_player.colliderect(ground_rect_4),
                hit_box_player.colliderect(ground_rect_5),
            ]

            if True in A:
                gravity = False
            else:
                gravity = True


            keys = pygame.key.get_pressed()


        #player_movement

            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_count], (player_x, player_y))
                afk_side = False
            elif keys[pygame.K_RIGHT]:
                screen.blit(walk_right[player_count], (player_x, player_y))
                afk_side = True
            else:
                if afk_side:
                    screen.blit(afk_player_right, (player_x, player_y))
                else:
                    screen.blit(afk_player_left, (player_x, player_y))

            if hit_box_player.colliderect(ground_rect_2_down) or hit_box_player.colliderect(ground_rect_3_down) or hit_box_player.colliderect(ground_rect_4_down) or hit_box_player.colliderect(ground_rect_5_down):
                is_jump = False
                jump_count = 22



        #player_jump

            if not is_jump:
                if not gravity:
                    if keys[pygame.K_SPACE]:
                        is_jump = True
            else:
                if jump_count >= 0:
                    player_y -= (jump_count ** 1.1) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 22

            if gravity == True and is_jump == False:
                player_y += (gravity_count ** 1.3) / 3
                gravity_count += 0.3
            else:
                gravity_count = 1



        #the_images_of_the_player's_movement_change

            if player_count == 47:
                player_count = 0
            else:
                player_count += 1


        #player_movement

            if keys[pygame.K_LEFT] and player_x > 0 and not hit_box_player.colliderect(ground_rect_3_side) and not hit_box_player.colliderect(ground_rect_4_side):
                player_x -= speed_player
            elif keys[pygame.K_RIGHT] and player_x < 1870 and not hit_box_player.colliderect(ground_rect_2_side) and not hit_box_player.colliderect(ground_rect_5_side):
                player_x += speed_player


            if hit_box_player.colliderect(hit_box_vision_right):
                direction_of_the_enemy2 = True
                direction_of_the_enemy2_left = False
                shooting_enemy_count += 1
                if shooting_enemy_count == 120:
                    shooting_enemy_count = 0
            elif hit_box_player.colliderect(hit_box_vision_left):
                direction_of_the_enemy2_left = True
                direction_of_the_enemy2 = False
                shooting_enemy_count_1 += 1
                if shooting_enemy_count_1 == 120:
                    shooting_enemy_count_1 = 0
            else:
                direction_of_the_enemy2 = False
                direction_of_the_enemy2_left = False
                agr = False
                shooting_enemy_count = 0
                shooting_enemy_count_1 = 0


            if direction_of_the_enemy2 and agr:
                screen.blit(shooting_enemy2[shooting_enemy_count], (600, 580))
            elif direction_of_the_enemy2_left:
                screen.blit(shooting_enemy2_left[shooting_enemy_count_1], (600, 580))
            else:
                screen.blit(afk_enemy2_left, (600, 580))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                    pygame.quit()

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right) and agr:
                    arrow = arrow_right
                    shells.append([arrow.get_rect(topleft=(640, 620)), 1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right):
                    agr = True

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left):
                    arrow = arrow_left
                    shells.append([arrow.get_rect(topleft=(640, 620)), -1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left):
                    agr = True

                if hit_box_player.colliderect(door_rect):
                    lvl1 = False
                    lvl2 = True
                    player_x = 100
                    player_y = 880
                    life_counter = 3









        if life_counter and lvl2:
            screen.blit(bg2, (0, 0))
            for i in range(6):
                screen.blit(stone, (330 * i, 950))
            screen.blit(stone, (1832, 800))
            for i in range(6):
                screen.blit(stone, (275 * i, 655))
            screen.blit(stone, (-250, 505))
            for i in range(6):
                screen.blit(stone, (182 + 330 * i, 360))
            for i in range(life_counter):
                screen.blit(heart, (50 + (i * 100), 100))
            screen.blit(door, (1854, 289))
            screen.blit(spikes, (813, 936))
            screen.blit(spikes, (930, 636))
            screen.blit(spikes, (1410, 341))

        #add_enemies




            if shells:
                for i in shells:
                    screen.blit(arrow, i[0])
                    if i[1] == 1:
                        i[0].x += 5
                    else:
                        i[0].x -= 5
                    if hit_box_player.colliderect(i[0]):
                        life_counter -= 1
                        player_x = 100
                        player_y = 880
                for i in shells:
                    if i[0].x > 2000 or i[0].x < -50:
                        shells.remove(i)



        #HIT_BOX
            if afk_side:
                hit_box_player = pygame.Rect(player_x, player_y, 45, 83)
            else:
                hit_box_player = pygame.Rect((player_x + 15), player_y, 45, 83)

            stone_rect_1 = pygame.Rect(0, 950, 1920, 22)
            stone_rect_2 = pygame.Rect(1838, 800, 88, 22)
            stone_rect_3 = pygame.Rect(0, 655, 1700, 22)
            stone_rect_4 = pygame.Rect(0, 505, 75, 22)
            stone_rect_5 = pygame.Rect(187, 360, 1920, 22)
            stone_rect_3_side = pygame.Rect(1695, 660, 10, 43)
            stone_rect_4_side = pygame.Rect(70, 510, 10, 43)
            stone_rect_5_side = pygame.Rect(182, 365, 10, 43)
            stone_rect_2_side = pygame.Rect(1832, 805, 10, 43)
            stone_rect_2_down = pygame.Rect(1837, 827, 88, 22)
            stone_rect_3_down = pygame.Rect(0, 682, 1700, 22)
            stone_rect_4_down = pygame.Rect(0, 532, 75, 22)
            stone_rect_5_down = pygame.Rect(187, 387, 1920, 22)

            door_rect2 = pygame.Rect(1854, 289, 54, 81)
            spikes_rect = pygame.Rect(813, 936, 145, 29)
            spikes_rect2 = pygame.Rect(930, 636, 145, 29)
            spikes_rect3 = pygame.Rect(1410, 341, 145, 29)



            hit_box_vision_right = pygame.Rect(600, 480, 1000, 183)
            hit_box_vision_left = pygame.Rect(600, 480, -1000, 183)
            hit_box_vision_right1 = pygame.Rect(1000, 180, 1000, 183)
            hit_box_vision_left1 = pygame.Rect(1000, 180, -1000, 183)



            if hit_box_player.colliderect(spikes_rect):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spikes_rect2):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spikes_rect3):
                life_counter -= 1
                player_x = 100
                player_y = 880



            A = [
                hit_box_player.colliderect(stone_rect_1),
                hit_box_player.colliderect(stone_rect_2),
                hit_box_player.colliderect(stone_rect_3),
                hit_box_player.colliderect(stone_rect_4),
                hit_box_player.colliderect(stone_rect_5),
            ]

            if True in A:
                gravity = False
            else:
                gravity = True


            keys = pygame.key.get_pressed()


        #player_movement

            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_count], (player_x, player_y))
                afk_side = False
            elif keys[pygame.K_RIGHT]:
                screen.blit(walk_right[player_count], (player_x, player_y))
                afk_side = True
            else:
                if afk_side:
                    screen.blit(afk_player_right, (player_x, player_y))
                else:
                    screen.blit(afk_player_left, (player_x, player_y))

            if hit_box_player.colliderect(stone_rect_2_down) or hit_box_player.colliderect(stone_rect_3_down) or hit_box_player.colliderect(stone_rect_4_down) or hit_box_player.colliderect(stone_rect_5_down):
                is_jump = False
                jump_count = 22



        #player_jump

            if not is_jump:
                if not gravity:
                    if keys[pygame.K_SPACE]:
                        is_jump = True
            else:
                if jump_count >= 0:
                    player_y -= (jump_count ** 1.1) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 22




            if gravity == True and is_jump == False:
                player_y += (gravity_count ** 1.3) / 3
                gravity_count += 0.3
            else:
                gravity_count = 1



        #the_images_of_the_player's_movement_change

            if player_count == 47:
                player_count = 0
            else:
                player_count += 1


        #player_movement

            if keys[pygame.K_LEFT] and player_x > 0 and not hit_box_player.colliderect(stone_rect_3_side) and not hit_box_player.colliderect(stone_rect_4_side):
                player_x -= speed_player
            elif keys[pygame.K_RIGHT] and player_x < 1870 and not hit_box_player.colliderect(stone_rect_2_side) and not hit_box_player.colliderect(stone_rect_5_side):
                player_x += speed_player

            # enemy

            if hit_box_player.colliderect(hit_box_vision_right):
                direction_of_the_enemy2 = True
                direction_of_the_enemy2_left = False
                shooting_enemy_count += 1
                if shooting_enemy_count == 120:
                    shooting_enemy_count = 0
            elif hit_box_player.colliderect(hit_box_vision_left):
                direction_of_the_enemy2_left = True
                direction_of_the_enemy2 = False
                shooting_enemy_count_1 += 1
                if shooting_enemy_count_1 == 120:
                    shooting_enemy_count_1 = 0
            else:
                direction_of_the_enemy2 = False
                direction_of_the_enemy2_left = False
                agr = False
                shooting_enemy_count = 0
                shooting_enemy_count_1 = 0




            if direction_of_the_enemy2 and agr:
                screen.blit(shooting_enemy2[shooting_enemy_count], (600, 580))
            elif direction_of_the_enemy2_left:
                screen.blit(shooting_enemy2_left[shooting_enemy_count_1], (600, 580))
            else:
                screen.blit(afk_enemy2_left, (600, 580))

            # enemy1!!!!!!!!!!!!!



            if hit_box_player.colliderect(hit_box_vision_right1):
                direction_of_the_enemy3 = True
                direction_of_the_enemy3_left = False
                shooting_enemy_count1 += 1
                if shooting_enemy_count1 == 120:
                    shooting_enemy_count1 = 0
            elif hit_box_player.colliderect(hit_box_vision_left1):
                direction_of_the_enemy3_left = True
                direction_of_the_enemy3 = False
                shooting_enemy_count_2 += 1
                if shooting_enemy_count_2 == 120:
                    shooting_enemy_count_2 = 0
            else:
                direction_of_the_enemy3 = False
                direction_of_the_enemy3_left = False
                agr1 = False
                shooting_enemy_count1 = 0
                shooting_enemy_count_2 = 0

            if direction_of_the_enemy3 and agr1:
                screen.blit(shooting_enemy2[shooting_enemy_count1], (1000, 280))
            elif direction_of_the_enemy3_left:
                screen.blit(shooting_enemy2_left[shooting_enemy_count_2], (1000, 280))
            else:
                screen.blit(afk_enemy2_left, (1000, 280))
            #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                    pygame.quit()

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right) and agr:
                    arrow = arrow_right
                    shells.append([arrow.get_rect(topleft=(640, 620)), 1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right):
                    agr = True

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left):
                    arrow = arrow_left
                    shells.append([arrow.get_rect(topleft=(640, 620)), -1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left):
                    agr = True
                #!!!!!!!!!!!!!!!!!!!!!!!!
                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right1) and agr1:
                    arrow = arrow_right
                    shells.append([arrow.get_rect(topleft=(1040, 320)), 1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right1):
                    agr1 = True

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left1):
                    arrow = arrow_left
                    shells.append([arrow.get_rect(topleft=(1040, 320)), -1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left1):
                    agr1 = True
                #!!!!!!!!!!!!!!!!!!!!!!!
                if hit_box_player.colliderect(door_rect2):
                    lvl2 = False
                    lvl3 = True
                    player_x = 100
                    player_y = 880
                    life_counter = 3







        if life_counter and lvl3:
            screen.blit(bg3, (0, 0))
            for i in range(6):
                screen.blit(dark_stone, (330 * i, 950))
            screen.blit(dark_stone, (1832, 800))
            for i in range(6):
                screen.blit(dark_stone, (275 * i, 655))
            screen.blit(dark_stone, (-250, 505))
            for i in range(6):
                screen.blit(dark_stone, (182 + 330 * i, 360))
            for i in range(life_counter):
                screen.blit(heart, (50 + (i * 100), 100))
            screen.blit(door, (1854, 289))
            screen.blit(spike, (525, 923))
            screen.blit(spike, (1200, 923))
            screen.blit(spike, (1100, 626))
            screen.blit(spike, (766, 330))
            screen.blit(spike, (1458, 330))

        #add_enemies




            if shells:
                for i in shells:
                    screen.blit(arrow, i[0])
                    if i[1] == 1:
                        i[0].x += 5
                    else:
                        i[0].x -= 5
                    if hit_box_player.colliderect(i[0]):
                        life_counter -= 1
                        player_x = 100
                        player_y = 880
                for i in shells:
                    if i[0].x > 2000 or i[0].x < -50:
                        shells.remove(i)



        #HIT_BOX
            if afk_side:
                hit_box_player = pygame.Rect(player_x, player_y, 45, 83)
            else:
                hit_box_player = pygame.Rect((player_x + 15), player_y, 45, 83)

            dark_stone_rect_1 = pygame.Rect(0, 950, 1920, 22)
            dark_stone_rect_2 = pygame.Rect(1838, 800, 88, 22)
            dark_stone_rect_3 = pygame.Rect(0, 655, 1700, 22)
            dark_stone_rect_4 = pygame.Rect(0, 505, 75, 22)
            dark_stone_rect_5 = pygame.Rect(187, 360, 1920, 22)
            dark_stone_rect_3_side = pygame.Rect(1695, 660, 10, 43)
            dark_stone_rect_4_side = pygame.Rect(70, 510, 10, 43)
            dark_stone_rect_5_side = pygame.Rect(182, 365, 10, 43)
            dark_stone_rect_2_side = pygame.Rect(1832, 805, 10, 43)
            dark_stone_rect_2_down = pygame.Rect(1837, 827, 88, 22)
            dark_stone_rect_3_down = pygame.Rect(0, 682, 1700, 22)
            dark_stone_rect_4_down = pygame.Rect(0, 532, 75, 22)
            dark_stone_rect_5_down = pygame.Rect(187, 387, 1920, 22)

            door_rect3 = pygame.Rect(1854, 289, 54, 81)
            spike_rect = pygame.Rect(525, 923, 28, 41)
            spike_rect2 = pygame.Rect(1200, 923, 28, 41)
            spike_rect3 = pygame.Rect(1100, 626, 28, 41)
            spike_rect4 = pygame.Rect(766, 330, 28, 41)
            spike_rect5 = pygame.Rect(1458, 330, 28, 41)

            hit_box_vision_right = pygame.Rect(600, 480, 1000, 183)
            hit_box_vision_left = pygame.Rect(600, 480, -1000, 183)
            hit_box_vision_right1 = pygame.Rect(1000, 180, 1000, 183)
            hit_box_vision_left1 = pygame.Rect(1000, 180, -1000, 183)
            hit_box_vision_right2 = pygame.Rect(1350, 780, 1000, 183)
            hit_box_vision_left2 = pygame.Rect(1350, 780, -1000, 183)



            if hit_box_player.colliderect(spike_rect):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect2):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect3):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect4):
                life_counter -= 1
                player_x = 100
                player_y = 880
            if hit_box_player.colliderect(spike_rect5):
                life_counter -= 1
                player_x = 100
                player_y = 880








            A = [
                hit_box_player.colliderect(dark_stone_rect_1),
                hit_box_player.colliderect(dark_stone_rect_2),
                hit_box_player.colliderect(dark_stone_rect_3),
                hit_box_player.colliderect(dark_stone_rect_4),
                hit_box_player.colliderect(dark_stone_rect_5),
            ]

            if True in A:
                gravity = False
            else:
                gravity = True


            keys = pygame.key.get_pressed()


        #player_movement

            if keys[pygame.K_LEFT]:
                screen.blit(walk_left[player_count], (player_x, player_y))
                afk_side = False
            elif keys[pygame.K_RIGHT]:
                screen.blit(walk_right[player_count], (player_x, player_y))
                afk_side = True
            else:
                if afk_side:
                    screen.blit(afk_player_right, (player_x, player_y))
                else:
                    screen.blit(afk_player_left, (player_x, player_y))

            if hit_box_player.colliderect(dark_stone_rect_2_down) or hit_box_player.colliderect(dark_stone_rect_3_down) or hit_box_player.colliderect(dark_stone_rect_4_down) or hit_box_player.colliderect(dark_stone_rect_5_down):
                is_jump = False
                jump_count = 22



        #player_jump

            if not is_jump:
                if not gravity:
                    if keys[pygame.K_SPACE]:
                        is_jump = True
            else:
                if jump_count >= 0:
                    player_y -= (jump_count ** 1.1) / 2
                    jump_count -= 1
                else:
                    is_jump = False
                    jump_count = 22




            if gravity == True and is_jump == False:
                player_y += (gravity_count ** 1.3) / 3
                gravity_count += 0.3
            else:
                gravity_count = 1



        #the_images_of_the_player's_movement_change

            if player_count == 47:
                player_count = 0
            else:
                player_count += 1


        #player_movement

            if keys[pygame.K_LEFT] and player_x > 0 and not hit_box_player.colliderect(dark_stone_rect_3_side) and not hit_box_player.colliderect(dark_stone_rect_4_side):
                player_x -= speed_player
            elif keys[pygame.K_RIGHT] and player_x < 1870 and not hit_box_player.colliderect(dark_stone_rect_2_side) and not hit_box_player.colliderect(dark_stone_rect_5_side):
                player_x += speed_player

            # enemy

            if hit_box_player.colliderect(hit_box_vision_right):
                direction_of_the_enemy2 = True
                direction_of_the_enemy2_left = False
                shooting_enemy_count += 1
                if shooting_enemy_count == 120:
                    shooting_enemy_count = 0
            elif hit_box_player.colliderect(hit_box_vision_left):
                direction_of_the_enemy2_left = True
                direction_of_the_enemy2 = False
                shooting_enemy_count_1 += 1
                if shooting_enemy_count_1 == 120:
                    shooting_enemy_count_1 = 0
            else:
                direction_of_the_enemy2 = False
                direction_of_the_enemy2_left = False
                agr = False
                shooting_enemy_count = 0
                shooting_enemy_count_1 = 0

            if direction_of_the_enemy2 and agr:
                screen.blit(shooting_enemy2[shooting_enemy_count], (600, 580))
            elif direction_of_the_enemy2_left:
                screen.blit(shooting_enemy2_left[shooting_enemy_count_1], (600, 580))
            else:
                screen.blit(afk_enemy2_left, (600, 580))

            # enemy1!!!!!!!!!!!!!

            if hit_box_player.colliderect(hit_box_vision_right1):
                direction_of_the_enemy3 = True
                direction_of_the_enemy3_left = False
                shooting_enemy_count1 += 1
                if shooting_enemy_count1 == 120:
                    shooting_enemy_count1 = 0
            elif hit_box_player.colliderect(hit_box_vision_left1):
                direction_of_the_enemy3_left = True
                direction_of_the_enemy3 = False
                shooting_enemy_count_2 += 1
                if shooting_enemy_count_2 == 120:
                    shooting_enemy_count_2 = 0
            else:
                direction_of_the_enemy3 = False
                direction_of_the_enemy3_left = False
                agr1 = False
                shooting_enemy_count1 = 0
                shooting_enemy_count_2 = 0

            if direction_of_the_enemy3 and agr1:
                screen.blit(shooting_enemy2[shooting_enemy_count1], (1000, 280))
            elif direction_of_the_enemy3_left:
                screen.blit(shooting_enemy2_left[shooting_enemy_count_2], (1000, 280))
            else:
                screen.blit(afk_enemy2_left, (1000, 280))
            # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

            if hit_box_player.colliderect(hit_box_vision_right2):
                direction_of_the_enemy4 = True
                direction_of_the_enemy4_left = False
                shooting_enemy_count2 += 1
                if shooting_enemy_count2 == 120:
                    shooting_enemy_count2 = 0
            elif hit_box_player.colliderect(hit_box_vision_left2):
                direction_of_the_enemy4_left = True
                direction_of_the_enemy4 = False
                shooting_enemy_count_3 += 1
                if shooting_enemy_count_3 == 120:
                    shooting_enemy_count_3 = 0
            else:
                direction_of_the_enemy4 = False
                direction_of_the_enemy4_left = False
                agr2 = False
                shooting_enemy_count2 = 0
                shooting_enemy_count_3 = 0

            if direction_of_the_enemy4 and agr2:
                screen.blit(shooting_enemy2[shooting_enemy_count2], (1350, 880))
            elif direction_of_the_enemy4_left:
                screen.blit(shooting_enemy2_left[shooting_enemy_count_3], (1350, 880))
            else:
                screen.blit(afk_enemy2_left, (1350, 880))
            #&&&&&&&&&&&&&&&&&&

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Run = False
                    pygame.quit()

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right) and agr:
                    arrow = arrow_right
                    shells.append([arrow.get_rect(topleft=(640, 620)), 1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right):
                    agr = True

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left):
                    arrow = arrow_left
                    shells.append([arrow.get_rect(topleft=(640, 620)), -1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left):
                    agr = True
                # !!!!!!!!!!!!!!!!!!!!!!!!
                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right1) and agr1:
                    arrow = arrow_right
                    shells.append([arrow.get_rect(topleft=(1040, 320)), 1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right1):
                    agr1 = True

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left1):
                    arrow = arrow_left
                    shells.append([arrow.get_rect(topleft=(1040, 320)), -1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left1):
                    agr1 = True


                #$$$$$$$

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right2) and agr2:
                    arrow = arrow_right
                    shells.append([arrow.get_rect(topleft=(1390, 920)), 1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_right2):
                    agr2 = True

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left2):
                    arrow = arrow_left
                    shells.append([arrow.get_rect(topleft=(1390, 920)), -1])

                if event.type == timer_enemy2 and hit_box_player.colliderect(hit_box_vision_left2):
                    agr2 = True

                if hit_box_player.colliderect(door_rect3):
                    lvl3 = False
                    bg1_sound.set_volume(0)
                    bg2_sound.set_volume(0)
                    bg3_sound.set_volume(0)
                    screen.fill((1, 1, 1))
                    screen.blit(win_label, (400, 489))

    else:
        bg1_sound.set_volume(0)
        bg2_sound.set_volume(0)
        bg3_sound.set_volume(0)
        screen.fill((1, 1, 1))
        screen.blit(lose_label, (750, 400))
        screen.blit(restart_label, restart_label_rect)

        shells.clear()

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            lvl1 = True
            lvl2 = False
            lvl3 = False
            player_x = 100
            player_y = 800
            life_counter = 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                pygame.quit()


    clock.tick(60)