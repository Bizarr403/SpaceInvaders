import pygame, math, random
pygame.init()


Height = 600
Width =  800
running = True
screen = pygame.display.set_mode((Width, Height))
Icon = pygame.display.set_icon(pygame.image.load("ufo.png"))
Title = pygame.display.set_caption("Space Invaders")
Colour = (235, 245, 255)

#Player
image1 = pygame.image.load('spaceship2.png')
player_x = 364
player_y = 464
player_x_change = 0
def Playerimg(x, y):
    screen.blit(image1, (x, y))

#Alien
image2 = []
alien_x = []
alien_y = []
alien_x_change = []
alien_y_change = []
num_of_aliens = 6

for i in range(num_of_aliens):
    image2.append(pygame.image.load('monster.png'))
    alien_x.append(random.randint(0, 800))
    alien_y.append(random.randint(50, 200))
    alien_x_change.append(0.3)
    alien_y_change.append(40)




def Enemyimg(x, y, i):
    screen.blit(image2[i], (x, y))


#collisiondetection

def isCollision(x1, y1, x2, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance <= 27:
        return True
    else:
        return False



#Bullet
image3 = pygame.image.load('bullet.png')
bullet_x = 364
bullet_y = 464
bulletx_change = 0.2
bullety_change = -0.2
bullet_state = "ready"
def bulletimg(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(image3, (x, y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -0.5
            if event.key == pygame.K_RIGHT:
                player_x_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_x
                    bullet_y = player_y
                    bulletimg(bullet_x, bullet_y)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_x_change = 0
            if event.key == pygame.K_RIGHT:
                player_x_change = 0
            

    if player_x <= 0:
        player_x = 0
    if player_x >= 764:
        player_x = 768
    for i  in range(num_of_aliens):
        alien_x[i] += alien_x_change[i]
        if alien_x[i] >= 784:
            alien_x_change[i] = -0.3
            alien_y[i] += alien_y_change[i]
        if alien_x[i] <= 0 :
            alien_x_change[i] = 0.3
            alien_y[i] += alien_y_change[i]
        coll = isCollision(alien_x[i], alien_y[i], bullet_x, bullet_y)
        if coll:
            bullet_x = player_x
            bullet_state = "ready"
            alien_x[i] = random.randint(0, 800)
            alien_y[i] = random.randint(50, 200)
        Enemyimg(alien_x[i], alien_y[i], i)  


        

    screen.fill(Colour)
    
    Playerimg(player_x, player_y)
    
    if bullet_state == "fire":
        bulletimg(bullet_x, bullet_y)
        bullet_y += bullety_change
    if bullet_y <= 0:
        bullet_x = player_x
        bullet_state = "ready"

   
         
    
    player_x += player_x_change
    
    pygame.display.update()