from matplotlib.patches import Rectangle
import pygame,sys


DEATH_SCREEN_IMAGE=pygame.transform.scale(pygame.image.load(r"C:\assets\Captura.PNG"),(300,80))
VADER=pygame.transform.scale(pygame.image.load(r"C:\assets\VADER.jpg"),(100,80))
VADER_FLIPED=pygame.transform.flip(VADER,True,False)
OBI_ONE=pygame.transform.scale(pygame.image.load(r"C:\assets\OBI_ONE.jpg"),(100,80))
OBI_ONE_FLIPPED=pygame.transform.flip(OBI_ONE,True,False)
WIDTH=1500
HEIGHT=800
WIN=pygame.display.set_mode((WIDTH,HEIGHT))
SEA_GREEN=(46,139,87)
FPS=60
WHITE=(255,255,255)
VELOCITY_VADER=7
VELOCITY_OBI_ONE=14
R1=pygame.Rect(300,600,100,80)
R2=pygame.Rect(1000,600,100,80)
VADER_LIFE=500
OBI_ONE_LIFE=350
OBI_ONE_HIT=20
VADER_HIT=30
clock=pygame.time.Clock()


VADRER_90_left=pygame.transform.rotate(VADER,90)
Vader_90_right=pygame.transform.rotate(VADER_FLIPED,270)
OBI_ONE_90_left=pygame.transform.rotate(OBI_ONE,90)
OBI_ONE_90_right=pygame.transform.rotate(OBI_ONE_FLIPPED,270)


def DRAW_WINDOW():
    WIN.fill(SEA_GREEN)
    FLOOR=pygame.Rect(0,500,1500,300)
    pygame.draw.rect(WIN,WHITE,FLOOR)
    pygame.display.update()


class CHARACTER(pygame.sprite.Sprite):
    def __init__(self,image,rectangle,velocity,hit,image_death_1,image_death_2):
        super().__init__()
        self.walk = image
        self.rect = rectangle
        self.velocity =velocity
        self.image_death_1 = image_death_1
        self.image_death_2 = image_death_2
        self.hit = hit
    def DRAW_PLAYER_ON_SCREEN(self):
        WIN.blit(self.walk,(self.rect.x,self.rect.y))
   
                
            
        

class CHARACTER_1(CHARACTER):
    def __init__(self,image,rectangle,velocity,life_1,image2,image_original,hit,image_death_1,image_death_2):
        CHARACTER.__init__(self,image,rectangle,velocity,hit,image_death_1,image_death_2)
        self.image_original_1= image_original
        self.imagedflipped1 = image2
        self.life_1=life_1
        self.direction = 1 #if 1, facing to the right, if 0 facing to the left
        
    def MOVEMENT(self):
        Player_input=pygame.key.get_pressed()
        if Player_input[pygame.K_a] and self.rect.x-self.velocity>0 :
            self.walk = self.imagedflipped1
            self.rect.x-=self.velocity
        if Player_input[pygame.K_d] and self.rect.x+self.velocity<1400:
            self.walk = self.image_original_1
            self.rect.x+=self.velocity
        if Player_input[pygame.K_w] and self.rect.y-self.velocity>500:
            self.rect.y-=self.velocity
        if Player_input[pygame.K_s] and self.rect.y+self.velocity<720:
            self.rect.y+=self.velocity
    def Life_bar_1(self):
        LIFE_BAR_1=pygame.Rect(0,0,self.life_1,10)
        pygame.draw.rect(WIN,(255,0,0),LIFE_BAR_1)
    def DRAW_HITBOX_1(self):
        self.hitbox_1 = (self.rect.x,self.rect.y,100,80)
        pygame.draw.rect(WIN,(0,0,0),self.hitbox_1,1)
    def DEATH1(self):
        if self.life_1 < 0:
            if self.direction == 1:
                WIN.blit(self.image_death_1,(self.rect.x,self.rect.y))
                WIN.blit(DEATH_SCREEN_IMAGE,(600,360))
                pygame.time.delay(10000)
                pygame.quit()
            if self.direction ==0:
                WIN.blit(self.image_death_2,(self.rect.x,self.rect.y))
                WIN.blit(DEATH_SCREEN_IMAGE,(600,360))
                pygame.display.update()
                pygame.time.delay(10000)
                pygame.quit()
    
        
    
        
    

