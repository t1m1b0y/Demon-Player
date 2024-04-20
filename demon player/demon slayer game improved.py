import pygame

pygame.init()


win = pygame.display.set_mode((500, 480))
pygame.display.set_caption(('hinokami chronicles'))



walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('tanji.png')

tanjiroright = [pygame.image.load('tanjiro1.png'), pygame.image.load('tanjiro2.png')]
tanjiroleft = [pygame.image.load('tanjiro3.png'), pygame.image.load('tanjiro4.png')]
tanjiro = [pygame.image.load('tanji.png')]
clock = pygame.time.Clock()



class player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.vel = 20
        self.right = False
        self.left = False
        self.walkcount = 0
        self.jumpcount = 10
        self.jump = False



    def redraw(self, win):
        if self.walkcount + 1 == 3:
            self.walkcount = 0

        if self.right:
            win.blit(tanjiroright[self.walkcount // 1], (self.x,self.y))
            self.walkcount += 1
        elif self.left:
            win.blit(tanjiroleft[self.walkcount // 1], (self.x, self.y))
            self.walkcount += 1
        else:
            win.blit(char, (self.x, self.y))
        
        



def draw():
    

    win.blit(bg, (0,0))

    man.redraw(win)

    
    pygame.display.update()
   

    


run = True
man = player(300, 410, 64, 64,)
while run:

    pygame.time.delay(50)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False

    elif keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
    else:
        man.right = False
        man.left = False



    if man.jump == False:
        if keys[pygame.K_SPACE]:
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









pygame.quit()
















