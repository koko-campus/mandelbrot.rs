import subprocess
import sys
import math

if __name__ != "__main__":
	print("call me directly!!")
	sys.exit(1)

COMMAND = "./target/release/mandelbrot_rs"
ASPECT_RATIO=1.5 # DEFAULT [1.5]
SHRINK_RATIO = 0.99 # DEFAULT [0.99]
FILESIZE_HEIGHT=1000 # DEFAULT [10000]
START_X = -1.21990088 # DEFAULT [-1.2]
START_Y = 0.335100082 # DEFAULT [0.35]

DEFAULT_WIDTH = 0.2 # DEFAULT [0.2]
DEFAULT_HEIGHT = 0.15 # DEFAULT [0.15]


def processor(file_name, size, upper_left, lower_right):
	#print("py -> ", [COMMAND, file_name + ".png", size, upper_left, lower_right])
	subprocess.Popen([COMMAND, file_name + ".png", size, upper_left, lower_right]) # 非同期実行
	#subprocess.run([COMMAND, file_name + ".png", size, upper_left, lower_right]) # 同期実行
	return

height = DEFAULT_HEIGHT

name = input("enter name...").strip()
os.makedirs("./seeds/{}".format(name)) 

for i in range(0, 1800):
	height =  DEFAULT_HEIGHT * SHRINK_RATIO ** i
	cSize_x = height * ASPECT_RATIO # 横幅
	cSize_y = height # 縦幅
	new_start_x = START_X + ((DEFAULT_WIDTH - cSize_x) / 2) # 左上のx座標
	new_start_y = START_Y - ((DEFAULT_HEIGHT - cSize_y) / 2) # 左上のy座標
	file_name = "./seeds/{}/{}".format(name, str(i).zfill(8))
	size = "{0}x{1}".format(math.floor(FILESIZE_HEIGHT * ASPECT_RATIO), math.floor(FILESIZE_HEIGHT))
	upper_left = "{0},{1}".format(new_start_x, new_start_y)
	lower_right = "{0},{1}".format(new_start_x + cSize_x, new_start_y - cSize_y)
	processor(file_name, size, upper_left, lower_right)

# /home/mandelbrot.rs/target/release/mandelbrot_rs image.png 40000x30000 -1.20,0.35 -1.0,0.20 &