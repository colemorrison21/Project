import os
from time import time
from filecmp import cmp

path = "C:/Users/Cole Morrison/Downloads/Project1/images/"
files = os.listdir(path)

lol = []
dups = [files.pop(0)]
image = files[0]
for i in range(len(files)):
    image = files[i]
    lol.append(image)
    lol.append(dups)
    dups = []
    for o in range(len(files) - 1, -1, -1):
        if o + 1 < len(files) and image != files[o + 1]:
            if cmp(path + image, path + files[o + 1], shallow=True):
                dups.append(files[o + 1])
    o = o + 1
i = i + 1
