from pygame import *
import random
import time as tm
init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

playing = False

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self): 
        if ball.rect.x <= screen_width-80 and ball.x_speed > 0 or ball.rect.x >= 0 and ball.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if ball.rect.y <= screen_height-80 and ball.y_speed > 0 or ball.rect.y >= 0 and ball.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0

                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.y_speed = 0
                self.rect.top = max(self.rect.top, p.rect.bottom)



class WoodPlank(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

random_num = random.randint(1,5)

my_font = font.SysFont(None, 69)
price_font = font.SysFont(None, 35)
text_surface = my_font.render('Main Menu', False, (0, 0, 0))



data = []

wood_count = 0
play = GameSprite('play.png',225,170,225,100)
shop = GameSprite('shop.png',225,300,225,100)
main_menu = GameSprite('main_menu.png',215,400,225,100)
screen_width = 700
screen_height = 500

file = open('points.txt','r')
points_file = file.readlines()
for line in points_file:
    data.append(line.strip())
points = data[0]
points = int(points)
gold_ball1 = data[1]
gold_ball1 = int(gold_ball1)
gold_ball = bool(gold_ball1)
print(gold_ball)
speed_amount = data[2]
speed_amount = int(speed_amount)
block_p = data[3]
block_p = int(block_p)


        
display.set_caption("maze")
screen = display.set_mode((screen_width, screen_height))
back = (119, 210, 223)
bg = transform.scale(image.load("bg.jpg"), (screen_width, screen_height))
barriers = sprite.Group()
woods = sprite.Group()
holes = sprite.Group()
w1 = GameSprite('wall.png',0,100, 125, 20)
w = GameSprite('wall.png',50,200,75,20)
w2 = GameSprite('wall_w.png', 125, 100, 20, 120)
w3 = GameSprite('wall_w.png',200,0,20,125)
w4 = GameSprite('wall_w.png',200,215,20,105)
w5 = GameSprite('wall.png',200,107,150,20)
w6 = GameSprite('wall_w.png',330,78,20,50)
w7 = GameSprite('wall.png',350,78,65,20)
w8 = GameSprite('wall_w.png',400,78,20,50)
w9 = GameSprite('wall.png',400,108,150,20)
w10 = GameSprite('wall_w.png',440,110,20,100)
w11 = GameSprite('wall.png',200,210,75,20)
w12 = GameSprite('wall.png',100,300,100,20)
w13 = GameSprite('wall_w.png',100,300,20,75)
w14 = GameSprite('wall.png',100,375,75,20)
w15 = GameSprite('wall_w.png',155,393,20,30)
w16 = GameSprite('wall.png',155,405,150,20)
w17 = GameSprite('wall_w.png',305,325,20,100)
w18 = GameSprite('wall_w.png',260,210,20,100)
w19 = GameSprite('wall.png',260,310,225,20)
w20 = GameSprite('wall_w.png',415,310,20,100)
w21 = GameSprite('wall_w.png',555,310,20,100)
w22 = GameSprite('wall.png',515,405,60,20)
barriers.add(w1)
barriers.add(w2)
barriers.add(w)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)
barriers.add(w21)
barriers.add(w22)
if not gold_ball:
    ball = Player('ball.png', 5, 0, 50, 50, 0, 0)
if gold_ball:
    ball = Player('gold_ball.png',5,0,50,50,0,0)
