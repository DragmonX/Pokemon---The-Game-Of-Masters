import pygame, random

pygame.init();

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
blue = (0, 0, 150)

display_width = 800
display_height = 600

font = pygame.font.Font('freesansbold.ttf', 25)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Pokemon')


def message(msg, color, a, b):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [a, b])
	
def writes(msg, color, a, b, size):
    Fonts = pygame.font.Font('freesansbold.ttf', size)
    screen_text = Fonts.render(msg, True, color)
    gameDisplay.blit(screen_text, [a, b])

def button(text, p1, p2, textcolor1, textcolor2, x, y, l, b, color1, color2):
    mouse = pygame.mouse.get_pos()
	
    if x < mouse[0] < x + l and y < mouse[1] < y + b:
	    pygame.draw.rect(gameDisplay, color2, [x, y, l, b])
	    message(text, textcolor2, p1, p2)
		
    else:
	    pygame.draw.rect(gameDisplay, color1, [x, y, l, b])
	    message(text, textcolor1, p1, p2)

def image(image, a, b):
    gameDisplay.blit(image, (a, b))

def sound(sound):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(sound)
	
def sound1(sound):
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.Sound.play(sound)
    pygame.mixer.music.set_volume(1.0)
	
def pokechange(im, im2, x, y, l, b):
    mouse = pygame.mouse.get_pos()
	
    if x < mouse[0] < x + l and y < mouse[1] < y + b:
	    image(im2, x, y)
	    image(im, x, y)
		
    else:
	    image(im, x, y)
	
def number(m, n):
    a = []
	
    k = 0
    i = 0
	
    while i < 6:
	    x = int(round(random.randrange(m, n)/1.0) * 1.0)
		
	    for value in a:
		    if x == value:
			    k = 1
			    break
		    else:
			    k = 0
				
	    if k == 0:
		    a.append(x)
		    i = i + 1
			
    return a