class CHARACTER_2(CHARACTER):
    def __init__(self,image,rectangle,velocity,life_2,image2,image_original,hit,image_death_1,image_death_2):
        CHARACTER.__init__(self,image,rectangle,velocity,hit,image_death_1,image_death_2)
        self.image_original= image_original
        self.imageflipped = image2
        self.life_2 = life_2
        self.direction = 1 #if one, facing to the right, if 0 facing to the left    
    def MOVEMENT(self):
        JUMP=False
        VELOCITY_y=10
        Player_input=pygame.key.get_pressed()
        if Player_input[pygame.K_LEFT] and self.rect.x-self.velocity>0:
            self.walk= self.imageflipped
            self.direction=0
            self.rect.x-=self.velocity
        if Player_input[pygame.K_RIGHT] and self.rect.x+self.velocity<1400:
            self.walk = self.image_original
            self.direction=1
            self.rect.x+=self.velocity
        if Player_input[pygame.K_UP]and self.rect.y-self.velocity>500: 
            self.rect.y-=self.velocity
        if Player_input[pygame.K_DOWN] and self.rect.y+self.velocity<720:
            self.rect.y+=self.velocity
        # if Player_input[pygame.K_SPACE] and JUMP is False:
        #     JUMP=True
        # if JUMP is True:
        #     self.rect.y-=VELOCITY_y
        #     VELOCITY_y-=1
        #     if VELOCITY_y < -10:
        #         JUMP = False
        #         VELOCITY_y=10

    def Life_bar_2(self):
        LIFE_BAR_2=pygame.Rect(1500-self.life_2,0,self.life_2,10)
        pygame.draw.rect(WIN,(255,0,0),LIFE_BAR_2)
    def DRAW_HITBOX_2(self):
        self.hitbox_2 = (self.rect.x,self.rect.y,100,80)
        pygame.draw.rect(WIN,(0,0,0),self.hitbox_2,1)
    def DEATH2(self):
        if self.life_2 < 0:
            if self.direction == 1:
                WIN.blit(self.image_death_1,(self.rect.x,self.rect.y))
                WIN.blit(DEATH_SCREEN_IMAGE,(600,360))
                pygame.display.update()
                pygame.time.delay(10000)
                pygame.quit()
            if self.direction ==0:
                WIN.blit(self.image_death_2,(self.rect.x,self.rect.y))
                WIN.blit(DEATH_SCREEN_IMAGE,(600,360))
                pygame.time.delay(10000)
                pygame.quit()
    
    

        
def main():
    
    run=True
    h="1)VADER"
    g="2)OBI-ONE"

    dam=input(f"Choose player 1:\n{h}\n{g}\n")
    if dam == "1":
        PLAYER_1=CHARACTER_1(VADER,R1,VELOCITY_VADER,VADER_LIFE,VADER_FLIPED,VADER,VADER_HIT,VADRER_90_left,Vader_90_right)
        h=""
        
    elif dam =="2":
        PLAYER_1=CHARACTER_1(OBI_ONE,R1,VELOCITY_OBI_ONE,OBI_ONE_LIFE,OBI_ONE_FLIPPED,OBI_ONE,OBI_ONE_HIT,OBI_ONE_90_left,OBI_ONE_90_right)
        g=""
        

    while True:
        try:
            dam2=input(f"Choose player 2:\n{h}\n{g}\n")
            if dam2 == "1":
                if h=="":
                    raise SyntaxError("El player que seleccionaste ya esta elejido")
                else:
                    PLAYER_2=CHARACTER_2(VADER,R2,VELOCITY_VADER,VADER_LIFE,VADER_FLIPED,VADER,VADER_HIT,VADRER_90_left,Vader_90_right)
                    break
            if dam2 == "2":
                if g == "":
                    raise ValueError("El player que seleccionaste ya esta elejido")
                else:
                    PLAYER_2=CHARACTER_2(OBI_ONE,R2,VELOCITY_OBI_ONE,OBI_ONE_LIFE,OBI_ONE_FLIPPED,OBI_ONE,OBI_ONE_HIT,OBI_ONE_90_left,OBI_ONE_90_right)
                    break
                
        except SyntaxError as E:
            print(E)
        except ValueError as J:
            print(J)      
    
    
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LCTRL and PLAYER_1.rect.colliderect(PLAYER_2.rect):
                        collition_tolerance=10
                        PLAYER_2.life_2 = PLAYER_2.life_2-PLAYER_1.hit
                    if event.key == pygame.K_RCTRL and PLAYER_2.rect.colliderect(PLAYER_1.rect):
                        PLAYER_1.life_1 = PLAYER_1.life_1 - PLAYER_2.hit
                   
                    


                        
                        
        DRAW_WINDOW()
        PLAYER_1.DRAW_PLAYER_ON_SCREEN()
        PLAYER_2.DRAW_PLAYER_ON_SCREEN()
        PLAYER_1.MOVEMENT()
        PLAYER_2.MOVEMENT()
        PLAYER_1.Life_bar_1()
        PLAYER_2.Life_bar_2()
        PLAYER_1.DRAW_HITBOX_1()
        PLAYER_2.DRAW_HITBOX_2()
        pygame.display.update()
        PLAYER_1.DEATH1()
        PLAYER_2.DEATH2()
        
        

        pygame.time.delay(10)
    pygame.quit()


if __name__=="__main__":
    
    pygame.init()
    main()