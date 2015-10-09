import pygame, time
from pygame.locals import*

#Printing text
def print_text(font, x, y, text, color=(255,255,255)):
    imgText = font.render(text, True, color)
    screen.blit(imgText, (x,y))

#Main
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((600,500))
pygame.display.set_caption("Tic Tac Toe")
font1 = pygame.font.Font(None, 24)
font2 = pygame.font.Font(None, 40)
blue = 0,0,255
red = 255,0,0
white = 255,255,255
black = 0,0,0

#Var and bools
turn_x = False
turn_o = False
x1 = False
x2 = False
x3 = False
x4 = False
x5 = False
x6 = False
x7 = False
x8 = False
x9 = False
o1 = False
o2 = False
o3 = False
o4 = False
o5 = False
o6 = False
o7 = False
o8 = False
o9 = False
s1 = False
s2 = False
s3 = False
s4 = False
s5 = False
s6 = False
s7 = False
s8 = False
s9 = False
game_start = True
x = y = 0
clock_start = 0
seconds = 2



#Main loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:          #Exit
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:         #If the user clicks the LMB
            x, y = event.pos
            #If its x's turn
            if turn_x == True:
                if (x in range(100,250)) and (y in range(300,400)):
                    x1 = True
                    turn_x = False
                    turn_o = True
                if (x in range(250,350)) and (y in range(300,400)):
                    x2 = True
                    turn_x = False
                    turn_o = True
                if (x in range(350,500)) and (y in range(300,400)):
                    x3 = True
                    turn_x = False
                    turn_o = True
                if (x in range(100,250)) and (y in range(200,300)):
                    x4 = True
                    turn_x = False
                    turn_o = True
                if (x in range(250,350)) and (y in range(200,300)):
                    x5 = True
                    turn_x = False
                    turn_o = True
                if (x in range(350,500)) and (y in range(200,300)):
                    x6 = True
                    turn_x = False
                    turn_o = True
                if (x in range(100,250)) and (y in range(100,200)):
                    x7 = True
                    turn_x = False
                    turn_o = True
                if (x in range(250,350)) and (y in range(100,200)):
                    x8 = True
                    turn_x = False
                    turn_o = True
                if (x in range(350,500)) and (y in range(100,200)):
                    x9 = True
                    turn_x = False
                    turn_o = True
            #If its o's turn  
            elif turn_o == True:
                if (x in range(100,250)) and (y in range(300,400)):
                    o1 = True
                    turn_o = False
                    turn_x = True
                if (x in range(250,350)) and (y in range(300,400)):
                    o2 = True
                    turn_o = False
                    turn_x = True
                if (x in range(350,500)) and (y in range(300,400)):
                    o3 = True
                    turn_o = False
                    turn_x = True
                if (x in range(100,250)) and (y in range(200,300)):
                    o4 = True
                    turn_o = False
                    turn_x = True
                if (x in range(250,350)) and (y in range(200,300)):
                    o5 = True
                    turn_o = False
                    turn_x = True
                if (x in range(350,500)) and (y in range(200,300)):
                    o6 = True
                    turn_o = False
                    turn_x = True
                if (x in range(100,250)) and (y in range(100,200)):
                    o7 = True
                    turn_o = False
                    turn_x = True
                if (x in range(250,350)) and (y in range(100,200)):
                    o8 = True
                    turn_o = False
                    turn_x = True
                if (x in range(350,500)) and (y in range(100,200)):
                    o9 = True
                    turn_o = False
                    turn_x = True

    keys = pygame.key.get_pressed()
    if keys[K_RETURN] and game_start:
        turn_x = True
        game_start = False
    elif keys[K_ESCAPE]:
        pygame.quit()

    #Draw background
    screen.fill((0,100,0))

    #Board
    pygame.draw.line(screen, white, (100,200), (500,200), 3)
    pygame.draw.line(screen, white, (100,300), (500,300), 3)
    pygame.draw.line(screen, white, (250,100), (250,400), 3)
    pygame.draw.line(screen, white, (350,100), (350,400), 3)

    if turn_x == True:
        turn_o = False
    if turn_o == True:
        turn_x = False

    #Draw X's
    if x1 == True:
        pygame.draw.line(screen, blue, (100,300), (250,400))
        pygame.draw.line(screen, blue, (250,300), (100,400))
    if x2 == True:
        pygame.draw.line(screen, blue, (250,300), (350,400))
        pygame.draw.line(screen, blue, (350,300), (250,400))
    if x3 == True:
        pygame.draw.line(screen, blue, (500,400), (350,300))
        pygame.draw.line(screen, blue, (350,400), (500,300))
    if x4 == True:
        pygame.draw.line(screen, blue, (250,300), (100,200))
        pygame.draw.line(screen, blue, (100,300), (250,200))
    if x5 == True:
        pygame.draw.line(screen, blue, (250,200), (350,300))
        pygame.draw.line(screen, blue, (250,300), (350,200))
    if x6 == True:
        pygame.draw.line(screen, blue, (350,200), (500,300))
        pygame.draw.line(screen, blue, (350,300), (500,200))
    if x7 == True:
        pygame.draw.line(screen, blue, (100,200), (250,100))
        pygame.draw.line(screen, blue, (250,200), (100,100))
    if x8 == True:
        pygame.draw.line(screen, blue, (250,200), (350,100))
        pygame.draw.line(screen, blue, (350,200), (250,100))
    if x9 == True:
        pygame.draw.line(screen, blue, (350,200), (500,100))
        pygame.draw.line(screen, blue, (350,100), (500,200))
		
    #Draw O's
    if o1 == True:
        pygame.draw.circle(screen, red, (175,350), 38, 1)
    if o2 == True:
        pygame.draw.circle(screen, red, (300,350), 38, 1)
    if o3 == True:
        pygame.draw.circle(screen, red, (425,350), 38, 1)
    if o4 == True:
        pygame.draw.circle(screen, red, (175,250), 38, 1)
    if o5 == True:
        pygame.draw.circle(screen, red, (300,250), 38, 1)
    if o6 == True:
        pygame.draw.circle(screen, red, (425,250), 38, 1)
    if o7 == True:
        pygame.draw.circle(screen, red, (175,150), 38, 1)
    if o8 == True:
        pygame.draw.circle(screen, red, (300,150), 38, 1)
    if o9 == True:
        pygame.draw.circle(screen, red, (425,150), 38, 1)
    
    #X victory
    if x1==True and x2==True and x3==True:
      pygame.draw.line(screen, black, (100,350), (500,350), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x4==True and x5==True and x6==True:
      pygame.draw.line(screen, black, (100,250), (500,250), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x7==True and x8==True and x9==True:
      pygame.draw.line(screen, black, (100,150), (500,150), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x1==True and x5==True and x9==True:
      pygame.draw.line(screen, black, (100,400), (500,100), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x3==True and x5==True and x7==True:
      pygame.draw.line(screen, black, (500,400), (100,100), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x1==True and x4==True and x7==True:
      pygame.draw.line(screen, black, (175,400), (175,100), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x2==True and x5==True and x8==True:
      pygame.draw.line(screen, black, (300,400), (300,100), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif x3==True and x6==True and x9==True:
      pygame.draw.line(screen, black, (425,400), (425,100), 2)
      print_text(font1, 300, 0, "X wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
          
    #O victory
    elif o1==True and o2==True and o3==True:
      pygame.draw.line(screen, black, (100,350), (500,350), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o4==True and o5==True and o6==True:
      pygame.draw.line(screen, black, (100,250), (500,250), 2)
      print_text(font1, 300, 0, ") wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o7==True and o8==True and o9==True:
      pygame.draw.line(screen, black, (100,150), (500,150), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o1==True and o5==True and o9==True:
      pygame.draw.line(screen, black, (100,400), (500,100), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o3==True and o5==True and o7==True:
      pygame.draw.line(screen, black, (500,400), (100,100), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o1==True and o4==True and o7==True:
      pygame.draw.line(screen, black, (175,400), (175,100), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o2==True and o5==True and o8==True:
      pygame.draw.line(screen, black, (300,400), (300,100), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()
    elif o3==True and o6==True and o9==True:
      pygame.draw.line(screen, black, (425,400), (425,100), 2)
      print_text(font1, 300, 0, "O wins!!!")
      clock_start = time.clock()
      if seconds - clock_start <= 0:
          pygame.quit()


    if game_start:
        print_text(font2, 120, 470, "PRESS ENTER TO START...", black)
        turn_x = False
        turn_o = False
		
		
      
    pygame.display.update()
            
                
            
            

















            
        

        
