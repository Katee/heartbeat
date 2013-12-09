FFMPEG_BIN = "ffmpeg"
videofile = "heartbeat.mp4"

import subprocess as sp
import numpy

pipe = sp.Popen([ FFMPEG_BIN, "-i", videofile,
                   "-f", "image2pipe", "-pix_fmt", "rgb24",
                   "-vcodec", "rawvideo", "-"],
                   stdout = sp.PIPE)

raw_image = pipe.stdout.read(420*360*3) # read 420*360*3 bytes (= 1 frame)
image =  numpy.fromstring(raw_image, dtype='uint8').reshape((360,420,3))

