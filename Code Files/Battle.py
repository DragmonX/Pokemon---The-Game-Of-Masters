import pygame, random
import time
from propervalues import *
from Important import *

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

background1 = pygame.image.load('images/Background.jpg')
background2 = pygame.image.load('images/Background2.jpg')
battleground = pygame.image.load('images/Battleground.png')
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
butred = pygame.image.load('images/RedRectangleButton.png')
butgreen = pygame.image.load('images/GreenRectangleButton.png')
butblue = pygame.image.load('images/BlueRectangleButton.png')
butpurple = pygame.image.load('images/PurpleRectangleButton.png')

#defining pokemon sounds

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

#defining other sounds

supereffect = pygame.mixer.Sound("Sound/SuperEffective.wav")
noteffect = pygame.mixer.Sound("Sound/NotEffective.wav")
normaleffect = pygame.mixer.Sound("Sound/NormalEffective.wav")

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
imageremoval = (0, 0, 0, 0)

#defining hard core values

display_width = 1240
display_height = 700
FPS = 50

#defining global variables

go = 0

#defining some variables

font = pygame.font.Font('freesansbold.ttf', 25)
clock = pygame.time.Clock()

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pokemon')


transparent = pygame.Surface((1240, 700))
transparent.set_alpha(168)

imageremoval = (0, 0, 0, 0)

def moveplay(pokemon1, pokemon2, graphic, player, anim):

    total = sprit[anim].fram
    start = 0

    while start < total:
	    if graphic == 1:
		    image(background1, 0, 0)
			
	    else:
		    image(background2, 0, 0)

	    image(battleground, 815, 230)
	    image(battleground, 25, 460)

	    image(poke[pokemon1].image, 25, 620 - poke[pokemon1].height)
	    image(poke[pokemon2].image2, 820, 410 - poke[pokemon2].height)

	    if player == 2:
		    image(sprit[anim].get_image(start), int(50 + poke[pokemon1].width) / 2, int(1240 - poke[pokemon1].height) / 2)
	    elif player == 1:
		    image(sprit[anim].get_image(start), int(1640 + poke[pokemon2].width) / 2, int(820 - poke[pokemon2].height) / 2)

	    start += 1

	    pygame.display.update()
	    clock.tick(15)


