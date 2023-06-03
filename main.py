import pygame
from random import randint as ri
time=pygame.time.Clock()
# pygame.display.set_icon(icon)
pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('Хорошая игра')
hero=pygame.image.load(r"C:\Users\hrach\PycharmProjects\Game\img\1.png")
walk_left=[
    pygame.image.load('img/left/1 (1).png'),
    pygame.image.load('img/left/2.png'),
    pygame.image.load('img/left/3.png'),
    pygame.image.load('img/left/4.png')
]
walk_right=[
    pygame.image.load('img/right/1 (2).png'),
    pygame.image.load('img/right/2 (1).png'),
    pygame.image.load('img/right/3 (1).png'),
    pygame.image.load('img/right/4 (1).png')
]


bg=pygame.image.load(r"C:\Users\hrach\PycharmProjects\Game\img\bg.jpg")
bg_x=0
bg_sound=pygame.mixer.Sound('music/Fon.mp3')
bg_sound.play()
is_jump=False
player_x=100
player_y=245
player_anim_count=0
zombi_anim_count=0
player_speed=10
jump_count=10
zombi_lis=[]
zombi_rect_x=810
zombi_speed=4
runn=True
while runn:


    screen.blit(bg,(bg_x,0))
    screen.blit(bg, (bg_x +800, 0))
    screen.blit(bg, (bg_x-800, 0))
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and player_x>50:
        screen.blit(walk_left[player_anim_count],(player_x,player_y))
        player_x-=player_speed
        bg_x+=player_speed-2
        if bg_x==800:
            bg_x=0

    elif keys[pygame.K_d] and player_x <720:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
        player_x += player_speed
        bg_x -= player_speed - 2
        if bg_x == -800:
            bg_x = 0

    else:
        screen.blit(hero,(player_x,player_y))


    if not is_jump:
        if keys[pygame.K_w]:
            is_jump=True
    else:
        if jump_count>=-10:
            if jump_count>0:
                player_y-=(jump_count**2)/3
            else:
                player_y += (jump_count ** 2) / 3
            jump_count-=2
        else:
            is_jump=False
            jump_count=10

    if player_anim_count==3:
        player_anim_count=0
    else:
        player_anim_count+=1

    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            runn=False
            pygame.quit()

    time.tick(20)
