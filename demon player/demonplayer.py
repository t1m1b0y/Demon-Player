#demonplayer
import pygame
import random

pygame.init()

#setting the window settings
pygame.display.set_caption(('hinokami chronicles'))
win = pygame.display.set_mode((736, 396))



#getting the animations
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('tanji.png')
splash = pygame.image.load('splash.png')
splash2 = pygame.image.load('splash2.png')

tanjiroright = [pygame.image.load('tanjiro1.png'), pygame.image.load('tanjiro2.png')]
tanjiroleft = [pygame.image.load('tanjiro3.png'), pygame.image.load('tanjiro4.png')]
tanjiro = pygame.image.load('tanji.png')
tanjirol = pygame.image.load('tanji2.png')
slash = pygame.image.load('slash.png')
hinok = pygame.image.load('hino.png')
hinoka = pygame.image.load('hinoka.png')
dmbg = pygame.image.load('dmnslyr.jpg')
dmbg2 = pygame.image.load('bg2.jpg')
menuu = pygame.image.load('menu.jpg')
        
#idk
clock = pygame.time.Clock()

score = 0

bg1 = True
bg2 = False

music = pygame.mixer.music.load('demonlofi.mp3')
pygame.mixer.music.play(-1)



#making everything cleaner
class player():
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health

        self.vel = 10
        self.right = False
        self.left = False
        self.walkcount = 0
        self.jumpcount = 10
        self.jump = False
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60 )
        self.hinoright = False
        self.hinoleft = False
        self.sprite_right = []
        self.sprite_left = []
        self.hinosprite = []
        self.hinoleftsprite = []
        self.hinoanimate = False
        self.hinoleftanimate = False
        self.is_animating = False
        
        self.sprite_right.append(pygame.image.load('tanimate1.png'))
        self.sprite_right.append(pygame.image.load('tanimate2.png'))
        self.sprite_right.append(pygame.image.load('tanimate3.png'))
        
        self.sprite_left.append(pygame.image.load('tanimate4.png'))
        self.sprite_left.append(pygame.image.load('tanimate5.png'))
        self.sprite_left.append(pygame.image.load('tanimate6.png'))
        self.image = self.sprite_right[0]
        self.hinosprite.append(pygame.image.load('flamedance1.png'))
        self.hinosprite.append(pygame.image.load('flamedance2.png'))
        self.hinosprite.append(pygame.image.load('flamedance3.png'))
        self.hinosprite.append(pygame.image.load('flamedance4.png'))
        self.hinosprite.append(pygame.image.load('flamedance5.png'))
        
        self.hinoimage = self.hinosprite[0]
        self.currenthino = 0

        self.hinoleftsprite.append(pygame.image.load('flameleft1.png'))
        self.hinoleftsprite.append(pygame.image.load('flameleft2.png'))
        self.hinoleftsprite.append(pygame.image.load('flameleft3.png'))
        self.hinoleftsprite.append(pygame.image.load('flameleft4.png'))
        

        self.hinoleftimage = self.hinoleftsprite[0]
        self.currenthinoleft = 0
        
        
        
        self.currentsprite = 0
        if self.right:
            self.image = self.sprite_right[self.currentsprite]
        elif self.left:
            self.image = self.sprite_left[self.currentsprite]

            

    def animate(self):
        self.is_animating = True
        
        

    
    def update(self, win):
        if self.is_animating == True:
            self.currentsprite += 0.4

            
        
            if self.right:
                if self.currentsprite >= len(self.sprite_right):
                    self.currentsprite = 0
                    self.is_animating = False
            elif self.left:
                if self.currentsprite >= len(self.sprite_left):
                    self.currentsprite = 0
                    self.is_animating = False

                    
                
            if self.right:
                self.image = self.sprite_right[int(self.currentsprite)]
            if self.left:
                self.image = self.sprite_left[int(self.currentsprite)]
            if self.right:
                win.blit(self.image, (self.x - 50, self.y - 30))
            elif self.left:
                win.blit(self.image, (self.x, self.y - 30))
    def hinoanimating(self):
        self.hinoanimate = True
        self.x += self.vel * 2
        
    def hinoupdate(self, win):
        if self.hinoanimate == True:
            self.currenthino += 0.4
            
            if self.currenthino >= len(self.hinosprite):
                self.currenthino = 0
                self.hinoanimate = False
            self.hinoimage = self.hinosprite[int(self.currenthino)]
            win.blit(self.hinoimage, (self.x, self.y))
    def hinoleftanimating(self):
        self.hinoleftanimate = True
        self.x -= self.vel * 2
        
    def hinoleftupdate(self, win):
        if self.hinoleftanimate == True:
            self.currenthinoleft += 0.4
            
            if self.currenthinoleft >= len(self.hinoleftsprite):
                self.currenthinoleft = 0
                self.hinoleftanimate = False
            self.hinoleftimage = self.hinoleftsprite[int(self.currenthinoleft)]
            win.blit(self.hinoleftimage, (self.x, self.y))

  
        
            


        


        
        
        
       



    def redraw(self, win):
        pygame.draw.rect(win, (250,0,0), (20, 10, 500, 15))
        pygame.draw.rect(win, (0, 255, 0), (20, 10, (50 * self.health), 15))
        if self.hinoanimate == False and self.hinoleftanimate == False:
            self.hitbox = (self.x + 4, self.y, 60, 60 )
        if self.is_animating == False and self.hinoanimate == False and self.hinoleftanimate == False:
            if self.walkcount + 1 == 3:
                self.walkcount = 0
           

            if not(self.standing):
                if self.right:
                    win.blit(tanjiroright[self.walkcount // 1], (self.x,self.y))
                    self.walkcount += 1
                elif self.left:
                    win.blit(tanjiroleft[self.walkcount // 1], (self.x, self.y))
                    self.walkcount += 1
            
            else:
                if self.right:
                    win.blit(tanjiro, (self.x, self.y))
                else:
                    win.blit(tanjirol, (self.x, self.y))
            
            
            
            #pygame.draw.rect(win, (255, 0,0), self.hitbox,2)

    def gameend(self):
        
        self.jump = False
        self.jumpcount = 10
        
        if self.x < goblin.x and self.x - self.width - (self.vel * 10) > 0 :
            self.y = 300
            self.x -= (self.vel * 10)
        elif self.x < goblin.x and self.x + self.width - (self.vel * 10) < 0 :
            self.x = 600
        else:
            if self.x > goblin.x and self.x + self.width + (self.vel * 10) < 720 :
                self.y = 300
                self.x += (self.vel * 10)
            elif self.x > goblin.x and self.x + self.width + (self.vel * 10) > 720 :
                self.x = 30
                self.y = 300

            
        
        self.walkcount = 0
        if self.health == 0:
            font1 = pygame.font.SysFont('comicsans', 100)
            text = font1.render(str(score),  1, (255,0,0))
            win.blit(text, (363 - (text.get_width() // 2), 100))
            pygame.display.update()
            pygame.time.delay(2000)
            i = 0
            while i < 300:
                i += 1
                if i == 299:
                    menu = True
                    menut()
            
    
                    
       

 
            
    
        
        

class projectile():
    def __init__(self, x, y, right):
        self.x = x
        self.y = y
        self.vel = 16 * facing
        self.right = False
        if man.right or man.hinoright:
            self.right = True
        else:
            self.right = False
    def draw(self, win):
        if self.right:
            win.blit(splash, (self.x, self.y))
        else:
            win.blit(splash2, (self.x, self.y))

    def hino(self, win):
        if self.right:
            win.blit(hinok, (self.x, self.y))
        else:
            win.blit(hinoka, (self.x, self.y))

class enemy():
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load("R11E.png")]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
    def __init__(self, x, y, width, height, end, health, visible, e_count): #for optimization, 
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x +17, self.y + 2, 31, 57)
        self.health = health
        self.visible = visible
        self.direct = 1
        self.e_count = e_count
        self.walkright = False
        


    def draw(self, win):
        if self.e_count == 1:
            self.move()
            self.respawn()
            if self.visible:
                if self.walkcount + 1 >= 33:
                    self.walkcount = 0
                if self.walkright:
                    win.blit(self.walkRight[self.walkcount // 3], (self.x, self.y))
                    self.walkcount += 1
                else:
                    win.blit(self.walkLeft[self.walkcount // 3], (self.x, self.y))
                    self.walkcount += 1
                pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
                pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 -self.health)), 10))
                self.hitbox = (self.x +17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
             
        

    def move(self):
        
        if self.x > man.x:
                self.x -= self.vel
                self.walkright = False
                
        else:
            self.x += self.vel
            
            self.walkright = True
    def hit(self):
        global score
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
            score += 1
        print('demon hit')
    def respawn(self):
        global score
        if self.e_count == 1:
            if self.visible == False :
                
                pygame.time.delay(150)
                if man.x < 300:
                    self.x = random.randrange(100, 350) - (man.width + man.vel) 
                    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                            self.x = rand.randrange(300, 350)

                else:
                    self.x = random.randrange(400, 600) - (man.width + man.vel)
                    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                            self.x = rand.randrange(350, 500)

                self.health = 10
                self.visible = True
                pygame.draw.rect(win, (0, 255, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 -self.health)), 10))
            
            
            
            
            

            
        
        
    
    
            

def draw():
    
    if bg1 == True:
        win.blit(dmbg, (0,0))
    if bg2 == True:
        win.blit(dmbg2, (0,0))
    text = font.render('score:' + str(score), 1, (16,231,239))
    text2 = font.render('Final selection completed', 1, (16,231,239))

    goblin.draw(win)
    

    man.redraw(win)
    man.update(win)
    man.hinoupdate(win)
    man.hinoleftupdate(win)
    

    for bullet in bullets:
        bullet.draw(win)

    for bullet in hinokami:
        bullet.hino(win)

    #if score == 10:
       # win.blit(text2, (100,200))
        
        global run
        
        
        
    
        

    
    pygame.display.update()
   

def menudraw():
    win.blit(menuu, (0,0))
    text3 = font3.render('Press Any Key To start', 3, (255,0,0))
    win.blit(text3, (150, 5))

        
    pygame.display.update()


    
#menu
menu = True
font3= pygame.font.SysFont('verdana', 45, True)
font = pygame.font.SysFont('comicsans', 30, True)
font1 = pygame.font.SysFont('comicsans', 100)
man = player(30, 300, 60, 60, 10)
goblin = enemy(200, 300, 64, 64, 700, 10, True, 1)
bullets = []
hinokami = []
shootloop = 0
facing = 1


def menut():
    global man
    global goblin
    global score
    man.health = 10
    man.x = 30
    man.y = 300
    score = 0
    goblin.health = 10
    
    global menu
    nezuko = False
    run = False
    menu = True
    
    while menu == True:
        menudraw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                menu = False
                run = True
                
if menu == True:
    menut()
    
        

    


def running():
        #mainloop
        

        

        
        run = True
        man.right = True
        global score
        global shootloop
        global hinkami
        global bullets
        global facing
        global bg1
        global bg2

        while run:
            clock.tick(27)
            if goblin.visible == True:
                if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
                    if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
                        man.gameend()
                        man.health -= 1
            
                                
            
            if shootloop > 0:
                shootloop += 1
            if shootloop > 3: 
                shootloop = 0

            


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if score == 10:
                man.x = 30
                pygame.time.delay(10000)
                score += 1
                
                

            for bullet in bullets:
                if goblin.visible == True:
                    if bullet.y < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y > goblin.hitbox[1]:
                        if bullet.x > goblin.hitbox[0] and bullet.x < goblin.hitbox[0] + goblin.hitbox[2]:
                            goblin.hit()
                            
                            bullets.pop(bullets.index(bullet))
            
                    
                #making sure the bullets delete after leaving screen
                if bullet.x < 736 and bullet.x > 0:
                    bullet.x += bullet.vel
                else:
                    bullets.pop(bullets.index(bullet))

            for bullet in hinokami:
                if goblin.visible == True:
                    if bullet.y < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y > goblin.hitbox[1]:
                        if bullet.x > goblin.hitbox[0] and bullet.x < goblin.hitbox[0] + goblin.hitbox[2]:
                            goblin.health -= 50
                            goblin.hit()
                            
                            

                if bullet.x < 6000 and bullet.x > -3000:
                    bullet.x += bullet.vel
                else:
                    hinokami.pop(hinokami.index(bullet))
            
            
                    
            # beggining biome codes
            #if goblin.visible == False and score >= 10:
                
                #if man.x >= 500 and bg1 == True:
                   # man.x = 30
                #    bg1 = False
                    
                    
                #    if bg2 == False:
                 #       man.x = 30
                #    bg2 = True
                # gonna have the game be an endless, might make it more? idk
                    
                
                    
                

                


            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE] and shootloop == 0:
                man.animate()
                
               
                if man.left: #the facing make the splash go in what direction i'm facing
                    facing = -1
                else:
                    facing = 1
                #making it so if there are less than 3 bullets when we press space, it creates another bullet
                if len(bullets) < 2:
                    if man.right: #making it so that if im looking right it spawns in front of me and vice versao
                        bullets.append(projectile(round(man.x + man.width // 2 ), round(man.y + man.height // 20), False ))
                    elif man.left:
                        bullets.append(projectile(round(man.x + man.width // -2), round(man.y + man.height // 20), True))
            if keys[pygame.K_h] and keys[pygame.K_k] and man.x < 736 - man.width - man.vel and man.x > 0:
                
                if man.right:
                    man.hinoanimating()
                if man.left:
                    man.hinoleftanimating()
                
                if man.hinoleft: #the facing make the splash go in what direction i'm facing
                    facing = -1
                else:
                    facing = 1
                if len(hinokami) < 1:
                    if man.hinoright:
                        hinokami.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 20), False))
                    elif man.hinoleft:
                        hinokami.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 20), False))
                        
                    
                shootloop = 1 
            if keys[pygame.K_RIGHT] and man.x < 736 - man.width - man.vel:
                    man.x += man.vel
                    man.right = True
                    man.left = False
                    man.hinoright = True
                    man.hinoleft = False
                    man.standing = False
                    

            elif keys[pygame.K_LEFT] and man.x > man.vel:
                man.x -= man.vel
                man.left = True
                man.right = False
                man.hinoright = False
                man.hinoleft = True
                man.standing = False
            else:
                man.standing = True
                man.walkcount = 0



            if man.jump == False:
                if keys[pygame.K_UP]:
                    man.jump = True
                    
                    
            else:
                 if man.jumpcount >= -10:
                    neg = 1
                    if man.jumpcount < 0:
                        neg = -1
                    man.y -= (man.jumpcount ** 2) * 0.5 * neg
                    man.jumpcount -= 1

                 else:
                    man.jumpcount = 10
                    man.jump = False
            


           





            draw()

            

if menu == False:
    running()
    



























