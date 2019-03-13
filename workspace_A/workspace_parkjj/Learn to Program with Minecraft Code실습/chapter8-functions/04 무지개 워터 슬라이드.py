from mcpi.minecraft import Minecraft

block = 35 # 양털 블록
air = 0 # 공기 블록
water = 8 # 물 블록

mc = Minecraft.create()
#player_id = mc.getPlayerEntityId('gasbugs')
pos = mc.player.getTilePos()

# 기준점 세팅
x = pos.x + 1
y = pos.y
z = pos.z

# 워터 슬라이드 블록 생성
def waterSlideBlock(x, y, z, status):
    # 빨간 블록 배치
    mc.setBlocks(x, y, z, x+5, y+2, z, block, status)
    # 아래 공기 블록 배치
    mc.setBlock(x, y, z, air)
    mc.setBlock(x+5, y, z, air)
    # 위 공기 블록 배치
    mc.setBlocks(x+1, y+2, z, x+4, y+2, z, air)
    # 물이 흐를 공간에 공기 블록 배치
    mc.setBlocks(x+2, y+1, z, x+3, y+1, z, air)

for status in range(16):
    # 풀장 블록 생성
    mc.setBlocks(x, y-1, z, x+5, y, z+5, block, status) # 양털 블록 6x6x2
    mc.setBlocks(x+1, y, z+1, x+4, y, z+4, water) # 물 블록 4x4
    # 기준점 재설정
    z += 6
    y += 1
    for i in range(50): # 0,1,2,3,4,5,6~49
        waterSlideBlock(x, y+i//2, z+i, status)
    mc.setBlocks(x+2, y+(49//2)+1, z+48, x+3, y+(49//2)+1, z+49, water)
    # 기준점 복구
    z -= 6
    y -= 1
    # 다음 슬라이드 구성을 위해 x축으로 6만큼 이동
    x += 6