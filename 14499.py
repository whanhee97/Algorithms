import sys

input = sys.stdin.readline

n,m,x,y,k = map(int,input().split())
Map = []
for _ in range(n):
  Map.append(list(map(int,input().split())))
orders = list(map(int,input().split()))

dice = [0,0,0,0,0,0]
bot = 0
nor = 1
eas = 2
wes = 3
sou = 4
acr = 5

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def move(x,y,dir):
  nx, ny = x, y
  global bot
  global nor
  global eas
  global wes
  global sou
  global acr

  flag = False
  if nx+dx[dir-1] >= 0 and nx+dx[dir-1] < m:
    if ny+dy[dir-1] >= 0 and ny+dy[dir-1] < n:
      nx += dx[dir-1]
      ny += dy[dir-1]
      flag = True
      
  if flag:
    if dir == 1: #동
      tmp = bot
      bot = eas
      eas= acr
      acr = wes
      wes= tmp
    elif dir == 2: #서
      tmp = bot
      bot = wes
      wes = acr
      acr = eas
      eas = tmp
    elif dir == 3: #북
      tmp = bot
      bot = nor
      nor= acr
      acr = sou
      sou = tmp
    else: #남
      tmp = bot
      bot = sou
      sou= acr
      acr = nor
      nor = tmp
    if Map[ny][nx] != 0:
      dice[bot] = Map[ny][nx]    
      Map[ny][nx] = 0
    else:
      Map[ny][nx] = dice[bot]
    print(dice[acr])
  return (nx,ny)  
  
for ord in orders:
  x, y = move(x,y,ord)