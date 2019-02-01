import math

grid=((True,True,True,True,True,True,True,True),
      (True,False,True,False,False,False,False,True),
      (True,False,False,False,False,True,False,True),
      (True,False,False,False,False,True,False,True),
      (True,False,False,False,False,False,False,True),
      (True,False,False,False,True,True,True,True),
      (True,True,False,False,False,False,False,True),
      (True,True,True,True,True,True,True,True))
direc=math.pi/3
cords=(2.0,2.0)
d = [0 for i in range(500)]
shades = [0 for i in range(500)]
h = 1

for i in range(250,-250,-1):
    a=math.atan2(i,250)+direc
    y=math.sin(a)/abs(math.cos(a)) if math.cos(a) != 0 else 1000000*math.sin(a)
    x=math.cos(a)/abs(math.sin(a)) if math.sin(a) != 0 else 1000000*math.cos(a)
    cx=list(cords)
    cy=list(cords)
    while 0<=cx[0]<=len(grid)-1 and 1<=cx[1]<=len(grid[0])-2 and not grid[int(math.floor(cx[0]))][int(cx[1] if y > 0 else cx[1]-1)]:
        cx[0]+=x
        cx[1]+=1 if y > 0 else -1
    dx = cx[0]*cx[0] + cx[1]*cx[1]
    
    while 1<=cy[0]<=len(grid)-2 and 0<=cy[1]<=len(grid[0])-1 and not grid[int(cy[0] if x > 0 else cy[0]-1)][int(math.floor(cy[1]))]:
        cy[0]+=1 if x > 0 else -1
        cy[1]+=y
    dy = cy[0]*cy[0] + cy[1]*cy[1]
    
    if dx < dy:
        d[250-i] = math.sqrt(dx)
        shades[250-i] = math.sqrt( (math.floor(cx[0])+0.5)*(math.floor(cx[0])+0.5) + (cx[1]+0.5 if y > 0 else cx[1]-0.5)*(cx[1]+0.5 if y > 0 else cx[1]-0.5) )
    else:
        d[250-i] = math.sqrt(dy)
        shades[250-i] = math.sqrt( (cy[0]+0.5 if x > 0 else cy[0]-0.5)*(cy[0]+0.5 if x > 0 else cy[0]-0.5) + (math.floor(cy[1])+0.5)*(math.floor(cy[1])+0.5) )
        
#print(d)
#print(shades)
txt = "P3 500 500 255\n\n"
for r in range(500):
    for c in range(500):
        if (r-250)*(r-250) < h * (250*250 + (c-250)*(c-250)) / d[c]:
            for i in range(3):
                txt += str(int(math.floor(128*shades[c]/10 + 128))) + " "
        else:
            txt += "0 0 0 "
    txt += "\n"
f = open("things.ppm", "w")
f.write(txt)
f.close()
