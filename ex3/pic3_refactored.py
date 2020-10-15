import pygame

from pygame.draw import *

pygame.init()

FPS = 10
screen = pygame.display.set_mode((1500, 1500))

BLACK = (0, 0, 0)
sc = screen

rect(sc,(166, 241, 160),(0,350,1500,1500)) #sky
rect(sc,(138, 170, 232),(0,0,1500,350))    #earth




def leggirl(x, y, width, height):
    '''
    Функция рисует ноги девочки на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    line(sc,BLACK,[x-int(30/1500*width),y+int(200/620*height)],[x-int(50/1500*width),y+int(300/620*height)])
    line(sc,BLACK,[x+int(30/1500*width),y+int(200/620*height)],[x+int(50/1500*width),y+int(300/620*height)])         
    line(sc,BLACK,[x-int(50/1500*width),y+int(300/620*height)],[x-int(70/1500*width),y+int(300/620*height)])
    line(sc,BLACK,[x+int(50/1500*width),y+int(300/620*height)],[x+int(70/1500*width),y+int(300/620*height)])           

def handboy(x, y, width, height):
    '''
    Функция рисует руки мальчика на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    line(sc,BLACK,[x+int(203/1500*width),y+int(95/620*height)],[x+int(83/1500*width),y+int(15/620*height)])         
    line(sc,BLACK,[x-int(97/1500*width),y+int(95/620*height)],[x+int(23/1500*width),y+int(15/620*height)])         

def legboy(x, y, width, height):
    '''
    Функция рисует ноги мальчика на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    line(sc,BLACK,[x+int(43/1500*width),y+int(195/620*height)],[x+int(33/1500*width),y+int(295/620*height)])
    line(sc,BLACK,[x+int(63/1500*width),y+int(195/620*height)],[x+int(73/1500*width),y+int(295/620*height)]) 
    line(sc,BLACK,[x+int(13/1500*width),y+int(295/620*height)],[x+int(33/1500*width),y+int(295/620*height)])
    line(sc,BLACK,[x+int(93/1500*width),y+int(295/620*height)],[x+int(73/1500*width),y+int(295/620*height)]) 

def handgirl1(x, y, width, height):
    '''
    Функция рисует руки левой девочки на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    line(sc,BLACK,[x-int(140/1500*width),y+int(100/620*height)],[x-int(5/1500*width),y+int(20/620*height)])         
    line(sc,BLACK,[x+int(145/1500*width),y+int(20/620*height)],[x+int(65/1500*width),y+int(60/620*height)])  
    line(sc,BLACK,[x+int(65/1500*width),y+int(60/620*height)],[x+int(5/1500*width),y+int(20/620*height)])
    
def handgirl2(x, y, width, height):
    '''
    Функция рисует руки правой девочки на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    line(sc,BLACK,[x+int(140/1500*width),y+int(100/620*height)],[x+int(5/1500*width),y+int(20/620*height)])         
    line(sc,BLACK,[x-int(155/1500*width),y+int(20/620*height)],[x-int(75/1500*width),y+int(60/620*height)])  
    line(sc,BLACK,[x-int(75/1500*width),y+int(60/620*height)],[x-int(5/1500*width),y+int(20/620*height)])


def boy(x, y, width, height):
    '''
    Функция рисует мальчика на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    ellipse(screen, (192, 126, 187), (x, y, int(107/1500*width), int(200/620*height)))
    circle(sc,(200,200,200),(x+int(53/1500*width),y-int(35/620*height)),int(40/1500/620*width*height))
    legboy(x, y, width, height)    
    handboy(x, y, width, height)

def girl1(x, y, width, height):
    '''
    Функция рисует левую девочку на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    polygon(sc,(255,0,255),[(x,y),(x-int(50/1500*width),y+int(200/620*height)),(x+int(50/1500*width),y+int(200/620*height))])
    circle(sc,(200,200,200),(x,y-int(30/620*height)),int(40/1500/620*width*height))
    leggirl(x, y, width, height)
    handgirl1(x, y, width, height)

def girl2(x, y, width, height):
    '''
    Функция рисует правую девочку на экране
    x, y - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    polygon(sc,(255,0,255),[(x,y),(x-int(50/1500*width),y+int(200/620*height)),(x+int(50/1500*width),y+int(200/620*height))])
    circle(sc,(200,200,200),(x,y-int(30/620*height)),int(40/1500/620*width*height))
    leggirl(x, y, width, height)
    handgirl2(x, y, width, height)

