import os
import pygame
import time
import random
import json

from pygame.font import SysFont

pygame.init()

#My colors:

retrocolor=(0,80,50)
black=(0,0,0)
white=(255,255,255) #Normal white
white2=(30,255,30)   #Music on
white3=(255,50,50)   #Music off
_dark_gray=(25,25,25)
_dark_gray2=(55,55,55)
red_=(100,0,0)
dark_blue=(20,10,60)
gray=(150,150,150)
yellow=(153,153,0)

#Text fonts
#fonts=pygame.font.get_fonts()
#for i in fonts:
   #print(i)

ExitFont=pygame.font.Font(None,30)
NormalFont=pygame.font.SysFont("arial",32)
OstFont=pygame.font.SysFont("century",35)
Game__Over__Font=pygame.font.SysFont("arial",50)
Start_Font=pygame.font.SysFont("bauhaus",80)

#Game options
Screen_size=(1530,730)
Screen=pygame.display.set_mode(Screen_size)

FPS=100

#Character design
character_=pygame.image.load("yuruyen_adam.png")
character_loc=character_.get_rect()
character_loc.topleft=(700,350)
speed=1.5

Clock_=pygame.time.Clock()

jumping=False
jumping_height=0
jumping_sınır=False

Starting=False

Standing_=True

Game__Over=False
Jumping_count=0
shoot_boolen=False
Direction_=True
#In Direction; True means right , False means left

Niggacent=0

Atack=2
Enemy_lines=Atack*2

milisecond=0
second=0
fps_counter=0

pygame.display.set_caption("Nigga man")

        
#Starting Screen

Start_screen=True
while Start_screen:
    Screen.fill(retrocolor)
    for Event in pygame.event.get():
        if Event.type==pygame.QUIT:
            Loop_=False
            Start_screen=False
            Start=False
        if Event.type==pygame.MOUSEBUTTONDOWN:
            Mousex,Mousey=Event.pos
            if Start_button.collidepoint(Mousex,Mousey):
                Starting=True
                print("Game started")
                Start=True
                Start_screen=False
                Start_button=pygame.draw.rect(Screen,yellow,(585,505,300,50),0)
                Start_=Start_Font.render("Start",True,white)
                Start_loc=Start_.get_rect()
                Start_loc=(665,505)
                Screen.blit(Start_,Start_loc)
                pygame.display.update()


    if Starting==False:
        pygame.draw.rect(Screen,_dark_gray2,(587,507,300,50),0)
        Start_button=pygame.draw.rect(Screen,yellow,(580,500,300,50),0)
        Start_=Start_Font.render("Start",True,white)
        Start_loc=Start_.get_rect()
        Start_loc=(660,500)
        Screen.blit(Start_,Start_loc)
    Niggacent_text=NormalFont.render(f"Niggacent = {Niggacent}",True,black)
    Niggacent_text_loc=Niggacent_text.get_rect()
    Niggacent_text_loc=(1200,50)
    Screen.blit(Niggacent_text,Niggacent_text_loc)
    pygame.display.update()
    if Starting:
        time.sleep(1)

if Start==False:
    pygame.quit()

if Start:
    #Music settings
    music=pygame.mixer.music.load("background_music.wav")
    pygame.mixer.music.play(-1,0,0)
    Music_play=True
    Music_on_loc=(680,625)
    Music_off_loc=(770,625)



class Falling:
    def __init__(self,location,Jumping_count,Standing_,jumping):
        self.count=Jumping_count
        self.loc_=location
        self.jumping=jumping
        self.Standing_=Standing_
        if not self.loc_.colliderect(myline) and not self.loc_.colliderect(fall_stopping_object) and not self.loc_.colliderect(myline_2) and self.jumping==False:
            self.loc_.y+=1

class Enemy:
    def __init__(self,Atack,location,Enemy_lines,second):
        self.Atack=Atack
        self.location=location
        self.lines=Enemy_lines
        self.second=second
        for self.line_counter in range(0,Enemy_lines):
            self.linex=random.randint(-1,1531)
            if self.linex<1530 and self.linex>0:
                self.liney=random.choice((0,730))
                pygame.draw.line(Screen,black,(self.linex,self.liney),(self.location.x+10,self.location.y-5),10)
            else:
                self.liney=random.randint(0,730)
                pygame.draw.line(Screen,black,(self.linex,self.liney),(self.location.x+10,self.location.y-5),10)



Jumping_option=True
bullet=3
Shooting=False

_open=False

Paused=False
if Start==True:
    _open=True
