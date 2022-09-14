import subprocess
import sys
print(__name__)
if __name__ != "__main__":
	print("call me directly!!")
	sys.exit(1)

COMMAND = "./release/mandelbrot_rs {0}.png {1} {2} {3}"
COUNT = 100
ASPECT_RATIO=1.5
SHRINK_RATIO = 0.95
FILESIZE_HEIGHT=10000
START_X = -1.2
START_Y = 0.35

DEFAULT_HEIGHT = -0.15
DEFAULT_WIDTH = 0.2


def processor(command):
	print(command)
	#subprocess.call(command)
	return

width = DEFAULT_WIDTH

for i in range(0, COUNT):
	delta_x = DEFAULT_WIDTH - width
	delta_y = DEFAULT_HEIGHT - width / ASPECT_RATIO
	new_start_x = delta_x / 2 + START_X
	new_start_y = delta_y / 2 + START_Y
	file_name = "target/{}".format(i)
	size = "{0}x{1}".format(FILESIZE_WIDTH, FILESIZE_WIDTH / ASPECT_RATIO)
	upper_left = "{0},{1}".format(new_start_x, new_start_y)
	lower_right = "{0},{1}".format(new_start_x + width, new_start_y - width / ASPECT_RATIO)
	processor(COMMAND.format(file_name, size, upper_left, lower_right))
	width *= SHRINK_RATIO

# /home/mandelbrot.rs/target/release/mandelbrot_rs super_big.png 4000000x3000000 -1.20,0.35 -1.0,0.20 &