def icecreamboy(x0, y0, width, height):
    '''
    Функция рисует мороженое у мальчика на экране
    x0, y0 - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    triangle3=[(x0+int(1300/1500*width),y0+int(415/620*height)),(x0+int(1335/1500*width),y0+int(330/620*height)),(x0+int(1285/1500*width),y0+int(330/620*height))]
    polygon(sc,(255,255,0),triangle3)
    circle(sc,(0,0,255),(x0+int(1327/1500*width),y0+int(330/620*height)),int(17/1500/620*width*height))
    circle(sc,(255,255,255),(x0+int(1295/1500*width),y0+int(330/620*height)),int(17/1500/620*width*height))
    circle(sc,(128,0,0),(x0+int(1303/1500*width),y0+int(315/620*height)),int(17/1500/620*width*height))


def icecreamgirl(x0, y0, width, height):
    '''
    Функция рисует мороженое у девочки на экране
    x0, y0 - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    triangle3 = [(x0+int(650/1500*width),y0+int(250/620*height)),(x0+int(670/1500*width),y0+int(180/620*height)),(x0+int(620/1500*width),y0+int(180/620*height))]
    polygon(sc,(255,255,0),triangle3)
    circle(sc,(255,0,0),(x0+int(662/1500*width),y0+int(180/620*height)),int(17/1500/620*width*height))
    circle(sc,(255,255,255),(x0+int(630/1500*width),y0+int(180/620*height)),int(17/1500/620*width*height))
    circle(sc,(128,0,0),(x0+int(638/1500*width),y0+int(165/620*height)),int(17/1500/620*width*height))
    line(sc,(128,0,0),[x0+int(650/1500*width),y0+int(250/620*height)],[x0+int(695/1500*width),y0+int(340/620*height)])

def heart(x0, y0, width, height):
    '''
    Функция рисует воздушный шарик у мальчика на экране
    x0, y0 - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    triangle2 = [(x0+int(100/1500*width),y0+int(320/620*height)),(x0+int(150/1500*width),y0+int(250/620*height)),(x0+int(60/1500*width),y0+int(240/620*height))]
    polygon(sc,(250,0,0),triangle2)
    circle(sc,(250,0,0),(x0+int(84/1500*width),y0+int(235/620*height)),int(23/1500/620*width*height))
    circle(sc,(250,0,0),(x0+int(128/1500*width),y0+int(239/620*height)),int(23/1500/620*width*height))
    line(sc,BLACK,[x0+int(100/1500*width),y0+int(320/620*height)],[x0+int(110/1500*width),y0+int(420/620*height)]) 



def draw(x0, y0, width, height):
    '''
    Функция рисует картинку на экране
    x0, y0 - координаты верхнего левого угла изображения
    width, height - ширина и высота изображения
    '''
    x = x0 + int(1096/1500*width)
    y = y0 + int(325/620*height)
    boy(x0 + int(1096/1500*width), y0 + int(325/620*height), width, height)
    x = x0 + int(207/1500*width)
    y = y0 + int(325/620*height)
    boy(x0 + int(207/1500*width), y0 + int(325/620*height), width, height)
    x = x0 + int(550/1500*width)
    y = y0 + int(320/620*height)
    girl1(x0 + int(550/1500*width), y0 + int(320/620*height), width, height)
    x = x0 + int(850/1500*width)
    y = y0 + int(320/620*height)
    girl2(x0 + int(850/1500*width), y0 + int(320/620*height), width, height)
    icecreamgirl(x0, y0, width, height)
    heart(x0, y0, width, height)
    icecreamboy(x0, y0, width, height)


n = int(input('Введите количество рисунков '))
for i in range (n):
    x0 = int(input('Координата х  '))
    y0 = int(input('Координата y  '))
    width = int(input('Введите ширину изображения  '))
    height = int(input('Введите высоту изображения  '))
    draw(x0, y0, width, height)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()