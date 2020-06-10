import pygame, time
from propervalues import *

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

class Pokemon():
    def __init__(self, name, type, move1, move2, move3, move4, picture, picture2, sound, width, height, weakness, strenghts, hp, attack, defence, speed):
	    self.type = type
	    self.name = name
	    self.move = []
	    self.move.append(move1)
	    self.move.append(move2)
	    self.move.append(move3)
	    self.move.append(move4)
	    self.image = picture
	    self.image2 = picture2
	    self.weakness = weakness
	    self.music = sound
	    self.width = width
	    self.height = height
	    self.strenghts = strenghts
	    self.hp = hp
	    self.attack = attack
	    self.defence = defence
	    self.speed = speed
		
    def draw(self, x, y):
	    image(self.image, x, y)
		
    def healthp(self, iv):
	    health = int(2 * self.hp + 2  * iv + 100 + 5)
	    return health
		
    def stats(self, iv):
	    rand = int((random.randrange(85, 100) / 1.0) * 1.0)
	    rand = rand / 100
	
	    mattack = int((2 * self.attack + 2 * iv) * rand + 5)
	    mdefence = int(2 * self.defence + 2 * iv + 5)
	    mspeed = int(2 * self.speed +  2 * iv + 5)
		
	    stat = [mattack, mdefence, mspeed]
	    return stat
		
		
