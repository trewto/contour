import copy
import pygame
from pygame import *
import random
import time 

#COLOR
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
CAL = (111,222,178)
WINDOW_HEIGHT = 20
WINDOW_WIDTH = 20
SIZE = 20
BOX = 700
SHADOW = (192, 192, 192)
WHITE = (255, 255, 255)
LIGHTGREEN = (0, 255, 0 )
GREEN = (0, 200, 0 )
BLUE = (0, 0, 128)
LIGHTBLUE= (0, 0, 255)
RED= (200, 0, 0 )
LIGHTRED= (255, 100, 100)
PURPLE = (102, 0, 102)



rows, cols = (SIZE+1, SIZE+1) 
#arr = [[0]*cols]*rows 
arr = [[0 for i in range(cols)] for j in range(rows)] 
#arr[2][2]=1
#arr[3][6]=1

row_n  = input("Number of row: \n")
col_n  = input("Number of col: \n")
row_n = int(row_n)
col_n = int(col_n)

#for a in range(0,190):
	#x= random.randint(1,SIZE)
	#y= random.randint(1,SIZE)   
#	arr[x][y]=1


for i in range( 1 , row_n+1):
    #print("Input the data for row"+ str(i) + " / " + str(row_n))
    for j in range ( 1, col_n+1):
        print("row "+ str(i) + " col " + str(j)+ "")
        arr[i][j] = i 
        print (str(arr[i][j]))

arr[1][1] = 608.3
arr[1][2] = 617.3 
arr[1][3] = 624.8 
arr[1][4] = 633.1


arr[2][1] = 603.2
arr[2][2] = 607.4 
arr[2][3] = 617.4
arr[2][4] = 627.2


arr[3][1] = 601.7
arr[3][2] = 604.3 
arr[3][3] = 612.5
arr[3][4] = 619.3

arr[4][1] = 507.4
arr[4][2] = 602.3 
arr[4][3] = 608.3
arr[4][4] = 616.7

#x = 2
#if 1<=x<=3: 
    #print ( str(1)) 

for i in range( 1 , row_n+1):
    for j in range ( 1, col_n+1):
        print(str(i)+str(j)+str(arr[i][j])+ " ")
    print("\n")

#print(arr)
parr = [[0 for i in range(cols)] for j in range(rows)] 

def drawline(x,d):
    if row_n > col_n:
        a = row_n
    else: 
        a = col_n 
    width = (BOX - 100)/  a; 
    #print("Width "+ str(width))
    
    for i in range(0,a):
       pygame.draw.line(SCREEN, WHITE, (50+i*width, 50), (50+i*width, BOX-50-width)) 
       pygame.draw.line(SCREEN, WHITE, (50, 50+i*width), (BOX-50-width, 50+i*width)) 
       

    for i in range( 1 , row_n+1):
        for j in range ( 1, col_n+1):
            #print("row "+ str(i) + " col " + str(j)+ "")
            #arr[i][j] = i
            text(str(arr[i][j]), 50+ (j-1)*width, 50 + (i-1)* width)
    
    #finding contour 605 
   # x = 630
   
    if int(d)%2==0:
        COL = RED
    else:
        COL = GREEN
        
    e = int(d)%2; 
    for i in range( 1 , row_n+1):
        for j in range ( 1, col_n+1-1):  

        
            if  arr[i][j]<= x <= arr[i][j+1]:
                #procedure 
                # print("matchfound")
                pygame.draw.circle(SCREEN, COL, (int(50+(j-1)*width+width/2+e*20), int(50 + (i-1)* width)), 8)
                textt(str(x),int(50+(j-1)*width+width/2),int(50 + (i-1)* width))
                
            elif  arr[i][j+1]<= x <= arr[i][j]:
                #procedure 
                #print("matchfound")
                pygame.draw.circle(SCREEN, COL, (int(50+(j-1)*width+width/2+e*20), int(50 + (i-1)* width)), 8)
                a = 1
                textt(str(x),int(50+(j-1)*width+width/2),int(50 + (i-1)* width))
            
          
    for i in range( 1 , row_n+1-1):
        for j in range ( 1, col_n+1):             
            #for row analysis
            if  arr[i][j]<= x <= arr[i+1][j]:
                #procedure 
                # print("matchfound")
                pygame.draw.circle(SCREEN, COL, (int(50+(j-1)*width), int(50 + (i-1)* width+width/2+e*20)), 8)
                textt(str(x), int(50+(j-1)*width+20) , int(50 + (i-1)* width+width/2+ e*20))
            elif  arr[i+1][j]<= x <= arr[i][j]:
                #procedure 
                #print("matchfound")
                pygame.draw.circle(SCREEN, COL, (int(50+(j-1)*width), int(50 + (i-1)* width+width/2+e*20)), 8)
                a = 1
                textt(str(x), int(50+(j-1)*width+20) , int(50 + (i-1)* width+width/2 + e*20))
                
    
    
    
    
def main():
    z=0
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((BOX, BOX))
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    
    d = 1
    rrr = 0 
    while True:
        z= z+1
        d = 1
        SCREEN.fill(BLACK)
        
        
        clist1 = { 600,610,620,630}
        clist2 = { 605,615,625}
        
        if rrr % 2 == 0:
            for p in clist1:
                drawline(p , d)
                d = d +1 ;
        else:
            for p in clist2:
                drawline(p , d)
                d = d +1 ;
        
        #drawing point text
        #text("122.3", 50,50)
        #text in position
     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                rrr = rrr + 1   
            elif 1==1:
                a = 1
                    
     
        pygame.display.update()
        time.sleep(.2)

def text(text,x , y):
    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    text_surface = font.render(str(text), True, RED)
    SCREEN.blit(text_surface, (x,y))
def textt(text,x , y):
    font = pygame.font.Font(pygame.font.get_default_font(), 15)
    text_surface = font.render(str(text), True, WHITE)
    SCREEN.blit(text_surface, (x,y))


main()
