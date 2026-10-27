import random
import numpy as np

richtung = [
    (0, -2),
    (-2, 0),
    (2, 0),
    (0, 2)
]

zeile = 19
feld = 19
maze = np.ones((zeile, feld))

start = (1, 1)
maze[1][1] = 0

stack = [start]

while stack:
    x, y = stack[-1]
    posible = richtung

    random.shuffle(posible)

    found_way = False

    for dx, dy in posible:
        nx = x + dx
        ny = y + dy
        if(( zeile - 1 > nx >= 1 and feld -1 > ny >= 1) and maze[nx][ny] == 1):
            maze[x + dx // 2][y + dy // 2] = 0
            maze[nx][ny] = 0
            stack.append((nx, ny))
            found_way = True
            break
    if found_way == False:
        stack.pop()

maze[1][1] = 2
maze[-2][-2] = 3

for zeilen in maze:
    ausgabe = ""
    for feld in zeilen:
        if feld == 1:
            ausgabe += "██"
        elif feld == 2:
            ausgabe += " S"
        elif feld == 3:
            ausgabe += " Z"
        else:
            ausgabe += "  "
    print(ausgabe)

move = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1)
]
pos = [start]




#while pos:
 #   x, y = pos[-1]
  #  moved = False
   # for sx, sy in move:
    #    gx = x + sx
     #   gy = y + sy
      #  if maze[gx, gy] == 0:
       #     pos.append((gx, gy))
        #    moved = True
         #   break
    #if maze[gx, gy] == " Z":
     #   break

#for wx, wy in pos:
 #   maze[wx, wy] = "*"'

print(ausgabe)




        