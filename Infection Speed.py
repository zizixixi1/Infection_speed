
import pygame
import sys
from pygame.locals import *
from random import *
import matplotlib.pyplot as plt
 

class Ball(pygame.sprite.Sprite):
    def __init__(self, image1, image2, position, speed, bg_size, left, right, top, bottom, infected_times):

        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image1).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.left, self.rect.top = position
        self.speed = speed
        self.left, self.right = left, right
        self.top, self.bottom = top, bottom
        self.radius = self.rect.width / 2  
        
        self.infected_times = infected_times
        
 
    def move(self,image2):
        self.rect = self.rect.move(self.speed)
        
        if self.infected_times >=3 :
            self.image = pygame.image.load(image2).convert_alpha()
 
       
        if self.rect.left < self.left:
            self.rect.right = self.right-1
 
        elif self.rect.right > self.right:
            self.rect.left = self.left+1
 
        elif self.rect.top < self.top:
            self.rect.bottom = self.bottom-1
 
        elif self.rect.bottom > self.bottom:
            self.rect.top = self.top+1


        
def main():
    pygame.init()
 
    image1 = "ball1.png"
    image2 = "ball2.png"
    
    running = True
 
    
    bg_size = width, height = 1250, 600
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("Infection Speed")
 
    bg_color = (233,233,233)

    line = pygame.Rect(600,0,50,600)
    line_color = (0,0,0)


    num1=1
    num2=1
    num1s = []
    num2s = []

    balls1 = []
    balls2 = []
    group1 = pygame.sprite.Group()
    group2 = pygame.sprite.Group()


    gametime = 0

   
    for i in range(20):
        if i < 1:
            infected_times = 3
        else:
            infected_times = 0
        position = randint(0, 600), randint(0, 600)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(image1,image2, position, speed, bg_size,  0, 600, 0, 600, infected_times)
        while pygame.sprite.spritecollide(ball, group1, False, pygame.sprite.collide_circle) or speed == [0,0]:
            ball.rect.left, ball.rect.top = randint(0, 600), randint(0, 600)
            speed = [randint(-10, 10), randint(-10, 10)]
        balls1.append(ball)
        group1.add(ball)
    for j in range(25):
        if j < 1:
            infected_times = 3
        else:
            infected_times = 0
        position = randint(650, 1250), randint(0, 600)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(image1,image2, position, speed, bg_size, 650, 1250, 0, 600,infected_times)
        while pygame.sprite.spritecollide(ball, group2, False, pygame.sprite.collide_circle) or speed == [0,0]:
            ball.rect.left, ball.rect.top = randint(650, 1250), randint(0, 600)
            speed = [randint(-10, 10), randint(-10, 10)]
        balls2.append(ball)
        group2.add(ball)
 
    clock = pygame.time.Clock()
 
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
        screen.fill(bg_color)
        pygame.draw.rect(screen,line_color, line)
        
        for each in balls1:
            each.move(image2)
            screen.blit(each.image, each.rect)
 
        for each in group1:
            group1.remove(each) 
            b = pygame.sprite.spritecollide(each, group1, False, pygame.sprite.collide_circle)
            if b:
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
                if num1 <= 20:
                    for a in b:
                        if a.infected_times >=3  and each.infected_times <3:
                            each.infected_times += 1
                            if each.infected_times == 3:
                                num1 +=1
 
            group1.add(each)
        for each in balls2:
            each.move(image2)
            screen.blit(each.image, each.rect)
 
        for each in group2:
            group2.remove(each) 
            b = pygame.sprite.spritecollide(each, group2, False, pygame.sprite.collide_circle)
            if b:
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
                if num2 <= 25:
                    for a in b:
                        if a.infected_times >=3  and each.infected_times <3:
                            each.infected_times += 1
                            if each.infected_times == 3:
                                num2 +=1
 
            group2.add(each)

        gametime +=1

        if gametime % 100 == 0 :
            num1s.append(num1/20)
            num2s.append(num2/25)
                
        pygame.display.flip()
        clock.tick(30)

        if gametime == 1600:
            pygame.quit()
            break
    plt.plot(num1s, linewidth = 1)
    plt.plot(num2s, linewidth = 1)
    plt.title("infected numbers", fontsize = 24)
    plt.xlabel("date", fontsize = 14)
    plt.ylabel("people infected", fontsize = 14)
    plt.show()
 
 
if __name__ == "__main__":
    main()