while _open:
    Enemy_lines=Atack*2
    if Paused==False:
        fps_counter+=1
        if fps_counter==FPS/100:
            milisecond+=1
            fps_counter=0
        if milisecond==100:
            milisecond=0
            second+=1
        #Enemy(Atack,character_loc,Enemy_lines,second)
    for gameEvent in pygame.event.get():
        if gameEvent.type==pygame.KEYUP:
            if (gameEvent.key==pygame.K_w or gameEvent.key==pygame.K_UP) :
                jumping=False
                jumping_sınır=False
                jumping_height=0
                if (not character_loc.colliderect(myline) or character_loc.colliderect(fall_stopping_object) or character_loc.colliderect(myline_2)) and Jumping_count>0:
                    Jumping_option=False
                Jumping_count+=1
        if gameEvent.type==pygame.QUIT:
            _open=False
        if gameEvent.type==pygame.MOUSEBUTTONDOWN:
            MousePointx,MousePointy=gameEvent.pos
            if Paused==True:
                if Music_button.collidepoint(MousePointx,MousePointy) or Music_button_circle1.collidepoint(MousePointx,MousePointy) or Music_button_circle2.collidepoint(MousePointx,MousePointy):
                    if Music_play==True:
                        Music_play=False
                        pygame.mixer.music.pause()
                        print("Music paused")
                    elif Music_play==False:
                        Music_play=True
                        pygame.mixer.music.unpause()
                        print("Music unpaused")
                    pygame.display.update()
                if Continue_button.collidepoint(MousePointx,MousePointy) or Continue_circle1.collidepoint(MousePointx,MousePointy) or Continue_circle2.collidepoint(MousePointx,MousePointy):
                    Paused=False
                    print("Continue")
            if MousePointx>1484 and MousePointx<1515 and MousePointy>14 and MousePointy<45:
                _open=False
                pygame.mixer.music.stop()
            if MousePointx>1484 and MousePointx<1515 and MousePointy>54 and MousePointy<85:
                print("Paused")
                Paused=True
    Key_down=pygame.key.get_pressed()
    if (Key_down[pygame.K_a] or Key_down[pygame.K_LEFT]) and Paused==False and character_loc.x>0 :
        character_loc.x-=speed
        character_=pygame.image.load("yuruyen_adam_sağa.png")
        Direction_=False
    if (Key_down[pygame.K_d] or Key_down[pygame.K_RIGHT]) and Paused==False and character_loc.x<1480:
        character_loc.x+=speed
        character_=pygame.image.load("yuruyen_adam.png")
        Direction_=True
    if (Key_down[pygame.K_w] or Key_down[pygame.K_UP]) and Paused==False and character_loc.y>0 and jumping_sınır==False and  Jumping_option:
        jumping=True
        character_loc.y-=1
        jumping_height+=1
        if jumping_height==100:
            jumping_sınır=True
            jumping=False
    Screen.fill(retrocolor)
    circle_exit=pygame.draw.circle(Screen,black,(1500,30),15,4)
    Textexit=ExitFont.render("X",True,black)
    TextLocexit=Textexit.get_rect()
    TextLocexit=(1494,21)
    circle_pause=pygame.draw.circle(Screen,black,(1500,70),15,4)
    Textpause=ExitFont.render("ll",True,black)
    TextLocpause=Textpause.get_rect()
    TextLocpause=(1495,61)
    Clock_bg=pygame.image.load("rgb.jpg")
    Clock_bg_loc=Clock_bg.get_rect()
    Clock_bg_loc=(10,42)
    Screen.blit(Clock_bg,Clock_bg_loc)
    Clock_object=pygame.draw.rect(Screen,dark_blue,(10,42,100,57),5)
    timer_object=NormalFont.render(f"{second},{milisecond}",True,black)
    #Sayaç görüntü düzeltmesi
    if milisecond==0:
        timer_object=NormalFont.render(f"{second},{milisecond}0",True,black)
    timer_loc=timer_object.get_rect()
    timer_loc.topright=(95,50)
    Screen.blit(timer_object,timer_loc)
    myline_2=pygame.draw.line(Screen,white,(400,580),(630,580),20)
    fall_stopping_object=pygame.draw.line(Screen,red_,(0,730),(1530,730),10)
    myline = pygame.draw.line(Screen,white,(250,400),(950,400),23)
    Screen.blit(Textpause,TextLocpause)
    Screen.blit(Textexit,TextLocexit)
    Screen.blit(character_,character_loc)
    if Paused==True:
        pygame.draw.rect(Screen,_dark_gray,(1,1,1529,729),0)
        Continue_button=pygame.draw.rect(Screen,gray,(650,485,150,50),0)
        Continue_circle1=pygame.draw.circle(Screen,gray,(650,510),25,0)
        Continue_circle2=pygame.draw.circle(Screen,gray,(800,510),25,0)
        Music_button_circle1=pygame.draw.circle(Screen,dark_blue,(675,625),25,0)
        Music_button_circle2=pygame.draw.circle(Screen,dark_blue,(775,625),25,0)
        Music_button=pygame.draw.rect(Screen,dark_blue,(675,600,100,50),0)
        Continue=OstFont.render("Continue",True,white)
        ContinueLoc=Continue.get_rect()
        ContinueLoc=(650,487)
        Screen.blit(Continue,ContinueLoc)
        Music_paused_text=OstFont.render("Music",True,white)
        Music_paused_text_loc=Music_paused_text.get_rect()
        Music_paused_text_loc=(680,550)
        Screen.blit(Music_paused_text,Music_paused_text_loc)
        On=NormalFont.render("On",True,white)
        On_loc=On.get_rect()
        On_loc=(600,610)
        Screen.blit(On,On_loc)
        Off=NormalFont.render("Off",True,white)
        Off_loc=Off.get_rect()
        Off_loc=(810,610)
        Screen.blit(Off,Off_loc)
        if Music_play==True:
            pygame.draw.circle(Screen,white,Music_on_loc,20,5)
            pygame.draw.circle(Screen,white2,Music_on_loc,14,5)
            pygame.display.update()
        elif Music_play==False:
            pygame.draw.circle(Screen,white,Music_off_loc,20,5)
            pygame.draw.circle(Screen,white3,Music_off_loc,14,5)
            pygame.display.update()
    if Game__Over==True:
        Game_Over=Game__Over__Font.render("GAME OVER",True,black)
        Game_Over_Loc=Game_Over.get_rect()
        Game_Over_Loc=(650,400)
        Screen.blit(Game_Over,Game_Over_Loc)
    if character_loc.colliderect(myline) or character_loc.colliderect(fall_stopping_object) or character_loc.colliderect(myline_2):
        Jumping_option=True
        Jumping_count=0
    Falling(character_loc,Jumping_count,Standing_,jumping)

    pygame.display.update()
    Clock_.tick(FPS)
