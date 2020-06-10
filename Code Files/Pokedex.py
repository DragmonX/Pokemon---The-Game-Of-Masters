import pygame, time
from propervalues import *
from Important import *

pygame.init()

#defining images

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
infernape = pygame.image.load('images/Infernape.png')
giratina = pygame.image.load('images/Giratina.png')
palkia = pygame.image.load('images/Palkia.png')
shaymin = pygame.image.load('images/Shaymin.png')
bisharp = pygame.image.load('images/Bisharp.png')
electivire = pygame.image.load('images/Electivire.png')
lugia = pygame.image.load('images/Lugia.png')

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
infernape2 = pygame.image.load('images/Infernape2.png')
giratina2 = pygame.image.load('images/Giratina2.png')
palkia2 = pygame.image.load('images/Palkia2.png')
shaymin2 = pygame.image.load('images/Shaymin2.png')
bisharp2 = pygame.image.load('images/Bisharp2.png')
electivire2 = pygame.image.load('images/Electivire2.png')
lugia2 = pygame.image.load('images/Lugia2.png')

#defining move images

hand = pygame.image.load('images/ChopHand.png')

#defining other images

openball = pygame.image.load('images/OpenPokeball.png')
square = pygame.image.load('images/Square.png')
table = pygame.image.load('images/Table.png')
oak = pygame.image.load('images/Oak.png')
pokeball = pygame.image.load('images/Pokeball.png')
logo = pygame.image.load('images/PokemonLogo.png')
dexback = pygame.image.load('images/Pokedexback.jpg')

#defining sounds

#defining Pokemon Sounds

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
infernapeso = pygame.mixer.Sound("Sound/Infernape.wav")
giratinaso = pygame.mixer.Sound("Sound/Giratina.wav")
palkiaso = pygame.mixer.Sound("Sound/Palkia.wav")
shayminso = pygame.mixer.Sound("Sound/Shaymin.wav")
bisharpso = pygame.mixer.Sound("Sound/Bisharp.wav")
electivireso = pygame.mixer.Sound("Sound/Electivire.wav")
lugiaso = pygame.mixer.Sound("Sound/Lugia.wav")

#defining colors

coffee_brown =((200,190,140))
forest_green = ((0,50,0))
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
navy_blue = ((0,0,100))
imageremoval = (0, 0, 0, 0)

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

transparent = pygame.Surface((1240, 700))
transparent.set_alpha(168)

def Pokedex(pokeindex, val):
	ind = pokeindex

	quit = 0

	while not quit:
		mouse = pygame.mouse.get_pos();
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = 1

			elif event.type == pygame.MOUSEBUTTONDOWN:
				if 1140 < mouse[0] < 1240 and 655 < mouse[1] < 700:
					ind = (ind + 1) % 26
				elif 1185 < mouse[0] < 1212 and 5 < mouse[1] < 32:
					quit = 2

		if val == 1:
			transparent.fill(black)
			gameDisplay.blit(transparent, (0, 0))

		else:
			gameDisplay.fill(black)
			
		button("X", 1190, 7, white, black, 1185, 5, 27, 27, red, white)

		poke[int(ind)].draw(5, 10)
		button(" %s " % poke[int(ind)].name, 125, 520, white, white, 90, 490, 100, 50, black, black)

		a = 10
		b = 600
		
		for types in poke[int(ind)].type:
			button(type[types - 1].name, a  + 10, b + 10, type[types - 1].textcolor, type[types - 1].textcolor, a, b, 120, 50, type[types - 1].color, type[types - 1].color) 
			a = a + 130

		writes("Stats", white, 950, 30, 25)

		writes("Attack ", red, 850, 75, 26)
		writes("Defence ", white, 850, 125, 26)
		writes("Speed ", blue, 850, 175, 26)

		att = poke[int(ind)].attack
		defe = poke[int(ind)].defence
		sp = poke[int(ind)].speed

		button(" %s " % att, 980, 76, white, white, 985, 74, int((att / 154) * 200), 28, orange, orange)
		button(" %s " % defe, 980, 126, white, white, 985, 124, int((defe / 154) * 200), 28, orange, orange)
		button(" %s " % sp, 980, 176, white, white, 985, 174, int((sp / 154) * 200), 28, orange, orange)

		button("Next", 1155, 663, white, black, 1140, 655, 100, 40, green, white)

		pygame.display.update()

	return (quit - 1)

def dex():
	pos = []

	quit = 0

	while not quit:
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				quit = 1
			elif event.type == pygame.MOUSEBUTTONDOWN:
				quit = 0

		gameDisplay.fill(blue)

		image(dexback, 0, 0)

		x = 50
		x = int(x)

		y = 50
		y = int(y)

		index = 0
		index = int(index)

		while y + 130 <= 650 and index < 27:
			image(pokeball, x, y)
			writes("%s" % poke[index].name, yellow, x + 8, y + 110, 20)

			if x + 320 <= 1230:
				x += 190
			else:
				x = 50
				y += 180

			index += 1

		pygame.display.update()