import pygame
import time
from propervalues import *
from midscreen import *
from Battle import *
from Important import *
from Pokedex import *
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()

#defining images

#defining pokemon images

gardevoir = pygame.image.load('images/Gardevoir.png')
mewtwo = pygame.image.load('images/Mewtwo.png')
arceus = pygame.image.load('images/Arceus.png')
greninja = pygame.image.load('images/Greninja.png')
gengar = pygame.image.load('images/Gengar.png')
electabuzz = pygame.image.load('images/Electabuzz.png')
tyranitar = pygame.image.load('images/Tyranitar.png')
dragonite = pygame.image.load('images/Dragonite.png')
snorlax = pygame.image.load('images/Snorlax.png')
machamp = pygame.image.load('images/Machamp.png')
articuno = pygame.image.load('images/Articuno.png')
weezing = pygame.image.load('images/Weezing.png')
feraligatr = pygame.image.load('images/Feraligatr.png')
meganium = pygame.image.load('images/Meganium.png')
rhydon = pygame.image.load('images/Rhydon.png')
lapras = pygame.image.load('images/Lapras.png')
charizard = pygame.image.load('images/Charizard.png')
darkrai = pygame.image.load('images/Darkrai.png')


gardevoir2 = pygame.image.load('images/Gardevoir2.png')
mewtwo2 = pygame.image.load('images/Mewtwo2.png')
arceus2 = pygame.image.load('images/Arceus2.png')
greninja2 = pygame.image.load('images/Greninja2.png')
gengar2 = pygame.image.load('images/Gengar2.png')
electabuzz2 = pygame.image.load('images/Electabuzz2.png')
tyranitar2 = pygame.image.load('images/Tyranitar2.png')
dragonite2 = pygame.image.load('images/Dragonite2.png')
snorlax2 = pygame.image.load('images/Snorlax2.png')
machamp2 = pygame.image.load('images/Machamp2.png')
articuno2 = pygame.image.load('images/Articuno2.png')
weezing2 = pygame.image.load('images/Weezing2.png')
feraligatr2 = pygame.image.load('images/Feraligatr2.png')
meganium2 = pygame.image.load('images/Meganium2.png')
rhydon2 = pygame.image.load('images/Rhydon2.png')
lapras2 = pygame.image.load('images/Lapras2.png')
charizard2 = pygame.image.load('images/Charizard2.png')
darkrai2 = pygame.image.load('images/Darkrai2.png')

#defining other images

openball = pygame.image.load('images/OpenPokeball.png')
square = pygame.image.load('images/Square.png')
table = pygame.image.load('images/Table.png')
oak = pygame.image.load('images/Oak.png')
pokeball = pygame.image.load('images/Pokeball.png')
logo = pygame.image.load('images/PokemonLogo.png')

#defining sounds

gardevoirso = pygame.mixer.Sound("Sound/Gardevoir.wav")
gengarso = pygame.mixer.Sound("Sound/Gengar.wav")
electabuzzso = pygame.mixer.Sound("Sound/Electabuzz.wav")
tyranitarso = pygame.mixer.Sound("Sound/Tyranitar.wav")
dragoniteso = pygame.mixer.Sound("Sound/Dragonite.wav")
snorlaxso = pygame.mixer.Sound("Sound/Snorlax.wav")
machampso = pygame.mixer.Sound("Sound/Machamp.wav")
articunoso = pygame.mixer.Sound("Sound/Articuno.wav")
weezingso = pygame.mixer.Sound("Sound/Weezing.wav")
feraligatrso = pygame.mixer.Sound("Sound/Feraligatr.wav")
meganiumso = pygame.mixer.Sound("Sound/Meganium.wav")
rhydonso = pygame.mixer.Sound("Sound/Rhydon.wav")
mewtwoso = pygame.mixer.Sound("Sound/Mewtwo.wav")
arceusso = pygame.mixer.Sound("Sound/Arceus.wav")
charizardso = pygame.mixer.Sound("Sound/Charizard.wav")
darkraiso = pygame.mixer.Sound("Sound/Darkrai.wav")
greninjaso = pygame.mixer.Sound("Sound/Greninja.wav")
laprasso = pygame.mixer.Sound("Sound/Lapras.wav")

#defining colors

coffee_brown =((200,190,140))
forest_green = ((0,50,0))
navy_blue = ((0,0,100))
white = ((255,255,255))
blue = ((0,0,255))
green = ((0,255,0))
red = ((255,0,0))
black = ((0,0,0))
orange = ((255,100,10))
yellow = ((255,255,0))
blue_green = ((0,255,170))
marroon = ((115,0,0))
lime = ((180,255,100))
pink = ((255,100,180))
purple = ((240,0,255))
gray = ((127,127,127))
magenta = ((255,0,230))
brown = ((100,40,0))

#defining hard core values

display_width = 1240
display_height = 700
FPS = 10

#defining global variables

go = 0

#defining some variables

font = pygame.font.Font('freesansbold.ttf', 25)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pokemon')

def startscreen():
    pygame.mixer.music.stop()
    pygame.mixer.music.load('Sound/Title.mp3')
    pygame.mixer.music.play(-1)
    quit = False
	
    go = 0
	

    while not quit:
	    mouse = pygame.mouse.get_pos()
	
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    quit = True
		    if event.type == pygame.MOUSEBUTTONDOWN:
			    if 570 < mouse[0] < 670 and 225 < mouse[1] < 275:
				    go = 1
			    if 550 < mouse[0] < 685 and 325 < mouse[1] < 375:
				    go = 2
				
	    if go == 0:
		    gameDisplay.fill(black)
		
		    image(mewtwo, 10, 50)
		    image(logo, 455, 2)
		    image(arceus, 780, 100)
			
		
		    button("Play", 595, 239, white, black, 570, 225, 100, 50, red, white)
		    button("Pokedex", 570, 339, white, black, 550, 325, 135, 50, red, white)
	    
		    pygame.display.update()
			
	    elif go == 1:

		    gameDisplay.fill(black)
		    sound(mewtwoso)
		    sound(arceusso)
		
		    image(mewtwo2, 10, 50)
		    image(logo, 455, 2)
		    image(arceus2, 780, 100)
		
		    button("Play", 595, 239, black, black, 570, 225, 100, 50, white, white)
		    button("Pokedex", 570, 339, white, black, 550, 325, 135, 50, red, white)
	    
		    pygame.display.update()
		    clock.tick(0.1)
			
		    quit = True

	    elif go == 2:
	        quit = True
			
    return go
	    
	
def loop():
    quit = False
	
    pokeselected = []
	
    back = 0
    go = startscreen()
	
    if go == 1:
	    back = midscreen(pokeselected)
    elif go == 2:
	    back = Pokedex(0, 0)
		
    if back == 1:
	    loop()
		
    elif back == 2:
	    back = battle(pokeselected)
	    if back == 1:
	    	loop()



		
		
	    
loop()

