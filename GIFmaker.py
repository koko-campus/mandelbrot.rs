from fileinput import filename
import glob
from PIL import Image

components = []

pics = glob.glob("./seeds/{}/*.png".format(input("enter name...").strip()))
pics.sort()

for pic in pics:
    print(pic)
for pic in pics:
    img = Image.open(pic)
    components.append(img)

fileName = "fruits/" + input("Enter file name to save...").strip() + ".gif"
print("filename -> {}".format(fileName))

print("started...")

components[0].save(fileName, save_all=True, append_images=components[1:], optimize=False, duration=100, loop=0)

print("ended...")