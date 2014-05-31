import pygame

import rgine
import base as base
import menu as menu
import battle as battle
import backpack as backpack
import Combinedv2 as libpkmon
import map as maps

textureSize = 32
ScreenSize = list(map(int, (16*textureSize*1.5, 9*textureSize*1.5)))

screen = pygame.display.set_mode(ScreenSize)

pgbar = rgine.Progressbar((ScreenSize[0]*9//10, ScreenSize[1]*2//10),(0,255,0),250,-50,1)
bsc = base.renderInitScene(ScreenSize, pgbar)

import ctypes
ctypes.windll.user32.MessageBoxW(0, "Close this window to run. ", "Run", 0)


intro_text = rgine.windows.render_text\
	(
			ScreenSize,
		    "CLOSE THIS WINDOW TO RUN!  \n\n"
			"Hit SPACE to show menu.  \n"
			"W, A, S, D: Directions.  \n"
			"Tab: Switch Option (msgbox).  \n"
			"Enter: Confirm the topmost button.  \n",
		    pygame.font.SysFont('Times New Romen', 16),
		    True, (255, 255, 255)
	)

while True:
	try:
		screen.blit(bsc.__next__(), (0, 0))
	except:
		# exit(0)
		break
	screen.blit(intro_text, (0, 0))
	pygame.display.flip()

def LoadMap(uPos):
	global g_cm, world, terrain
	g_cm = mapManager.getMap(uPos)
	world = g_cm.world
	terrain = g_cm.terrain

evt = rgine.Event()
wm = rgine.windows.WindowsManager(ScreenSize)

maps.init(ScreenSize, textureSize)
mapManager = maps.MapManager()
for i in base.maps:
	mapManager.add(maps.Map(*i))

terrain = base.init_terrain("1399339488.terrain", "myTexture.texture", True, textureSize)
terrain.readTextureFromSurface(pygame.image.load("1399339488.jpeg"))
terrain.readTextureProperty("1399648062.textureProperty")
terrain.setProperty(0, 1, 255)
terrain.setProperty(1, 0, 255)
mapManager.add(maps.Map(terrain, (4, 4)))

pManager = base.PlayerManager(libpkmon.player, terrain, base.playerEvent, base.npcs)
pManager.getPlayer().setPos(5+4, 10+4)

LoadMap(pManager.getPlayer().getPos())

npcManager = base.NPCManager()
for i in base.npcs:
	npcManager.new(i[0], i[1], base.npcs[i])

pEventList = []
runningNpcEvent = base.NPC(None, None)

uMenu = menu.init_menu(menu.buttons, menu.inst)
uBackpack = backpack.Backpack(wm, pManager.getPlayer())
uBattle = battle.Battle(uBackpack, wm)
menu.inst[2].setBackpack(uBackpack)

import time
fps = 0
t = time.clock()

direction = []
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
	pManager.setTerrain(terrain)
	pManager.updateEvent(evt, wm)
	x = y = 0

	if not runningNpcEvent.isRunning() and \
			not uMenu.isRunning() and \
			not uBattle.isRunning() and \
			not uBackpack.isRunning():

		if evt.isKeyHit(pygame.K_UP):
			direction.append(pygame.K_UP)
		elif evt.isKeyHit(pygame.K_DOWN):
			direction.append(pygame.K_DOWN)
		elif evt.isKeyHit(pygame.K_LEFT):
			direction.append(pygame.K_LEFT)
		elif evt.isKeyHit(pygame.K_RIGHT):
			direction.append(pygame.K_RIGHT)

		if evt.isKeyUp(pygame.K_UP):
			direction.remove(pygame.K_UP)
		elif evt.isKeyUp(pygame.K_DOWN):
			direction.remove(pygame.K_DOWN)
		elif evt.isKeyUp(pygame.K_LEFT):
			direction.remove(pygame.K_LEFT)
		elif evt.isKeyUp(pygame.K_RIGHT):
			direction.remove(pygame.K_RIGHT)

		if direction:
			if direction[-1] == pygame.K_UP:
				y -= 1
			elif direction[-1] == pygame.K_DOWN:
				y += 1
			elif direction[-1] == pygame.K_LEFT:
				x -= 1
			elif direction[-1] == pygame.K_RIGHT:
				x += 1
			else:
				raise ValueError(direction[-1])
	else:
		direction = []


	# check npc event
	player = pManager.getPlayer()
	player.normalize_pos()
	px, py = player.getPos()
	px+=x; py+=y

	#npc direction calc.
	di = base.DOWN
	if x > 0:
		di = base.LEFT
	elif x < 0:
		di = base.RIGHT
	elif y > 0:
		di = base.UP
		
	for npc, bNpcEvent in npcManager.update(pygame.Rect(rgx[0], rgy[0], rgx[1]-rgx[0], rgy[1]-rgy[0]), (px, py)):
		if bNpcEvent:
			if not runningNpcEvent.isRunning() and npc.init(evt, wm):
				runningNpcEvent = npc
				npc.chgDir(di)
			else:
				runningNpcEvent = base.NPC(None, None)
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
		if not pEventList[-1].init(evt, wm): pEventList.pop()


	# shift world
	x, y = ScreenSize
	px, py = pos
	px -= x/textureSize/2-0.5
	py -= y/textureSize/2-0.5
	world.setShift(px*textureSize, py*textureSize)

	# render gaming world
	screen.blit(world.render_s(), (0, 0))

	# Player events
	for i in pEventList:
		surf, pos = i.render(evt, wm)
		if surf is None:
			i.release(wm)
			pEventList.remove(i)
		else:
			if isinstance(pos, (tuple, list)):
				screen.blit(surf, pos)

	# User Menu
	surf, pos = uMenu.update(evt, wm)
	if surf is not None and pos is None: break

	# Battle
	if evt.isKeyHit(pygame.K_0) and not uBattle.isRunning():
		t1 = libpkmon.Pokemon()
		t1.load(4, 0000+400)
		t2 = libpkmon.Pokemon()
		t2.load(1, 500*9+300)
		t2.load(1, 500)
		p = libpkmon.Player([t2, t1], [], "name", 0, 0)
		uBattle.setFightingObjects(player, p)
		uBattle.init(evt, wm)
	elif evt.isKeyHit(pygame.K_0):
		uBattle.release(wm)
	result = uBattle.render(evt, wm)[1]
	if result is not None and result != 0:
		if result == battle.ATK:
			print("Winner: ATK, %s"%uBattle._atk.getCurrentPokemon().getName())
		elif result == battle.DEF:
			print("Winner: DEF, %s"%uBattle._def.getCurrentPokemon().getName())
		else:
			raise ValueError(result)
		uBattle.release(wm)

	# Backpack
	if evt.isKeyHit(pygame.K_8) and not uBackpack.isRunning():
		uBackpack.setPlayer(pManager.getPlayer())
		uBackpack.init(evt, wm)
	elif evt.isKeyHit(pygame.K_8):
		uBackpack.release(wm)
	result = uBackpack.render(evt, wm)[1]
	if result is not None and result != 0:
		print(result)
		uBackpack.release(wm)

	# WindowsManager should always stay above the world
	for hWnd, msg, surface, pos in wm.DispatchMessage(evt):
		screen.blit(surface, pos)

	# Present
	pygame.display.flip()

	fps += 1
	if time.clock() - t >= 1:
		print(fps/(time.clock()-t))
		fps = 0
		t = time.clock()
pManager.release()

for i in pEventList:
	i.release(wm)
pEventList = []

if runningNpcEvent.isRunning():
	runningNpcEvent.release(wm)

uMenu.release(wm)
uBattle.release(wm)

wm.Release()

pygame.quit()
