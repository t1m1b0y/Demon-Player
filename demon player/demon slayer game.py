import pygame

pygame.init()


win = pygame.display.set_mode((500, 500))
pygame.display.set_caption(('hinokami chronicles'))



walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('tanji.png')

tanjiroright = [pygame.image.load('tanjiro1.png'), pygame.image.load('tanjiro2.png')]
tanjiroleft = [pygame.image.load('tanjiro3.png'), pygame.image.load('tanjiro4.png')]
tanjiro = [pygame.image.load('tanji.png')]
clock = pygame.time.Clock()
x = 270
y = 400
width = 64
height = 64
vel = 10



walkcount = 0
right = False
left = False

jump = False
jumpcount = 10


def draw():
    global walkcount

    win.blit(bg, (0,0))

    if walkcount + 1 == 3:
        walkcount = 0

    if right:
        win.blit(tanjiroright[walkcount // 1], (x,y))
        walkcount += 1
    elif left:
        win.blit(tanjiroleft[walkcount // 1], (x, y))
        walkcount += 1
    else:
        win.blit(char, (x, y))
        
         




    

    pygame.display.update()
   

    


run = True
while run:

    pygame.time.delay(100)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
            x += vel
            right = True
            left = False

    elif keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    else:
        right = False
        left = False



    if jump == False:
        if keys[pygame.K_SPACE]:
            jump = True
            
    else:
         if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1

         else:
            jumpcount = 10
            jump = False





    draw()









pygame.quit()
