balls = sprite.Group()
balls.add(ball)
bought_gold_ball = GameSprite('bought_gold_ball.png',525,60,150,150)
hole = GameSprite('hole.png', 200, 150, 50, 50)
hole1 = GameSprite('hole.png',150,435,50,50)
hole2 = GameSprite('hole.png',275,435,50,50)
hole3 = GameSprite('hole.png',400,435,50,50)
hole4 = GameSprite('hole.png',550,435,50,50)
hole5 = GameSprite('hole.png',575,350,75,75)
hole6 = GameSprite('hole.png',625,325,75,75)
wood = WoodPlank('wood.png',60,132,50,50)
wood1 = WoodPlank('wood.png',240,30,50,50)
wood3 = WoodPlank('wood.png',475,135,50,50)
wood2 = WoodPlank('wood.png',345,355,50,50)
wood4 = WoodPlank('wood.png',215,435,50,50)
woods.add(wood)
woods.add(wood1)
woods.add(wood2)
woods.add(wood3)
woods.add(wood4)
holes.add(hole)
holes.add(hole1)
holes.add(hole2)
holes.add(hole3)
holes.add(hole4)
holes.add(hole5)
holes.add(hole6)
file = open('points.txt','w')
speed = GameSprite('speed.png',50,100,100,100)
balls = sprite.Group()
balls.add(ball)
gold_ball_img = GameSprite('gold_ball.png',525,60,150,150)
wood_p_1 = GameSprite('wood_p_1.png',300,100,100,100)
final_sprite = GameSprite('kegla.png', screen_width - 85, screen_height - 100, 80, 80)
finish = False
run = True
Shop = False
counter = False
x = 0
y = 0
while run:
    for e in event.get():
        
        if e.type == QUIT:
            run = False
        if gold_ball:
            if e.type == KEYDOWN:
                if e.key == K_LEFT:
                    ball.x_speed = -8
                elif e.key == K_RIGHT:
                    ball.x_speed = 8
                elif e.key == K_UP :
                    ball.y_speed = -8
                elif e.key == K_DOWN :
                    ball.y_speed = 8
                elif e.key == K_s and speed_amount > 0:
                        counter = True
                        y = 0
                        speed_amount -= 1
                if y <= 150 and counter:
                    ball.x_speed *= 2
                    ball.y_speed *= 2
                elif y > 150:
                        counter = False
                        y = 0
                if e.key == K_w and block_p > 0:
                    wood_count += 1
                    block_p -= 1
            elif e.type == KEYUP:
                if e.key == K_LEFT :
                    ball.x_speed = 0
                elif e.key == K_RIGHT:
                    ball.x_speed = 0
                elif e.key == K_UP:
                    ball.y_speed = 0
                elif e.key == K_DOWN:
                    ball.y_speed = 0
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                ball.x_speed = -5
            elif e.key == K_RIGHT:
                ball.x_speed = 5
            elif e.key == K_UP :
                ball.y_speed = -5
            elif e.key == K_DOWN :
                ball.y_speed = 5
            elif e.key == K_s and speed_amount > 0:
                counter = True
            if y <= 150 and counter:
                ball.x_speed *= 2
                ball.y_speed *= 2
            elif y > 150:
                    counter = False
                    y = 0
            elif e.key == K_w and block_p > 0:
                wood_count += 1
                block_p -= 1
        elif e.type == KEYUP:
            if e.key == K_LEFT :
                ball.x_speed = 0
            elif e.key == K_RIGHT:
                ball.x_speed = 0
            elif e.key == K_UP:
                ball.y_speed = 0
            elif e.key == K_DOWN:
                ball.y_speed = 0
        
        if mouse.get_pressed()[0] and play.rect.collidepoint(mouse.get_pos()):
            playing = True
            tim_e = tm.time()
        if mouse.get_pressed()[0] and speed.rect.collidepoint(mouse.get_pos()) and points >= 50:
            speed_amount += 1
            points -= 50
        if mouse.get_pressed()[0] and wood_p_1.rect.collidepoint(mouse.get_pos()) and points >= 50:
            block_p += 1
            points -= 50
        if mouse.get_pressed()[0] and gold_ball_img.rect.collidepoint(mouse.get_pos()) and not gold_ball and points >= 500:
            gold_ball = 1
            points -= 500
            bought_gold_ball.reset()
        if mouse.get_pressed()[0] and main_menu.rect.collidepoint(mouse.get_pos()) and (finish == True or Shop == True):
            Shop = False
            playing = False
            finish = False
            if not gold_ball:
                ball = Player('ball.png', 5, 0, 50, 50, 0, 0)
            if gold_ball:
                ball = Player('gold_ball.png',5,0,50,50,0,0)
            balls = sprite.Group()
            balls.add(ball)
            
            hole = GameSprite('hole.png', 200, 150, 50, 50)
            hole1 = GameSprite('hole.png',150,435,50,50)
            hole2 = GameSprite('hole.png',275,435,50,50)
            hole3 = GameSprite('hole.png',400,435,50,50)
            hole4 = GameSprite('hole.png',550,435,50,50)
            hole5 = GameSprite('hole.png',575,350,75,75)
            hole6 = GameSprite('hole.png',625,325,75,75)
            wood = WoodPlank('wood.png',60,132,50,50)
            wood1 = WoodPlank('wood.png',240,30,50,50)
            wood3 = WoodPlank('wood.png',475,135,50,50)
            wood2 = WoodPlank('wood.png',345,355,50,50)
            wood4 = WoodPlank('wood.png',215,435,50,50)
            woods.add(wood)
            woods.add(wood1)
            woods.add(wood2)
            woods.add(wood3)
            woods.add(wood4)
            holes.add(hole)
            holes.add(hole1)
            holes.add(hole2)
            holes.add(hole3)
            holes.add(hole4)
            holes.add(hole5)
            holes.add(hole6)
        if mouse.get_pressed()[0] and shop.rect.collidepoint(mouse.get_pos()) and Shop == False:
            Shop = True
    


    if playing:
        if not finish:
            screen.blit(bg,(0,0))
            woods.draw(screen)
            barriers.draw(screen)
            holes.draw(screen)
            final_sprite.reset()
            ball.reset()
            ball.update()
            speed_am = price_font.render(f'speed amount: {speed_amount}',False,(255,255,255))
            block_am = price_font.render(f'blocks amount: {block_p}',False,(255,255,255))
            screen.blit(speed_am,(200,25))
            screen.blit(block_am,(450,25))
            if sprite.groupcollide(balls,woods,False,True):
                wood_count += 1
            elif sprite.collide_rect(ball, final_sprite):
                finish = True
                points += 50 - int(tm.time() - tim_e)
                points_txt = my_font.render(f'You got:{50 - int((tm.time() - tim_e))} points',False,(0,0,0))
                screen.blit(points_txt,(150,100))
                main_menu.reset()
            elif sprite.spritecollide(ball, holes, False):
                if wood_count == 0 and finish == False:
                    finish = True
                    points += random_num
                    random_num = random.randint(1,5)
                    points_txt = my_font.render(f'You got:{random_num} points',False,(0,0,0))
                    screen.blit(points_txt,(150,100))
                    main_menu.reset()
                elif wood_count > 0:
                    sprite.groupcollide(balls,holes,False,True)
                    wood_count -= 1
    if not playing:
        screen.fill((255,255,255))
        screen.blit(text_surface, (225,50))
        play.reset()
        shop.reset()
    if Shop:
        screen.fill((255,255,255))
        speed.reset()
        main_menu.reset()
        points1 = price_font.render('BUY: 50 POINTS',False,(0,0,0))
        points2 = price_font.render('BUY: 500 POINTS',False,(0,0,0))
        you_have = price_font.render(f"YOU HAVE: {points}",False,(0,0,0))
        screen.blit(points1,(25,210))
        wood_p_1.reset()
        screen.blit(points1,(260,210))
        if not gold_ball:
            gold_ball_img.reset()
        elif gold_ball:
            bought_gold_ball.reset()
        screen.blit(points2,(485,210))
        screen.blit(you_have,(225,350))
    if x % 25 == 0:
        if gold_ball:
            gold_ball = 1
        else:
            gold_ball = 0
        file = open('points.txt', 'r+')
        file.truncate(0)
        file = open('points.txt','w')
        file.write(str(points)+ "\n")
        file.write(str(gold_ball)+ "\n")
        file.write(str(speed_amount)+ "\n")
        file.write(str(block_p)+ "\n")
    if counter:
        y += 1
    x += 1
    time.delay(50)
    display.update()