def animation(iv1, iv2, pokemon1, pokemon2, moved, hp1, hp2, changed, percentage1, percentage2, index1, index2, graphic):
    die = 0
	
    effectiveness1 = 1
    effectiveness2 = 1

    stat1 = poke[pokemon1].stats(iv1)
    stat2 = poke[pokemon2].stats(iv2)
	
    harm = int(move[poke[pokemon1].move[moved]].damage * stat1[0] / stat2[1])
    uplife1 = int(move[poke[pokemon1].move[moved]].heal)
	
    if uplife1 != 0:
	    uplife1 = int(move[poke[pokemon1].move[moved]].heal + percentage1[index1])
	
    moved2 = int(round(random.randrange(0, 4) / 1.0) * 1.0) 
	
    harm2 = int(move[poke[pokemon2].move[moved2]].damage * stat2[0] / stat1[1])
	
    uplife2 = int(move[poke[pokemon2].move[moved2]].heal)
	
    hitting1 = move[poke[pokemon1].move[moved]].willhit
    hitting2 = move[poke[pokemon2].move[moved2]].willhit
	
    if uplife2 != 0:
	    uplife2 = int(move[poke[pokemon2].move[moved2]].heal + percentage2[index2])
	
    for weak in poke[pokemon2].weakness:
	    if move[poke[pokemon1].move[moved]].type[0] == weak or poke[pokemon1].move[moved] == 'Judgement':
		    effectiveness1 = 2
		    harm *= 2
			
    for stren in poke[pokemon2].strenghts:
	    if move[poke[pokemon1].move[moved]].type[0] == stren and poke[pokemon1].move[moved] != 'Judgement':
		    effectiveness1 = 0
		    harm = int(harm / 2)
			
    for weak in poke[pokemon1].weakness:
	    if move[poke[pokemon2].move[moved2]].type[0] == weak or poke[pokemon2].move[moved2] == 'Judgement':
		    effectiveness2 = 2
		    harm2 *= 2
			
    for stren in poke[pokemon1].strenghts:
	    if move[poke[pokemon2].move[moved2]].type[0] == stren and poke[pokemon2].move[moved2] != 'Judgement':
		    effectiveness2 = 0
		    harm2 = int(harm2 / 2)
	
    if stat1[2] >= stat2[2] and changed == 0:
	    k = int(percentage2[index2] - ((harm * 380) / hp2))
		
	    if uplife1 != 0:
		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("%s Used %s" % (poke[pokemon1].name, poke[pokemon1].move[moved]), black, 12, 660, 25)
			
		    while percentage1[index1] < uplife1 and percentage1[index1] < 380:
			    percentage1[index1] += 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
				
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
				
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
				
			    pygame.display.update()
			    clock.tick(FPS)
				
	 
	    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
	    writes("%s Used %s" % (poke[pokemon1].name, poke[pokemon1].move[moved]), black, 12, 660, 25)
		
	    if hitting1 != 0 and uplife1 == 0:
		    moveplay(pokemon1, pokemon2, graphic, 1, 0)

		    if effectiveness1 == 2:
			    sound1(supereffect)
		    elif effectiveness1 == 0:
			    sound1(noteffect)
		    else:
			    sound1(normaleffect)

		    move[poke[pokemon1].move[moved]].animating(poke[pokemon1].move[moved], 2)

		    while percentage2[index2] > k and percentage2[index2] > 0:
			    percentage2[index2] -= 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
			
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
					
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
				
			    pygame.display.update()
			
			    clock.tick(FPS)

		    if effectiveness1 == 2:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Super Effective", black, 12, 660, 25)
		    elif effectiveness1 == 0:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Not Very Effective", black, 12, 660, 25)

			
	    if percentage2[index2] == 0:
		    die = 2
			
	    elif uplife2 != 0:
		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("Foe's %s Used %s" % (poke[pokemon2].name, poke[pokemon2].move[moved2]), black, 12, 660, 25)
			
		    while percentage2[index2] < uplife2 and percentage2[index2] < 380:
			    percentage2[index2] += 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
				
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
				
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
				
			    pygame.display.update()
			    clock.tick(FPS)
		
	    elif hitting2 != 0:
		    moveplay(pokemon1, pokemon2, graphic, 2, 0)
		    k = int(percentage1[index1] - ((harm2 * 380) / hp1))
			
		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("Foe's %s Used %s" % (poke[pokemon2].name, poke[pokemon2].move[moved2]), black, 12, 660, 25)
			
		    if effectiveness2 == 2:
			    sound1(supereffect)
		    elif effectiveness2 == 0:
			    sound1(noteffect)
		    else:
			    sound1(normaleffect)
		
		    while percentage1[index1] > k and percentage1[index1] > 0:
			    percentage1[index1] -= 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
				
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
				
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
				
			    pygame.display.update()
			    clock.tick(FPS)
				
		    if effectiveness2 == 2:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Super Effective", black, 12, 660, 25)
		    elif effectiveness2 == 0:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Not Very Effective", black, 12, 660, 25)

	    if percentage1[index1] == 0:
		    die = 1
	
	    
			
    else:
	    k = int(percentage1[index1] - ((harm2 * 380) / hp1))
	
	    if uplife2 != 0:
		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("Foe's %s Used %s" % (poke[pokemon2].name, poke[pokemon2].move[moved2]), black, 12, 660, 25)
			
		    while percentage2[index2] < uplife2 and percentage2[index2] < 380:
			    percentage2[index2] += 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
				
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
				
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
				
			    pygame.display.update()
			    clock.tick(FPS)
	
	    
		
	    if hitting2 != 0:
		    moveplay(pokemon1, pokemon2, graphic, 2, 0)

		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("Foe's %s Used %s" % (poke[pokemon2].name, poke[pokemon2].move[moved2]), black, 12, 660, 25)
		    
		    if effectiveness2 == 2:
			    sound1(supereffect)
		    elif effectiveness2 == 0:
			    sound1(noteffect)
		    else:
			    sound1(normaleffect)
				
		
			
		    while percentage1[index1] > k and percentage1[index1] > 0:
			    percentage1[index1] -= 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
			
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
					
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
			
			    pygame.display.update()
			    clock.tick(FPS)

		    if effectiveness2 == 2:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Super Effective", black, 12, 660, 25)
		    elif effectiveness2 == 0:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Not Very Effective", black, 12, 660, 25)


	    if percentage1[index1] == 0:
		    die = 1
			
	    elif uplife1 != 0:
		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("%s Used %s" % (poke[pokemon1].name, poke[pokemon1].move[moved]), black, 12, 660, 25)

		
		    while percentage1[index1] < uplife1 and percentage1[index1] < 380:
			    percentage1[index1] += 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
				
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
				
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
			
			    pygame.display.update()
			    clock.tick(FPS)
		
	    elif hitting1 != 0:
		    moveplay(pokemon1, pokemon2, graphic, 1, 0)
		    k = int(percentage2[index2] - ((harm * 380) / hp2))
			
		    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
		    writes("%s Used %s" % (poke[pokemon1].name, poke[pokemon1].move[moved]), black, 12, 660, 25)
			
		    if effectiveness1 == 2:
			    sound1(supereffect)
		    elif effectiveness1 == 0:
			    sound1(noteffect)
		    else:
			    sound1(normaleffect)

		    move[poke[pokemon1].move[moved]].animating(poke[pokemon1].move[moved], 2)
		
		    while percentage2[index2] > k and percentage2[index2] > 0:
			    percentage2[index2] -= 1
			    button(poke[pokemon1].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
			    button(poke[pokemon2].name, 415, 240, black, black, 405, 230, 400, 100, white, white)
				
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
			    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])
			
			    if percentage1[index1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[index1], 20])
			    elif percentage1[index1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[index1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[index1], 20])
			
			    if percentage2[index2] > 190:
				    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[index2], 20])
			    elif percentage2[index2] <= 38:
				    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[index2], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[index2], 20])
				
			    writes(" %s " % int((percentage1[index1] * hp1) / 380), black, 755, 470, 25)
			    writes(" %s " % int((percentage2[index2] * hp2) / 380), black, 725, 240, 25)
				
			    pygame.display.update()
			    clock.tick(FPS)

		    if effectiveness1 == 2:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Super Effective", black, 12, 660, 25)
		    elif effectiveness1 == 0:
			    button("", 10, 610, black, black, 0, 650, 600, 50, white, white)
			    writes("It's Not Very Effective", black, 12, 660, 25)
				
	    if percentage2[index2] == 0:
		    die = 2
			
    return die
			
    