poke = [  Pokemon("Mewtwo", [11],  "Psychic", "Recover", "Aerial Ace", "Shadow Ball", mewtwo2, mewtwo, mewtwoso, 420, 420, [12, 14, 16], [7, 11], 106, 154, 90, 130) 
		, Pokemon("Arceus" ,[1], "Recover", "Judgement", "Swift", "Overheat", arceus, arceus2, arceusso, 272, 384, [], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18], 120, 120, 120, 120)
		, Pokemon("Greninja", [3, 16], "Shadow Ball", "Hydro Pump", "Surf", "Cross Chop", greninja2, greninja, greninjaso, 280, 418, [18, 5, 4, 7, 12], [2, 3, 6, 11, 14, 16, 17], 72, 103, 71, 122)
		, Pokemon("Darkrai", [16], "Dark Void", "Dream Eater", "Recover", "Dark Pulse", darkrai2, darkrai, darkraiso, 361, 400, [7, 12, 18], [11, 14, 16], 70, 135, 90, 125)
		, Pokemon("Charizard", [2, 10], "Flamethrower", "Aerial Ace", "Fire Blast", "Overheat", charizard2, charizard, charizardso, 333, 350, [3, 4, 9, 13], [18, 7, 12, 5, 17, 2], 70, 109, 85, 100)
		, Pokemon("Lapras", [3, 6], "Ice Beam", "Blizzard", "Surf", "Psychic", lapras2, lapras, laprasso, 322, 353, [4, 5, 7, 13], [3, 6], 130, 85, 95, 60)
		, Pokemon("Meganium", [5], "Magical Leaf", "Synthesis", "Razor Leaf", "Hyper Beam", meganium2, meganium, meganiumso, 310, 402, [2, 6, 8, 10, 12], [3, 4, 5], 80, 83, 100, 80)
		, Pokemon("Rhydon", [9, 13], "Horn Drill", "Megahorn", "Earthquake", "Aerial Ace", rhydon2, rhydon, rhydonso, 398, 332, [3, 5, 6, 7, 17], [1, 2, 4, 8, 10, 13], 105, 45, 45, 40)
		, Pokemon("Weezing", [8], "Sludge Bomb", "Smog", "Explosion", "Tackle", weezing, weezing2, weezingso, 300, 257, [11], [5, 7, 12, 18], 65, 90, 120, 60)
		, Pokemon("Feraligatr", [3], "Ice Fang", "Hydro Pump", "Surf", "Ice Beam", feraligatr2, feraligatr, feraligatrso, 352, 407, [4, 5], [2, 3, 6, 17], 85, 105, 100, 78)
		, Pokemon("Machamp", [7], "Cross Chop", "Submission", "Rock Slide", "Karate Chop", machamp, machamp2, machampso, 317, 362, [10, 11, 18], [5, 12, 13, 16], 90, 130, 85, 55)
		, Pokemon("Articuno", [6, 10], "Ice Beam", "Blizzard", "Aerial Ace", "Recover", articuno2, articuno, articunoso, 325, 338, [2, 4, 13, 17], [5, 9, 12], 90, 95, 125, 85)
		, Pokemon("Snorlax", [1], "Body Slam", "Thunder Bolt", "Rock Slide", "Hyper Beam", snorlax2, snorlax, snorlaxso, 337, 337, [7], [14], 160, 110, 110, 30)
		, Pokemon("Dragonite", [10, 15], "Aerial Ace", "Outrage", "Thunder Bolt", "Hyper Beam", dragonite2, dragonite, dragoniteso, 309, 400, [6, 13, 15, 18], [2, 3, 5, 7, 9, 12], 90, 134, 100, 80)
		, Pokemon("Tyranitar", [13, 16], "Crunch", "Earthquake", "Aerial Ace", "Rock Slide", tyranitar2, tyranitar, tyranitarso, 325, 336, [3, 7, 9, 18, 5, 12, 17], [1, 4, 8, 14, 16, 2, 10, 11], 100, 104, 110, 61)
		, Pokemon("Electabuzz", [4], "Thunder", "Thunder Bolt", "Cross Chop", "Shock Wave", electabuzz2, electabuzz, electabuzzso, 397, 397, [9], [4, 10, 17], 65, 95, 85, 105)
		, Pokemon("Gardevoir", [11, 18], "Psychic", "Recover", "Dream Eater", "Hypnosis", gardevoir, gardevoir2, gardevoirso, 299, 406, [8, 14, 15, 17], [7, 11, 16], 65, 125, 115, 80)
		, Pokemon("Gengar", [8, 14], "Psychic", "Sludge Bomb", "Hypnosis", "Shadow Punch", gengar, gengar2, gengarso, 337, 341, [11, 14, 16], [1, 5, 7, 8, 12, 18], 60, 130, 75, 110)
		, Pokemon("Dialga", [15, 17], "Roar Of Time", "Dragon Rush", "Recover", "Ancient Power", dialga, dialga2, dialgaso, 357, 357, [7, 9, 18], [1, 3, 4, 10, 11, 12, 13, 17, 5, 8], 100, 150, 120, 90)
		, Pokemon("Raikou", [4], "Thunder", "Extrasensory", "Crunch", "Signal Beam", raikou, raikou2, raikouso, 344, 292, [9], [4, 10, 17], 90, 115, 100, 115)
		, Pokemon("Infernape", [2, 7], "Flare Blitz", "Flamethrower", "Cross Chop", "Close Combat", infernape2, infernape, infernapeso, 325, 300, [3, 9, 10, 11], [2, 6, 12, 17, 5, 16], 76, 104, 71, 108)
		, Pokemon("Giratina", [14, 15], "Outrage", "Shadow Force", "Earthquake", "Recover", giratina2, giratina, giratinaso, 400, 319, [15, 18, 6, 14, 16], [2, 3, 4, 5, 12, 1, 7, 8], 150, 100, 120, 90)
		, Pokemon("Palkia", [3, 15], "Draco Meteor", "Hydro Pump", "Recover", "Spacial Rend", palkia2, palkia, palkiaso, 350, 350, [15, 18], [2, 3, 17], 90, 150, 120, 100)
		, Pokemon("Shaymin", [5], "Seed Flare", "Energy Ball", "Synthesis", "Psychic", shaymin2, shaymin, shayminso, 200, 200, [2, 6, 12, 10, 8], [3, 4, 5], 100, 100, 100, 100)
		, Pokemon("Bisharp", [16, 17], "Focus Blast", "Guillotine", "Iron Head", "Dark Pulse", bisharp, bisharp2, bisharpso, 283, 400, [2, 7, 9], [5, 14, 15, 16, 1, 10, 13, 17, 8, 11], 65, 125, 100, 70)
		, Pokemon("Electivire", [4], "Thunder", "Thunder Bolt", "Fire Punch", "Giga Impact", electivire, electivire2, electivireso, 349, 350, [9], [4, 10, 17], 75, 123, 85, 95)
		, Pokemon("Lugia", [11, 10], "Dragon Rush", "Recover", "Psychic", "Sky Attack", lugia2, lugia, lugiaso, 350, 277, [4, 6, 13, 14, 15], [5, 7, 9, 11], 106, 90, 154, 110)
		]

#27 Pokemon added
		
