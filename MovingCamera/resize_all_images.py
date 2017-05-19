# This script reads all of the files in ./train
# and resizes all .png files to be 480 x 360
#
###  Input:  .png files in ./train
###  Output: .png files resized to 480 x 360

import os
import re
from PIL import Image

def resizeImage(filename):
  im_in = Image.open(filename)
  # adjust width and height to your needs
  width = 480
  height = 360
  # use one of these filter options to resize the image
  print filename
  im_out = im_in.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
  im_out.save(filename)


png_pattern = re.compile(".png")

cwd = os.getcwd()

for filename in sorted(os.listdir(cwd + "/train")):
  if png_pattern.search(filename) is not None:
    print "found .png match: " + filename
    resizeImage(cwd + "/train/" + filename)
