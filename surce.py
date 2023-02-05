import sys, random, argparse
import numpy as np
import math
import os
 
from PIL import Image

def getAverageL(image):
 
    im = np.array(image)
 
    w,h = im.shape
 
    return np.average(im.reshape(w*h))
 
def covertImageToAscii(fileName, cols, scale):
     
    gscale2 = '@%#*+=-:. '
 
    image = Image.open(fileName).convert('L')
 
    W, H = image.size[0], image.size[1]
    print("input image dims: %d x %d" % (W, H))
 
    w = W/cols
 
    h = w/scale
 
    rows = int(H/h)
 
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)
 
    aimg = []
    for j in range(rows):
        y1 = int(j*h)
        y2 = int((j+1)*h)
 
        if j == rows-1:
            y2 = H
 
        aimg.append("")
 
        for i in range(cols):
 
            x1 = int(i*w)
            x2 = int((i+1)*w)
 
            if i == cols-1:
                x2 = W
 
            img = image.crop((x1, y1, x2, y2))
 
            avg = int(getAverageL(img))

            gsval = gscale2[int((avg*9)/255)]
 
            aimg[j] += gsval
    
    return aimg

print("Welcome to ChocolateBar v1.0!")
print(" ")

imgFile = input("FileName: ")

need = int(input("Save to file?(1 - yes, 2 - no): "))
colls = input("Specify columns?(y/n): ")

outFile = "CBoutput.txt"

scale = 0.43

if colls.lower() == "y" or colls.lower() == "yes":
    cols = int(input("Columns: "))
elif colls.lower() == "n" or colls.lower() == "no":
    cols = 80
else:
    print("Error! No such command.")

print('generating ASCII art...')
aimg = covertImageToAscii(imgFile, cols, scale)

if need == 1:
    f = open(outFile, 'w')

    for row in aimg:
        f.write(row + '\n')

    f.close()
    print("ASCII art written to %s" % outFile)
elif need == 2:
    for row in aimg:
        print(row + '\n')
else:
    print("Error! Cant save to file.")

os.system("pause")