class Moves():
    def __init__(self, type, color, textcolor, damage, heal, accuracy, powerpoints, sleep, paralyze):
	    self.type = type
	    self.textcolor = textcolor
	    self.color = color
	    self.damage = damage
	    self.heal = heal
	    self.accuracy = accuracy
	    self.pp = powerpoints
	    self.sleep = sleep
	    self.paralyze = paralyze
		
    def animation(self, x, y):
	    image(self.picture, x, y)
		
    def willhit(self):
	    accu = int((random.randrange(1, 101) / 1.0) * 1.0)
		
	    if accu <= self.accuracy:
		    return 1
	    else:
		    return 0

    def animating(self, name, player):
        if name == "karate chop":
            if player == 1:
                i = 0
                j = 410

                while i < 230:
            	    image(hand, i, j)
            	    hand.fill(imageremoval)

            	    i += 1
            	    clock.tick(100)
            if player == 2:
                i = 790
                j = 180

                while i < 1020:
            	    image(hand, i, j)
            	    hand.fill(imageremoval)

            	    i += 1
            	    clock.tick(100)
		
move =  {  "Psychic":Moves([11], purple, black, 120, 0, 100, 10, 0, 0)
		 , "Recover":Moves([1], brown, white, 0, 190, 100, 20, 0, 0)
		 , "Swift":Moves([1], brown, white, 60, 0, -1, 25, 0, 0)
		 , "Psycho Cut":Moves([11], purple, black, 80, 0, 100, 10, 0, 0)
		 , "Judgement":Moves([1], brown, white, 100, 0, 100, 5, 0, 0)
		 , "Overheat":Moves([2], orange, white, 140, 0, 75, 5, 0, 0)
		 , "Shadow Ball":Moves([14], purple, white, 80, 0, 100, 15, 0, 0)
		 , "Hydro Pump":Moves([3], blue, white, 140, 0, 75, 5, 0, 0)
		 , "Surf":Moves([3], blue, white, 80, 0, 100, 15, 0, 0)
		 , "Cross Chop":Moves([7], red, black, 140, 0, 75, 5, 0, 0)
		 , "Dark Void":Moves([16], black, white, 0, 0, 75, 20, 1, 0)
		 , "Dream Eater":Moves([11], purple, black, 100, 0, 100, 15, 2, 0)
		 , "Dark Pulse":Moves([16], black, white, 80, 0, 100, 15, 0, 0)
		 , "Flamethrower":Moves([2], orange, white, 90, 0, 100, 10, 0, 0)
		 , "Aerial Ace":Moves([10], white, blue, 80, 0, -1, 15, 0, 0)
		 , "Fire Blast":Moves([2], orange, white, 140, 0, 75, 5, 0, 0)
		 , "Ice Beam":Moves([6], navy_blue, blue, 90, 0, 100, 10, 0, 0)
		 , "Blizzard":Moves([6], navy_blue, blue, 140, 0, 100, 5, 0, 0)
		 , "Magical Leaf":Moves([5], forest_green, white, 80, 0, -1, 25, 0, 0)
		 , "Synthesis":Moves([5], forest_green, white, 0, 190, 100, 5, 0, 0)
		 , "Razor Leaf":Moves([5], forest_green, white, 80, 0, 90, 20, 0, 0)
		 , "Hyper Beam":Moves([1], brown, white, 160, 0, 100, 5, 0, 0)
		 , "Horn Drill":Moves([5], yellow, green, 220, 0, 50, 5, 0, 0)
		 , "Megahorn":Moves([5], yellow, green, 100, 0, 100, 10, 0, 0)
		 , "Earthquake":Moves([9], coffee_brown, brown, 100, 0, 100, 10, 0, 0)
		 , "Sludge Bomb":Moves([8], marroon, purple, 80, 0, 100, 10, 0, 0)
		 , "Smog":Moves([8], marroon, purple, 40, 0, 100, 20, 0, 0)
		 , "Explosion":Moves([1], brown, white, 200, 0, 100, 10, 0, 0)
		 , "Tackle":Moves([1], brown, white, 40, 0, 90, 20, 0, 0)
		 , "Ice Fang":Moves([6], navy_blue, blue, 80, 0, 100, 15, 0, 0)
		 , "Submission":Moves([7], red, black, 80, 0, 100, 10, 0, 0)
		 , "Rock Slide":Moves([13], coffee_brown, black, 80, 0, 90, 10, 0, 0)
		 , "Karate Chop":Moves([7], red, black, 40, 0, -1, 20, 0, 0)
		 , "Body Slam":Moves([1], brown, white, 80, 0, 75, 20, 0, 0)
		 , "Thunder Bolt":Moves([4], yellow, white, 80, 0, 100, 15, 0, 0)
		 , "Outrage":Moves([15], red, yellow, 100, 0, 100, 10, 0, 0)
		 , "Crunch":Moves([14], purple, white, 100, 0, 100, 10, 0, 0)
		 , "Thunder":Moves([4], yellow, white, 140, 0, 75, 5, 0, 0)
		 , "Shock Wave":Moves([4], yellow, white, 60, 0, -1, 15, 0, 0)
		 , "Hypnosis":Moves([11], purple, black, 0, 0, 75, 10, 1, 0)
		 , "Shadow Punch":Moves([14], purple, white, 60, 0, -1, 15, 0, 0)
		 , "Roar Of Time":Moves([15], red, yellow, 150, 0, 90, 5, 0, 0)
		 , "Dragon Rush":Moves([15], red, yellow, 100, 0, 85, 10, 0, 0)
		 , "Ancient Power":Moves([13], coffee_brown, black, 60, 0, 100, 5, 0, 0)
		 , "Extrasensory":Moves([11], purple, black, 80, 0, 100, 20, 0, 0)
		 , "Signal Beam":Moves([12], yellow, green, 75, 0, 100, 20, 0, 0)
		 , "Flare Blitz":Moves([2], orange, white, 120, 0, 100, 5, 0, 0)
		 , "Close Combat":Moves([7], red, black, 120, 0, 85, 5, 0, 0)
		 , "Shadow Force":Moves([14], purple, white, 120, 0, 100, 5, 0, 0)
		 , "Draco Meteor":Moves([15], red, yellow, 130, 0, 85, 5, 0, 0)
		 , "Spacial Rend":Moves([15], red, yellow, 100, 0, 100, 5, 0, 0)
		 , "Seed Flare":Moves([5], forest_green, white, 120, 0, 85, 5, 0, 0)
		 , "Energy Ball":Moves([5], forest_green, white, 100, 0, 100, 10, 0, 0)
		 , "Focus Blast":Moves([7], red, black, 120, 0, 85, 5, 0, 0)
		 , "Guillotine":Moves([1], brown, white, 200, 0, 30, 5, 0, 0)
		 , "Iron Head":Moves([17], black, lime, 80, 0, 100, 10, 0, 0)
		 , "Giga Impact":Moves([1], brown, white, 140, 0, 100, 5, 0, 0)
		 , "Fire Punch":Moves([2], orange, white, 80, 0, 100, 20, 0, 0)
		 , "Sky Attack":Moves([10], white, blue, 130, 0, 100, 5, 0, 0)
		}
		
