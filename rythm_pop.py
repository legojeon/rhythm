#coding:utf-8
import pygame, sys
from pygame.locals import *
import ctypes  # An included library with Python install.
import random
import os

red = (255,  0,  0)
black = (0, 0, 0,)
green = (0,204,0)

width = 360
height = 640
case = 0
level = 0
nani = [0,0]
#keys = [False, False,False,False]
bars = []
dby = 2  #bar speed
hbxY = 590 #hitbox line Y
hbxH = 10 #hitbox line height
btwidth = 90
btheight = 40
score = 0
ishit = False
lasttime=0
casetime=0
waittime=0
musictime = 0
effects = []
effect=[0,0,0]

imgfolder = 'image' + os.path.sep
sndfolder = 'music' + os.path.sep

bt1=pygame.image.load(imgfolder +"bt1.png")
bt2=pygame.image.load(imgfolder +"bt2.png")
bt3=pygame.image.load(imgfolder +"bt3.png")
spark=pygame.image.load(imgfolder +"spark.png")
bg1=pygame.image.load(imgfolder +"bg1.jpg")
bg2=pygame.image.load(imgfolder +"bg2.jpg")
bg3=pygame.image.load(imgfolder +"bg3.jpg")
bg4=pygame.image.load(imgfolder +"bg4.jpg")
bg5=pygame.image.load(imgfolder +"bg5.jpg")
bg6=pygame.image.load(imgfolder +"bg6.jpg")
bg7=pygame.image.load(imgfolder +"bg7.jpg")
main=pygame.image.load(imgfolder +"main.jpg")
nan=pygame.image.load(imgfolder +"nanido.jpg")
gg=pygame.image.load(imgfolder + "gg.png")

bt = [bt1,bt2,bt3]
bg = [main,bg1,bg2,bg3,bg4,bg5,bg6,bg7]
bgm = ["login.mp3","TT.mp3","sugar.mp3","IF_I.mp3","fire.mp3","LostStars.mp3","ovwatch.mp3","LOL_bgm.mp3","ggyo.mp3"]
bgmtime = [300000,282000,238000,228000,210000,268000,153000,188000]
nanido = [1000,1500,750,1250,500,1000,250,750]

btcol = []
i = []
cnt= 0
for table in range(1000):
	i.append(random.randrange(0,4))
	btcol.append(random.randrange(0,3))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('rhythm2')

pygame.mixer.init()
pygame.mixer.music.load(sndfolder + bgm[0])
pygame.mixer.music.play(-1,0.0)

def barsinit():
	global i,btcol,cnt
	x = i[cnt] * btwidth
	y = 0
	state = True
	bar=[x,y,state,btcol[cnt]]
	bars.append(bar)
	cnt += 1

def drawbar():
	global bars,height,dby,bt,score
	for b in bars:
		if b[2] == True:
			b[1] += dby
			screen.blit(bt[b[3]],(b[0],b[1]))
		if b[1] >= height:
			bars.remove(b)
			score -= 100

def effectsinit():
	global effect,effects
	if effect[0] == 1:
		x= effect[1]+5
		y= effect[2]-25
		tt = pygame.time.get_ticks()
		efe=[x,y,tt]
		effects.append(efe)
		effect[0] = 0

def draweffect():
	global effects
	for e in effects:
		screen.blit(spark,(e[0],e[1]))
		if (pygame.time.get_ticks() - e[2] >= 100):
			effects.remove(e)

def drawHitBox():
	global hbxY,hbxH,width
	pygame.draw.rect(screen, red, [0, hbxY, width, hbxH], 0)

def drawscore(score):
	global black
	scoreFont = pygame.font.Font(None,32)
	scoreText = scoreFont.render("score : " + str(score),0,green)
	screen.blit(scoreText, (5,5))

def DDan(i): #i = 0,1,2,3
	global keys,bars,hbxY,hbxH,btwidth,btheight,height,score,ishit,effect
	hbx = pygame.Rect(i*btwidth, hbxY, btwidth, hbxH)
	ishit = False
	for b in bars:
		if b[0] == i * btwidth:
			objbar = pygame.Rect(b[0],b[1],btwidth,btheight)
			if hbx.colliderect(objbar):
				effect[0] = 1
				effect[1]= b[0]
				effect[2]= b[1]
				ishit = True
				bars.remove(b)
				score += 100
	if ishit == False:
		score -= 100

def levelset(level):
	global bgm,lasttime,musictime,casetime,waittime
	pygame.mixer.init()
	pygame.mixer.music.load(sndfolder +bgm[level])
	pygame.mixer.music.play(-1,0.0)
	lasttime = pygame.time.get_ticks()
	waittime = random.randrange(1000,1500)
	casetime = pygame.time.get_ticks()
	musictime = bgmtime[level]

while True:
	if case == 0:
		screen.blit(bg[0],(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == K_1:
				level = 1
			if event.key == K_2:
				level = 2
			if event.key == K_3:
				level = 3
			if event.key == K_4:
				level = 4
			if event.key == K_5:
				level = 5
			if event.key == K_6:
				level = 6
			if event.key == K_7:
				level = 7
			case = 1
		pygame.display.update()

	if case == 1:
		screen.blit(nan,(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == K_q:
				nani[0] = nanido [0]
				nani[1] = nanido [1]
				levelset(level)
				case = 2
			if event.key == K_w:
				nani[0] = nanido [2]
				nani[1] = nanido [3]
				levelset(level)
				case = 2
			if event.key == K_e:
				nani[0] = nanido [4]
				nani[1] = nanido [5]
				levelset(level)
				case = 2
			if event.key == K_r:
				nani[0] = nanido [6]
				nani[1] = nanido [7]
				levelset(level)
				case = 2
		pygame.display.update()


	if case == 2:
		screen.blit(bg[level],(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == K_h:
					DDan(0)
				elif event.key == K_j:
					DDan(1)
				elif event.key == K_k:
					DDan(2)
				elif event.key == K_l:
					DDan(3)
				elif event.key == K_s:
					musictime = 3

		if (pygame.time.get_ticks() - lasttime >= waittime):
			barsinit()
			lasttime =  pygame.time.get_ticks()
			waittime = random.randrange(nani[0],nani[1])

		if (pygame.time.get_ticks() - casetime >= musictime):
			case = 3
			pygame.mixer.init()
			pygame.mixer.music.load(sndfolder + bgm[8])
			pygame.mixer.music.play(-1,0.0)

		drawscore(score)
		drawbar()
		drawHitBox()
		effectsinit()
		draweffect()
		pygame.display.update()

	if case == 3:
		screen.blit(gg,(0,0))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		drawscore(score)
		pygame.display.update()
