import subprocess
import sys
import math

if __name__ != "__main__":
	print("call me directly!!")
	sys.exit(1)

COMMAND = "./target/release/mandelbrot_rs"
COUNT = 100
ASPECT_RATIO=1.5
SHRINK_RATIO = 0.95
FILESIZE_HEIGHT=10000
START_X = -1.2
START_Y = 0.35

DEFAULT_WIDTH = 0.2
DEFAULT_HEIGHT = -0.15


def processor(file_name, size, upper_left, lower_right):
	print("py -> ", [COMMAND, file_name + ".png", size, upper_left, lower_right])
	subprocess.call([COMMAND, file_name + ".png", size, upper_left, lower_right])
	return

height = DEFAULT_HEIGHT

for i in range(0, 3):
	delta_x = height * ASPECT_RATIO
	delta_y = height
	new_start_x = delta_x / 2 + START_X
	new_start_y = delta_y / 2 + START_Y
	file_name = "./target/{}".format(i)
	size = "{0}x{1}".format(math.floor(FILESIZE_HEIGHT * ASPECT_RATIO), math.floor(FILESIZE_HEIGHT))
	upper_left = "{0},{1}".format(new_start_x, new_start_y)
	lower_right = "{0},{1}".format(new_start_x + height * ASPECT_RATIO, new_start_y - height)
	processor(file_name, size, upper_left, lower_right)
	height *= SHRINK_RATIO

# /home/mandelbrot.rs/target/release/mandelbrot_rs image.png 40000x30000 -1.20,0.35 -1.0,0.20 &