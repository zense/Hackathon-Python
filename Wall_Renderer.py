import pygame
import math

pygame.init()

class surface:
    def __init__(self, pointA, pointB):
        self.pointA = pointA
        self.pointB = pointB


def find_angle(p1, p2):
    angle = 0
    if(p1[0] == p2[0]):
        if(p2[1] <= p1[1]):
            angle = -math.pi/2
        else:
            angle = math.pi/2
    else:
        angle = math.atan((p2[1] - p1[1])/(p2[0] - p1[0]))
        if(p2[0] < p1[0]):
            if(angle <= 0):
                angle += math.pi
            else:
                angle -= math.pi
    return angle


def angle_between(A, B):
    return math.acos((A[1] * B[1] + A[0] * B[0])/math.sqrt(A[1] * A[1] + A[0] * A[0])/math.sqrt(B[1] * B[1] + B[0] * B[0]))


infoObject = pygame.display.Info()  # finding screen resolution
width = infoObject.current_w
height = infoObject.current_w/2

pygame.display.set_caption("Wolfenstein")
screen=pygame.display.set_mode((int(width),int(height)))

playerX = 0
playerY = 0
Thita=0
number_of_surfaces = 4
surfaces = []
hFOV = 90*math.pi/180
vFOV = 90*math.pi/180
circum_radius = 128
height_of_wall = circum_radius/4


pointA = [0,circum_radius]
pointB = [-circum_radius,0]
surfaces.append(surface(pointA, pointB))
pointA = [-circum_radius,0]
pointB = [0,-circum_radius]
surfaces.append(surface(pointA, pointB))
pointA = [0,-circum_radius]
pointB = [circum_radius,0]
surfaces.append(surface(pointA, pointB))
pointA = [circum_radius,0]
pointB = [0,circum_radius]
surfaces.append(surface(pointA, pointB))


clock = pygame.time.Clock()
running = True

while(running):

    clock.tick(60)
    
    screen.fill((255,255,255))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        pressed_keys=pygame.key.get_pressed()
        if pressed_keys[pygame.K_j]:
            Thita-=math.pi/90
            if(Thita<=-math.pi):
                Thita+=2*math.pi
        if pressed_keys[pygame.K_l]:
            Thita+=math.pi/90
            if(Thita>math.pi):
                Thita-=2*math.pi
        if pressed_keys[pygame.K_w] and abs(playerX-math.cos(Thita)*circum_radius/128)+abs(playerY-math.sin(Thita)*circum_radius/128)<circum_radius:
            playerX-=math.cos(Thita)*circum_radius/128
            playerY-=math.sin(Thita)*circum_radius/128
        if pressed_keys[pygame.K_s] and abs(playerX+math.cos(Thita)*circum_radius/128)+abs(playerY+math.sin(Thita)*circum_radius/128)<circum_radius:
            playerX+=math.cos(Thita)*circum_radius/128
            playerY+=math.sin(Thita)*circum_radius/128
        if pressed_keys[pygame.K_a] and abs(playerX-math.sin(Thita)*circum_radius/128)+abs(playerY+math.cos(Thita)*circum_radius/128)<circum_radius:
            playerY+=math.cos(Thita)*circum_radius/128
            playerX-=math.sin(Thita)*circum_radius/128
        if pressed_keys[pygame.K_d] and abs(playerX+math.sin(Thita)*circum_radius/128)+abs(playerY-math.cos(Thita)*circum_radius/128)<circum_radius:
            playerY-=math.cos(Thita)*circum_radius/128
            playerX+=math.sin(Thita)*circum_radius/128
    
    column_number=0
    Alpha=Thita-hFOV/2
    prev_wall=-1;
    while(Alpha<=Thita+hFOV/2):

        Alpha1=Alpha
        if(Alpha>math.pi):
            Alpha1-=2*math.pi
        elif(Alpha<=-math.pi):
            Alpha1+=2*math.pi

        dist_min=-1
        slope=-1
        c=-1
        normal=-1
        distance_from_player=-1
        angle_from_normal=-1
        c=0
        c1=0
        
        for i in surfaces:
            c1+=1
            angle1=find_angle(i.pointA,[playerX,playerY])
            angle2=find_angle(i.pointB,[playerX,playerY])
            intercept=False
            if(abs(angle1-angle2)<math.pi):
                if( ( Alpha1>angle1 and Alpha1<angle2 )or( Alpha1<angle1 and Alpha1>angle2 ) ):
                    intercept=True
            else:
                if(angle1>0):
                    if(Alpha1>angle1 or Alpha1<angle2):
                        intercept=True
                else:
                    if(Alpha1>angle2 or Alpha1<angle1):
                        intercept=True
            if(intercept):
                if(intercept):
                    if( not i.pointB[0]==i.pointA[0] ):
                        slope= ( i.pointB[1]-i.pointA[1] )/( i.pointB[0]-i.pointA[0] )
                    else:
                        slope="Inf"
                    if(slope=="Inf"):
                        c="Inf"
                    else:
                        c=i.pointA[1]-slope*i.pointA[0]
                    temp_vect1=[math.cos(Alpha1),math.sin(Alpha1)]
                    temp_vect2=[]
                    if(slope==0):
                        if(i.pointA[1]>playerY):
                            temp_vect2=[0,1]
                        else:
                            temp_vect2=[0,-1]
                    elif(slope=="Inf"):
                        if(i.pointA[0]>playerX):
                            temp_vect2=[1,0]
                        else:
                            temp_vect2=[-1,0]
                    else:
                        temp_vect2=[1,-1/slope]
                    angle_from_normal=angle_between(temp_vect1,temp_vect2)
                    if(slope=="Inf"):
                        normal=abs(i.pointA[0] - x)
                        distance_from_player=normal/abs(math.cos((angle_from_normal)))
                    else:
                        normal=abs((slope*playerX-playerY+c)/math.sqrt(slope*slope+1))
                        distance_from_player=normal/abs(math.cos((angle_from_normal)))
                    if(dist_min>=0):
                        if(distance_from_player<dist_min):
                        	dist_min=distance_from_player
                        	c=c1
                    else:
                        dist_min=distance_from_player
                        c=c1
        if(dist_min<=0 or dist_min>256):
            brightness=255
            height_of_drawn_column=0
        else:
            brightness=255-dist_min
            height_of_drawn_column=height*(height_of_wall/2/dist_min)
        if(prev_wall==-1):
            prev_wall=c
        pygame.draw.line(screen,(256-brightness,0,0),((column_number),(height/2-10-height_of_drawn_column)),((column_number),(height/2-height_of_drawn_column)),int(width*math.pi/1800/hFOV)+1)
        pygame.draw.line(screen,(0,brightness,0),((column_number),(height/2-height_of_drawn_column)),((column_number),(height/2+height_of_drawn_column)),int(width*math.pi/1800/hFOV)+1)
        pygame.draw.line(screen,(256-brightness,0,0),((column_number),(height/2+10+height_of_drawn_column)),((column_number),(height/2+height_of_drawn_column)),int(width*math.pi/1800/hFOV)+1)
        if(not prev_wall==c):
        	pygame.draw.line(screen,(256-brightness,0,0),((column_number),(height/2-height_of_drawn_column)),((column_number),(height/2+height_of_drawn_column)),10)
        	prev_wall=c
        column_number+=width*math.pi/1800/hFOV
        
        Alpha+=math.pi/1800
    pygame.display.update()
