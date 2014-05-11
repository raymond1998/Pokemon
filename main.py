import copy

import pygame

import rgine
import basics as base
import ChiangObjectives as character

textureSize = 32
ScreenSize = (16*textureSize, 9*textureSize)

screen = pygame.display.set_mode(ScreenSize)

pgbar = rgine.Progressbar((ScreenSize[0]*9//10, ScreenSize[1]*2//10),(0,255,0),250,-50,1)
bsc = base.renderInitScene(ScreenSize, pgbar)

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Close this window to run. ", "Run", 0)

while True:
	try:
		screen.blit(bsc.__next__(), (0, 0))
	except:
		# exit(0)
		break
	pygame.display.flip()

terrain = base.init_terrain("1399339488.terrain", "myTexture.texture", True, textureSize)
terrain.readTextureFromSurface(pygame.image.load("1399339488.jpeg"))
terrain.readTextureProperty("1399648062.textureProperty")
terrain.setProperty(0, 1, 255)
terrain.setProperty(1, 0, 255)
world = rgine.TerrainWorld(terrain.width*terrain.textureW, terrain.height*terrain.textureH)
world.setScreenSize(*ScreenSize)
world.setTextureFormat(textureSize, textureSize)
evt = rgine.Event()
wm = rgine.windows.WindowsManager()


pManager = base.PlayerManager(character.player, terrain)
npcManager = base.NPCManager()

for i in base.npcs:
	npcManager.new(i[0], i[1], base.npcs[i])

pEventList = []
while True:
	evt.update()

	if evt.type == pygame.QUIT: break
	screen.fill((0, 0, 0))

	# render terrain to gaming world
	rgx, rgy = world.getTerrainRange()
	rgx, rgy = list(map(int, rgx)), list(map(int, rgy))
	(x0, x1), (y0, y1) = rgx, rgy
	terrain.render_s(world.getSurface(), world.Terrain2World(x0-2, y0-2), range(x0-2, x1+2), range(y0-2, y1+2))


	# check user event
	pManager.updateEvent(evt, wm)
	x = y = 0
	if evt.isKeyDown("w"):
		y -= 1
	elif evt.isKeyDown("s"):
		y += 1
	if not y:
		if evt.isKeyDown("a"):
			x -= 1
		elif evt.isKeyDown("d"):
			x += 1

	# check npc event
	player = pManager.getPlayer()
	player.normalize_pos()
	px, py = player.getPos()
	px+=x; py+=y
	for npc, bNpcEvent in npcManager.update(pygame.Rect(rgx[0], rgy[0], rgx[1]-rgx[0], rgy[1]-rgy[0]), (px, py)):
		if bNpcEvent: pEventList.append(copy.deepcopy(npc))
		surf, pos = npc.render(evt, wm)
		if surf is None:
			npcManager.delete(npc)
		else:
			world.blit(surf, world.Terrain2World(*pos))

	# check player event
	(surf, pos), pEvt, bMoving = pManager.update(x, y)
	world.blit(surf, world.Terrain2World(*pos))

	if pEvt != -1:
		pEventList.append(pEvt[0](*pEvt[1]))
		if not pEvent[-1].init(evt, wm): pEventList.pop()

	# shift world
	x, y = ScreenSize
	px, py = pos
	px -= x/textureSize/2-0.5
	py -= y/textureSize/2-0.5
	world.setInitShift(px*textureSize, py*textureSize)

	# render gaming world
	screen.blit(world.render_s(), (0, 0))

	# Player events
	for i in pEventList:
		surf, pos = i.render(evt, wm)
		if surf is None:
			i.release(wm)
			pEvent.remove(i)
		else:
			screen.blit(surf, pos)

	# WindowsManager should always stay above the world
	for hWnd, msg, surface, pos in wm.DispatchMessage(evt):
		screen.blit(surface, pos)

	# Present
	pygame.display.flip()

for i in pEventList:
	i.release(wm)
pEventList = []

wm.Release()
pygame.quit()