class Type():
    def __init__(self, name, color, textcolor):
	    self.color = color
	    self.textcolor = textcolor
	    self.name = name
		
type = [  Type("Normal", brown, white)
		, Type("Fire", orange, white)
		, Type("Water", blue, white)
		, Type("Electric", yellow, white)
		, Type("Grass", forest_green, white)
		, Type("Ice", navy_blue, blue)
		, Type("Fighting", red, black)
		, Type("Poison", marroon, white)
		, Type("Ground", coffee_brown, brown)
		, Type("Flying", white, blue)
		, Type("Psychic", purple, black)
		, Type("Bug", yellow, green)
		, Type("Rock", coffee_brown, black)
		, Type("Ghost", purple, white)
		, Type("Dragon", red, yellow)
		, Type("Dark", black, white)
		, Type("Steel", black, lime)
		, Type("Fairy", pink, white)
	   ]

class SpriteSheet(object):
    def __init__(self, file_name, x, y, fram, row, col):
	    self.sprite_sheet = pygame.image.load(file_name).convert()
	    self.height = x
	    self.width = y
	    self.fram = fram
	    self.row = row
	    self.col = col

    def get_image(self, num):
	    image = pygame.Surface([self.width, self.height]).convert()

	    y = int(num / self.col) * self.height
	    x = num % self.col * self.width

 
	    image.blit(self.sprite_sheet, (0, 0), (x, y, self.width, self.height))
 
	    image.set_colorkey(black)
 
	    return image

sprit = [  SpriteSheet("images/Explosion.png", 130, 130, 42, 7, 6)
		 , SpriteSheet("images/Thunderbolt.png", 403, 148, 10, 1, 10)
		]
