from mcpi.minecraft import Minecraft

oak_stair_East = (53, 0) # 참나무 계단 블록(동)
oak_stair_West = (53, 1) # 참나무 계단 블록(서)
oak_stair_South = (53, 2) # 참나무 계단 블록(남)
oak_stair_North = (53, 3) # 참나무 계단 블록(북)
oak_wood_plank = (5,0) # 참나무 목재
length = 4 # 계단 길이

mc = Minecraft.create()
#player_id = mc.getPlayerEntityId('gasbugs')
pos = mc.player.getTilePos()

# 기준점 세팅
x = pos.x + 1
y = pos.y - 1 # 지면부터 시작
z = pos.z

for status in range(16): # 나선형 반복을 16회
    mc.setBlock(x, y, z, oak_wood_plank) # 모서리 블록
    for i in range(length): # x+1, y+1, S:0
        x += 1
        y += 1
        mc.setBlock(x, y, z, oak_stair_East)
    x += 1
    mc.setBlock(x, y, z, oak_wood_plank) # 모서리 블록
    for i in range(length): # z+1, y+1, S:2
        z += 1
        y += 1
        mc.setBlock(x, y, z, oak_stair_South)
    z += 1
    mc.setBlock(x, y, z, oak_wood_plank) # 모서리 블록
    for i in range(length): # x-1, y+1, S:1
        x -= 1
        y += 1
        mc.setBlock(x, y, z, oak_stair_West)
    x -= 1
    mc.setBlock(x, y, z, oak_wood_plank) # 모서리 블록
    for i in range(length): # z-1, y+1, S:3
        z -= 1
        y += 1
        mc.setBlock(x, y, z, oak_stair_North)
    z -= 1