from pickle import TRUE
import pygame,sys
def PLAY_GAME():
    #SCREEN DIMENTIONS
    WIDTH=1500
    HEIGHT=800
    #SCREEN IMAGES
    SCREEN_IMAGE=pygame.transform.scale(pygame.image.load(r"JUEGO\773D.tmp.png"),(WIDTH,HEIGHT))
    #PLAYER IMAGES
    DEATH_SCREEN_IMAGE=pygame.transform.scale(pygame.image.load(r"JUEGO\Captura.PNG"),(300,80))
    ##VADER IMAGES
    VADER=pygame.transform.scale(pygame.image.load(r"JUEGO\VADER.jpg"),(100,80))
    VADER_FLIPED=pygame.transform.flip(VADER,True,False)
    VADRER_90_left=pygame.transform.rotate(VADER,90)
    Vader_90_right=pygame.transform.rotate(VADER_FLIPED,270)
    #OBI ONE IMAGES
    OBI_ONE=pygame.transform.scale(pygame.image.load(r"JUEGO\FINAL KENOBI.PNG"),(100,80))
    OBI_ONE_FLIPPED=pygame.transform.flip(OBI_ONE,True,False)
    OBI_ONE_90_left=pygame.transform.rotate(OBI_ONE,90)
    OBI_ONE_90_right=pygame.transform.rotate(OBI_ONE_FLIPPED,270)
    #JERO
    JERO_IMAGE=pygame.transform.scale(pygame.image.load(r"JUEGO\LUKE.PNG"),(100,80))
    JERO_FLIPPED=pygame.transform.flip(JERO_IMAGE,True,False)
    JERO_90_left=pygame.transform.rotate(JERO_IMAGE,90)
    JERO_90_right=pygame.transform.rotate(JERO_FLIPPED,270)
    #COUNT DOOKU IMAGES
    COUNT_IMAGE=pygame.transform.scale(pygame.image.load(r"JUEGO\count.png"),(100,80))
    COUNT_FLIPPED=pygame.transform.flip(COUNT_IMAGE,True,False)
    COUNT_90_left=pygame.transform.rotate(COUNT_IMAGE,90)
    COUNT_90_right=pygame.transform.rotate(COUNT_FLIPPED,270)
    #SET SCREEN
    WIN=pygame.display.set_mode((WIDTH,HEIGHT))
    SEA_GREEN=(46,139,87)
    WHITE=(255,255,255)
    #GAME FPS
    FPS=60
    #PLAYER ATRIBUTES
    VELOCITY_VADER=7
    VELOCITY_OBI_ONE=14
    JERO_SPEED=10
    JERO_HIT=10
    JERO_LIFE=400
    COUNT_SPEED=10
    COUNT_LIFE=350
    COUNT_HIT=12
    VADER_LIFE=500
    OBI_ONE_LIFE=350
    OBI_ONE_HIT=20
    VADER_HIT=30

    #PLAYER RECTANGLES
    R1=pygame.Rect(300,600,100,80)
    R2=pygame.Rect(1000,600,100,80)

    clock=pygame.time.Clock()
    WIN.fill((0,0,0))





    def DRAW_WINDOW():
        WIN.fill(SEA_GREEN)
        FLOOR=pygame.Rect(0,500,1500,300)
        pygame.draw.rect(WIN,WHITE,FLOOR)
        WIN.blit(SCREEN_IMAGE,(0,0))
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
            JUMP=False
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
            pygame.draw.rect(WIN,(0,255,0),LIFE_BAR_1)
        def DRAW_HITBOX_1(self):
            self.hitbox_1 = (self.rect.x,self.rect.y,100,80)
        def DEATH1(self):
            if self.life_1 < 0:
                if self.direction == 1:
                    WIN.blit(self.image_death_1,(self.rect.x,self.rect.y))
                    WIN.blit(DEATH_SCREEN_IMAGE,(600,360))
                    pygame.display.update()
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
        def Life_bar_2(self):
            LIFE_BAR_2=pygame.Rect(1500-self.life_2,0,self.life_2,10)
            pygame.draw.rect(WIN,(0,255,0),LIFE_BAR_2)
        def DRAW_HITBOX_2(self):
            self.hitbox_2 = (self.rect.x,self.rect.y,100,80)
            
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
                    pygame.display.update()
                    pygame.time.delay(10000)
                    pygame.quit()
        
        

            
    if __name__=="__main__":
        
        run=True
        h="1)VADER"
        g="2)OBI-ONE"
        z="3)LUKE"
        l="4)COUNT DOOKU"

        dam=input(f"Choose player 1:\n{h}\n{g}\n{z}\n{l}\n")
        if dam == "1":
            PLAYER_1=CHARACTER_1(VADER,R1,VELOCITY_VADER,VADER_LIFE,VADER_FLIPED,VADER,VADER_HIT,VADRER_90_left,Vader_90_right)
            h=""
                
        elif dam =="2":
            PLAYER_1=CHARACTER_1(OBI_ONE,R1,VELOCITY_OBI_ONE,OBI_ONE_LIFE,OBI_ONE_FLIPPED,OBI_ONE,OBI_ONE_HIT,OBI_ONE_90_left,OBI_ONE_90_right)
            g=""

        elif dam == "3":
            PLAYER_1=CHARACTER_1(JERO_IMAGE,R1,JERO_SPEED,JERO_LIFE,JERO_FLIPPED,JERO_IMAGE,JERO_HIT,JERO_90_left,JERO_90_right)
            z=""
        elif dam == "4":
            PLAYER_1=CHARACTER_1(COUNT_IMAGE,R1,COUNT_SPEED,COUNT_LIFE,COUNT_FLIPPED,COUNT_IMAGE,COUNT_HIT,COUNT_90_left,COUNT_90_right)
            l=""
                

        while True:
            try:
                dam2=input(f"Choose player 2:\n{h}\n{g}\n{z}\n{l}\n")
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
                if dam2 =="3":
                    if z == "":
                        raise TypeError ("El player que seleccionaste ya esta elejido")
                    else:
                        PLAYER_2=CHARACTER_2(JERO_IMAGE,R2,JERO_SPEED,JERO_LIFE,JERO_FLIPPED,JERO_IMAGE,JERO_HIT,JERO_90_left,JERO_90_right)
                        break
                if dam2 == "4":
                    if l == "":
                        raise SystemError("El player que seleccionaste ya esta elejido")
                    else:
                        PLAYER_2=CHARACTER_2(COUNT_IMAGE,R2,COUNT_SPEED,COUNT_LIFE,COUNT_FLIPPED,COUNT_IMAGE,COUNT_HIT,COUNT_90_left,COUNT_90_right)
                        break
                    
            except SyntaxError as E:
                print(E)
            except ValueError as J:
                print(J) 
            except TypeError as K:
                print(K)
            except SystemError as D:
                print(D)
            

        while run:
            clock.tick(FPS)
            JUMP=False
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

