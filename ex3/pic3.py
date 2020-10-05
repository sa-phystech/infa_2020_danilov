import pygame

from pygame.draw import *

pygame.init()

FPS = 10
screen = pygame.display.set_mode((1500, 1500))

BLACK = (0, 0, 0)
sc = screen

rect(sc,(166, 241, 160),(0,350,1500,1500)) #sky
rect(sc,(138, 170, 232),(0,0,1500,350))    #earth



line(sc,BLACK,[520,520],[500,620])
line(sc,BLACK,[580,520],[600,620])         #legs left woman

line(sc,BLACK,[820,520],[800,620])
line(sc,BLACK,[880,520],[900,620])          #legs right woman

line(sc,BLACK,[250,520],[240,620])
line(sc,BLACK,[270,520],[280,620])          #legs left man

line(sc,BLACK,[1140,520],[1120,620])
line(sc,BLACK,[1160,520],[1180,620])        #legs right man

line(sc,BLACK,[1100,620],[1120,620])
line(sc,BLACK,[1200,620],[1180,620])         #right man little legs

line(sc,BLACK,[220,620],[240,620])
line(sc,BLACK,[300,620],[280,620])        #left man little legs

line(sc,BLACK,[500,620],[480,620])
line(sc,BLACK,[600,620],[620,620])           #left girl little legs

line(sc,BLACK,[920,620],[900,620])
line(sc,BLACK,[780,620],[800,620])            #right girl little legs


polygon(sc,(255,0,255),[(550,320),(500,520),(600,520)])
polygon(sc,(255,0,255),[(850,320),(800,520),(900,520)])

ellipse(screen, (192, 126, 187), (207, 325, 107, 200))
ellipse(screen, (192, 126, 187), (1096, 325, 107, 200))

circle(sc,(200,200,200),(260,290),40)
circle(sc,(200,200,200),(550,290),40)
circle(sc,(200,200,200),(850,290),40)
circle(sc,(200,200,200),(1150,290),40)

line(sc,BLACK,[410,420],[290,340])         #left hand left man

line(sc,BLACK,[410,420],[545,340])         #right hand left woman

line(sc,BLACK,[1300,420],[1180,340])       #left hand right man

line(sc,BLACK,[990,420],[855,340])         #left hand right woman

line(sc,BLACK,[110,420],[230,340])         #right hand left man

line(sc,BLACK,[990,420],[1120,340])        #right hand right man
line(sc,BLACK,[775,380],[845,340])

line(sc,BLACK,[695,340],[775,380])          #right hand right woman
line(sc,BLACK,[615,380],[555,340])

line(sc,BLACK,[695,340],[615,380])          #left hand left woman



triangle3 = [(650,250),(670,180),(620,180)]
polygon(sc,(255,255,0),triangle3)
circle(sc,(255,0,0),(662,180),17)
circle(sc,(255,255,255),(630,180),17)
circle(sc,(128,0,0),(638,165),17)
line(sc,(128,0,0),[650,250],[695,340])         #ice cream woman



triangle3=[(1300,415),(1335,330),(1285,330)]
polygon(sc,(255,255,0),triangle3)
circle(sc,(0,0,255),(1327,330),17)
circle(sc,(255,255,255),(1295,330),17)
circle(sc,(128,0,0),(1303,315),17)           #ice cream man



triangle2 = [(100,320),(150,250),(60,240)]
polygon(sc,(250,0,0),triangle2)
circle(sc,(250,0,0),(84,235),23)
circle(sc,(250,0,0),(128,239),23)
line(sc,BLACK,[100,320],[110,420])              #heart

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()