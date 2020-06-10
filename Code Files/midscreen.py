import pygame, random
import time
from propervalues import *
from Important import *
from Pokedex import *

pygame.init()

#defining pokemon images
dialga = pygame.image.load('images/Dialga.png')
raikou = pygame.image.load('images/Raikou.png')
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

dialga2 = pygame.image.load('images/Dialga2.png')
raikou2 = pygame.image.load('images/Raikou2.png')
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
buton = pygame.image.load('images/Button.png')
pressed = pygame.image.load('images/ButtonPressed.png')
rigid = pygame.image.load('images/RigidSquare.png')
buton2d = pygame.image.load('images/Button2d.png')
hovered2d = pygame.image.load('images/Button2dHover.png')
pressed2d = pygame.image.load('images/Button2dPressed.png')

#defining sounds

dialgaso = pygame.mixer.Sound("Sound/Dialga.wav")
raikouso = pygame.mixer.Sound("Sound/Raikou.wav")
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

def midscreen(pokeselected):
    quit = False
    pygame.mixer.music.load('Sound/page2.mp3')
    pygame.mixer.music.play(-1)
	
    k = 0
    z = 0
    back = 0
    but = 0
    selected = [-1, -1, -1, -1, -1, -1]
    total = 0
    goto = 0
    moveselected = 0
    dex = 0

    values = number(0, 27)

    while not quit:
	    mouse = pygame.mouse.get_pos()
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    quit = True
		    if event.type == pygame.MOUSEBUTTONDOWN:
			    if 330 < mouse[0] < 429 and 255 < mouse[1] < 354 and k != 1:
				    moveselected = 0
				    k = 1
				    z = 1
			    elif 790 < mouse[0] < 889 and 255 < mouse[1] < 354 and k != 2:
				    moveselected = 0
				    k = 2
				    z = 1
			    elif 455 < mouse[0] < 554 and 175 < mouse[1] < 274 and k != 3:
				    moveselected = 0
				    k = 3
				    z = 1
			    elif 650 < mouse[0] < 749 and 175 < mouse[1] < 274 and k != 4:
				    moveselected = 0
				    k = 4
				    z = 1
			    elif 455 < mouse[0] < 554 and 305 < mouse[1] < 404 and k != 5:
				    moveselected = 0
				    k = 5
				    z = 1
			    elif 650 < mouse[0] < 749 and 305 < mouse[1] < 404 and k != 6:
				    moveselected = 0
				    k = 6
				    z = 1
			    elif 1140 < mouse[0] < 1240 and 650 < mouse[1] < 700:
				    back = 1
				    quit = True
			    elif 560 < mouse[0] < 659 and 240 < mouse[1] < 339 and k != 0 and total < 3 and selected[k - 1] < 0:
				    moveselected = 0
				    but = 1
				    selected[k - 1] = total
				    total = total + 1
				    k = 0
			    elif 770 < mouse[0] < 869 and 580 < mouse[1] < 679:
				    i = 0
				    goto = 0
				    for elements in selected:
					    if elements >= 0:
						    selected[i] -= 1

					    i += 1
						
				    total -= 1
			    elif 879 < mouse[0] < 978 and 580 < mouse[1] < 679:
				    i = 0
				    goto = 0
				    for elements in selected:
					    if elements == 1:
						    selected[i] = -1
					    elif elements == 2:
						    selected[i] -= 1
					    i += 1
							
				    total -= 1
			    elif 988 < mouse[0] < 1087 and 580 < mouse[1] < 679:
				    i = 0
				    goto = 0
				    for elements in selected:
					    if elements == 2:
						    selected[i] = -1

					    i += 1
							
				    total -= 1
			    elif 740 < mouse[0] < 838 and 5 < mouse[1] < 103 and goto == 1:
				    goto = 2
			    elif 900 < mouse[0] < 1230 and 60 < mouse[1] < 160 and k != 0:
				    moveselected = 1
			    elif 900 < mouse[0] < 1230 and 180 < mouse[1] < 280 and k != 0:
				    moveselected = 2
			    elif 900 < mouse[0] < 1230 and 300 < mouse[1] < 400 and k != 0:
				    moveselected = 3
			    elif 900 < mouse[0] < 1230 and 420 < mouse[1] < 520 and k != 0:
				    moveselected = 4
			    elif 0 < mouse[0] < 200 and 650 < mouse[1] < 700 and k != 0 and selected[k - 1] < 0:
			    	Pokedex(values[k - 1], 1)

					
	    if total == 3 and goto != 2:
		    goto = 1
		
	    gameDisplay.fill(blue)
	    pygame.draw.rect(gameDisplay, black, [0, 0, 610, 700])
	    button("Back", 1160, 665, white, black, 1140, 650, 100, 50, black, white)
	
	    image(rigid, 770, 580)
	    image(rigid, 879, 580)
	    image(rigid, 988, 580)
		
	    button(" MOVES ", 1010, 10, red, red, 890, 0, 350, 550, green, green)
		
	    if k != 0 and selected[k - 1] < 0:
		    if z == 1:
			    sound1(poke[int(values[k - 1])].music)
			    z = 0
		    poke[int(values[k - 1])].draw(5, 10)
		    button(" %s " % poke[int(values[k - 1])].name, 125, 520, white, white, 90, 490, 100, 50, black, black)
			
		    a = 10
		    b = 585
		
		    for types in poke[int(values[k - 1])].type:
			    button(type[types - 1].name, a  + 10, b + 10, type[types - 1].textcolor, type[types - 1].textcolor, a, b, 120, 50, type[types - 1].color, type[types - 1].color) 
			    a = a + 130
				
		    a = 0		
		    b = 60
		
		    while a < 4:
			    button(" %s \n PP: %s " % ( poke[int(values[k - 1])].move[a], move[poke[int(values[k - 1])].move[a]].pp ), 910, b + 10, move[poke[int(values[k - 1])].move[a]].textcolor, move[poke[int(values[k - 1])].move[a]].color, 900, b, 330, 100, move[poke[int(values[k - 1])].move[a]].color, move[poke[int(values[k - 1])].move[a]].textcolor)
			    b = b + 120
			    a = a + 1

		    button("Pokedex", 10, 660, black, white, 0, 650, 200, 50, white, blue)

	    if moveselected != 0:
		    a = poke[int(values[k - 1])].move[moveselected - 1]
		    b = 60 + 120 * (moveselected - 1)

		    button("", 910, b + 10, move[a].textcolor, move[a].textcolor, 900, b, 330, 100, move[a].color, move[a].color)
		    writes("Power: %s" % (move[a].damage), move[a].textcolor, 910, b + 10, 20)
		    writes("Accuracy: %s" % (move[a].accuracy), move[a].textcolor, 910, b + 40, 20)
		    writes("Heal: %s" % (move[a].heal), move[a].textcolor, 910, b + 70, 20)


				
	    for yes in selected:
		    if yes == 0:
			    image(pokeball, 770, 580)
		    elif yes == 1:
			    image(pokeball, 879, 580)
		    elif yes == 2:
			    image(pokeball, 988, 580)
	
	    image(oak, 500, 0)
	    image(table, 320, 230)
		
	    if but == 0:
		    image(buton, 560, 240)
		    writes("Select", red, 590, 260, 15)
	    elif but == 1:
		    image(pressed, 566, 246)
		    but = 0
		
	    if goto == 0:
		    image(buton2d, 740, 5)
	    elif goto == 1:
		    image(hovered2d, 740, 5)
		    message("Tap To Play", white, 715, 108)
	    elif goto == 2:
		    image(pressed2d, 740, 5)
		    for i in range(0, 6):
			    if selected[i] == 0:
				    pokeselected.append(int(values[i]))
					
		    for i in range(0, 6):
			    if selected[i] == 1:
				    pokeselected.append(int(values[i]))
					
		    for i in range(0, 6):
			    if selected[i] == 2:
				    pokeselected.append(int(values[i]))
		
		    quit = True
		    back = 2
		    goto = 1
		
	    if k == 1 and selected[0] < 0:
		    image(openball, 310, 204)
	    elif selected[0] < 0:
		    pokechange(pokeball, square, 330, 255, 99, 99)
			
	    if k == 2 and selected[1] < 0:
		    image(openball, 770, 204)
	    elif  selected[1] < 0:
		    pokechange(pokeball, square, 790, 255, 99, 99)
		
	    if k == 3 and selected[2] < 0:
		    image(openball, 435, 124)
	    elif selected[2] < 0:
		    pokechange(pokeball, square, 455, 175, 99, 99)
		
	    if k == 4 and selected[3] < 0:
		    image(openball, 630, 124)
	    elif selected[3] < 0:
		    pokechange(pokeball, square, 650, 175, 99, 99)
		
	    if k == 5 and selected[4] < 0:
		    image(openball, 435, 254)
	    elif selected[4] < 0:
		    pokechange(pokeball, square, 455, 305, 99, 99)
		
	    if k == 6 and selected[5] < 0:
		    image(openball, 630, 254)
	    elif selected[5] < 0:
		    pokechange(pokeball, square, 650, 305, 99, 99)
		    
		
	    pygame.display.update()
		
    return back
