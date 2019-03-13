from mcpi.minecraft import Minecraft

sand = 12 # 모래 블록
mc = Minecraft.create()
#player_id = mc.getPlayerEntityId('gasbugs')
pos = mc.player.getTilePos()

# 기준점 세팅
x = pos.x + 1
y = pos.y - 2
z = pos.z

width = 50
for i in range(width//2):
    mc.setBlocks(x+i, y+i, z+i, x+width-i, y+i, z+width-i, sand)