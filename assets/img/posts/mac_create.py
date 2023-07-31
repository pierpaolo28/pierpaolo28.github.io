import subprocess
import os
import sys
import signal

args = list(sys.argv)

photos = args[1]
photo, type = args[1].split('.')

os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 2000 " + str(photo) + "." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 2000 " + str(photo) + "_lg." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 1000 " + str(photo) + "_md." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 768 " + str(photo) + "_sm." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 575 " + str(photo) + "_xs." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 256 " + str(photo) + "_placehold." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 535 " + str(photo) + "_thumb." + str(type))
os.system("magick -verbose " + str(photos) + " -background white -flatten -resize 1070 " + str(photo) + "_thumb@2x." + str(type))