def MAIN_MENU():

    def DRAW_MAIN_MENU():
        MARON = (128,0,0)
        BLACK = (0,0,0)
        RECT_FOR_TEXT=pygame.Rect(400,100,700,150)
        RECT_FOR_TEXT_2 = pygame.Rect(400,300,700,120)
        RECT_TEXT_3 = pygame.Rect(400,500,700,120)
        FONT= pygame.font.Font(r"JUEGO\RubikMoonrocks-Regular.ttf",120)
        TEXT = FONT.render("MAIN MENU",True,BLACK,MARON)
        TEXT_2 = FONT.render("PLAY GAME",True,BLACK,MARON)
        TEXT_EXIT = FONT.render("EXIT?",True,BLACK,MARON)
        WIDTH=1500
        HEIGHT=800
        WIN=pygame.display.set_mode((WIDTH,HEIGHT))
        WIN.fill(MARON)
        WIN.blit(TEXT,(400,100))
        WIN.blit(TEXT_2,(400,300))
        WIN.blit(TEXT_EXIT,(400,500))
        pygame.draw.rect(WIN,BLACK,RECT_FOR_TEXT,1)
        pygame.draw.rect(WIN,BLACK,RECT_FOR_TEXT_2,1)
        pygame.draw.rect(WIN,BLACK,RECT_TEXT_3,1)
        pygame.display.update()
        return RECT_FOR_TEXT_2,RECT_TEXT_3
    pygame.init()   
    run =True
    def IS_OVER(rect,pos):
        if rect.collidepoint(pos[0],pos[1]):
            return True
        else:
            return False

    while run:
        MOUSE=pygame.mouse.get_pos()
       
     
        x,y=DRAW_MAIN_MENU()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type == pygame.MOUSEBUTTONDOWN and IS_OVER(x,MOUSE) is True:
                PLAY_GAME()
                
                
            if event.type == pygame.MOUSEBUTTONDOWN and IS_OVER(y,MOUSE) is True:
                pygame.quit()

MAIN_MENU()