def Initial(player, sound):
    if(player == 1):
	    image(pokeball, 176, 491)
	    pygame.display.update()
	    clock.tick(1)
		
	    image(battleground, 25, 460)
		
	    image(openball, 151, 441)
	    pygame.display.update()
	    clock.tick(1)
		
	    sound1(sound)
		
    if(player == 2):
	    image(pokeball, 966, 261)
	    pygame.display.update()
	    clock.tick(1)
		
	    image(battleground, 815, 230)
		
	    image(openball, 941, 211)
	    pygame.display.update()
	    clock.tick(1)
		
	    sound1(sound)

def battle(pokemon1):
    quit = False
	
    pokemon2 = []
    pokemon2 = number(0, 27)
	
    pokemon2.pop()
    pokemon2.pop()
    pokemon2.pop()
	
    pygame.mixer.music.stop()
	
    percentage1 = [380, 380, 380]
    percentage2 = [380, 380, 380]
	
    graphic = int(round(random.randrange(1, 3)/1.0) * 1.0)
	
    iv = number(10, 50)
    iv1 = [iv[0], iv[1], iv[2]]
    iv2 = [iv[3], iv[4], iv[5]]
	
    hp1 = [poke[pokemon1[0]].healthp(iv[0]), poke[pokemon1[1]].healthp(iv[1]), poke[pokemon1[2]].healthp(iv[2])]
    hp2 = [poke[pokemon2[0]].healthp(iv[3]), poke[pokemon2[1]].healthp(iv[4]), poke[pokemon2[2]].healthp(iv[5])]

    battling1 = 0
    battling2 = 0
    click = 0
    attackmove = -1
    pokeswitch = 2
    switching = -1
    pokeb = -1
    die = 0
    pokenumber = 3
    back = 0
    poke1X = 0
    poke1Y = 0
    poke2X = 0
    poke2Y = 0

    if graphic == 1:
	    pygame.mixer.music.load('Sound/Battlesong1.mp3')
	    pygame.mixer.music.play(-1)
		
    else:
	    pygame.mixer.music.load('Sound/Battlesong2.mp3')
	    pygame.mixer.music.play(-1)
	
    while not quit:
	    mouse = pygame.mouse.get_pos()
	    for event in pygame.event.get():
		    if event.type == pygame.QUIT:
			    quit = True
		    if event.type == pygame.MOUSEBUTTONDOWN:
			    if 915 < mouse[0] < 1115 and 430 < mouse[1] < 576 and click == 0:
				    click = 1
			    elif 840 < mouse[0] < 940 and 582 < mouse[1] < 652 and click == 0:
				    click = 2
			    elif 970 < mouse[0] < 1070 and 622 < mouse[1] < 692 and click == 0:
				    click = 3
			    elif 865 < mouse[0] < 1165 and 435 < mouse[1] < 485 and click == 1:
				    click = 0
				    attackmove = 0
			    elif 865 < mouse[0] < 1165 and 505 < mouse[1] < 555 and click == 1:
				    click = 0
				    attackmove = 1
			    elif 865 < mouse[0] < 1165 and 575 < mouse[1] < 625 and click == 1:
				    click = 0
				    attackmove = 2
			    elif 865 < mouse[0] < 1165 and 645 < mouse[1] < 695 and click == 1:
				    click = 0
				    attackmove = 3
			    elif click == 1:
				    click = 0
			    elif 50 < mouse[0] < 149 and 100 < mouse[1] < 199 and click == 2:
				    if battling1 == 0 and percentage1[1] != 0:
					    switching = 1
				    elif percentage1[0] != 0:
					    switching = 0
						
				    pokeb = 1
			    elif 650 < mouse[0] < 749 and 100 < mouse[1] < 199 and click == 2:
				    if battling1 == 2 and percentage1[1] != 0:
					    switching = 1
				    elif percentage1[2] != 0:
					    switching = 2

				    pokeb = 2
			    elif 1180 < mouse[0] < 1207 and 10 < mouse[1] < 37 and click == 2 and die != 1:
				    pokeb = 0
				    click = 0
			    elif 1140 < mouse[0] < 1240 and 650 < mouse[1] < 700 and click == 2 and battling1 != switching and switching != -1:
				    battling1 = switching
				    pokeb = 0
				    pokeswitch = 1
				    click = 0
				    switching = -1
			    elif 480 < mouse[0] < 780 and 200 < mouse[1] < 250 and click >= 3:
				    quit = True
				    back = 1
			    elif 570 < mouse[0] < 650 and 300 < mouse[1] < 350 and click > 3:
				    quit = True
			    elif 620 < mouse[0] < 720 and 300 < mouse[1] < 350 and click == 3:
				    quit = True

				
					
	    if graphic == 1:
		    image(background1, 0, 0)
			
	    else:
		    image(background2, 0, 0)

	    image(battleground, 815, 230)
	    image(battleground, 25, 460)
		
	    if pokeswitch == 2:
		    Initial(1, poke[pokemon1[battling1]].music)
		
	    if pokeswitch != 1 and click <= 1:
		    image(poke[pokemon1[battling1]].image, 25 + poke1X, 620 + poke1Y - poke[pokemon1[battling1]].height)
		    poke1Y = (poke1Y + 10) % 30
		
	
		
	    if pokeswitch == 2:
		    Initial(2, poke[pokemon2[battling2]].music)
		    pokeswitch = 0
			
	    if pokeswitch != 3 and click <= 2:
		    image(poke[pokemon2[battling2]].image2, 820 + poke2X, 410 + poke2Y - poke[pokemon2[battling2]].height)
		    poke2Y = (poke2Y + 10) % 30
		
	    if pokeswitch == 1:
		    Initial(1, poke[pokemon1[battling1]].music)
		    pokeswitch = 0
		    image(poke[pokemon1[battling1]].image, 25, 620 - poke[pokemon1[battling1]].height)
			
	    if pokeswitch == 3:
		    Initial(2, poke[pokemon2[battling2]].music)
		    pokeswitch = 0
		    image(poke[pokemon2[battling2]].image2, 820, 410 - poke[pokemon2[battling2]].height)

	    if attackmove >= 0 or pokeswitch == 1:
		    die = animation(iv1[battling1], iv2[battling2], pokemon1[battling1], pokemon2[battling2], attackmove, hp1[battling1], hp2[battling2], pokeswitch, percentage1, percentage2, battling1, battling2, graphic)
		    attackmove = -1
		    if die == 1 and pokenumber > 1:
			    click = 2
			    pokenumber -= 1
		    elif die == 1 and pokenumber == 1:
			    click = 5
		    elif die == 2 and battling2 != 2:
			    battling2 += 1
			    pokeswitch = 3
		    elif die == 2 and battling2 == 2:
			    click = 4
		
	    if click <= 2:
		    if click <= 1:
			    button(poke[pokemon1[battling1]].name, 445, 470, black, black, 435, 460, 400, 100, white, white)
		
		    button(poke[pokemon2[battling2]].name, 415, 240, black, black, 405, 230, 400, 100, white, white)

		    if click <= 1:
			    pygame.draw.rect(gameDisplay, black, [443, 518, 382, 22])
		    
		    pygame.draw.rect(gameDisplay, black, [413, 288, 382, 22])

		    if click <= 1:
			    if percentage1[battling1] > 190:
				    pygame.draw.rect(gameDisplay, green, [445, 520, percentage1[battling1], 20])
			    elif percentage1[battling1] <= 38:
				    pygame.draw.rect(gameDisplay, red, [445, 520, percentage1[battling1], 20])
			    else:
				    pygame.draw.rect(gameDisplay, yellow, [445, 520, percentage1[battling1], 20])
				
		    if percentage2[battling2] > 190:
			    pygame.draw.rect(gameDisplay, green, [415, 290, percentage2[battling2], 20])
		    elif percentage2[battling2] <= 38:
			    pygame.draw.rect(gameDisplay, red, [415, 290, percentage2[battling2], 20])
		    else:
			    pygame.draw.rect(gameDisplay, yellow, [415, 290, percentage2[battling2], 20])
		
	    if click <= 1:
		    writes(" %s " % int((percentage1[battling1] * hp1[battling1]) / 380), black, 755, 470, 25)
	    if click <= 2:
		    writes(" %s " % int((percentage2[battling2] * hp2[battling2]) / 380), black, 725, 240, 25)


	    if click == 0:
		    image(butred, 915, 430)
		    writes("Fight", black, 970, 485, 40)
			
		    image(butgreen, 840, 582)
		    writes("Pokemon", black, 856, 610, 15)
			
		    image(butpurple, 970, 622)
		    writes("Surrender", black, 983, 652, 14)
			
		    image(butblue, 1100, 582)
		    writes("Bag", black, 1127, 605, 22)

			
	    elif click == 1:
		    a = 0	
		    b = 435
		
		    while a < 4:
			    button(" %s \n PP: %s " % ( poke[int(pokemon1[battling1])].move[a], move[poke[int(pokemon1[battling1])].move[a]].pp ), 875, b + 10, move[poke[int(pokemon1[battling1])].move[a]].textcolor, move[poke[int(pokemon1[battling1])].move[a]].color, 865, b, 300, 50, move[poke[int(pokemon1[battling1])].move[a]].color, move[poke[int(pokemon1[battling1])].move[a]].textcolor)
			    b = b + 70
			    a = a + 1
				
	    elif click == 2:
		    gameDisplay.blit(transparent, (0, 0))
		    transparent.fill(black)
			
		    button("X", 1185, 12, white, black, 1180, 10, 27, 27, black, white)
		
		
			
		    if pokeb == 1:
			    image(openball, 25, 50)
			    poke[pokemon1[switching]].draw(151, 209)
			    pokechange(pokeball, square, 650, 100, 99, 99)
		    elif pokeb == 2:
			    image(openball, 625, 50)
			    poke[pokemon1[switching]].draw(751, 209)
			    pokechange(pokeball, square, 50, 100, 99, 99)
		    else:
			    pokechange(pokeball, square, 50, 100, 99, 99)
			    pokechange(pokeball, square, 650, 100, 99, 99)
				
		    button("Switch", 1150, 665, white, black, 1140, 650, 100, 50, black, white)
			
	    elif click == 3:
		    transparent.fill(red)
		    gameDisplay.blit(transparent, (0, 0))
		    writes("You Surrendered", white, 470, 100, 50)

		    button("Return to main screen", 540, 212, white, black, 530, 200, 300, 50, black, white)
		    button("Quit", 630, 312, white, black, 620, 300, 80, 50, black, white)
			
	    elif click == 4:
		    transparent.fill(blue)
		    gameDisplay.blit(transparent, (0, 0))
		    writes("You Won", white, 520, 100, 50)

		    button("Return to main screen", 490, 212, white, black, 480, 200, 300, 50, black, white)
		    button("Quit", 580, 312, white, black, 570, 300, 80, 50, black, white)
			
	    elif click == 5:
		    transparent.fill(red)
		    gameDisplay.blit(transparent, (0, 0))
		    writes("You Lost", white, 520, 100, 50)

		    button("Return to main screen", 490, 212, white, black, 480, 200, 300, 50, black, white)
		    button("Quit", 580, 312, white, black, 570, 300, 80, 50, black, white)
			
	    pygame.display.update()
	    clock.tick(5)

    return back