from PIL import ImageGrab
import os

im = ImageGrab.grab()

cwd = os.getcwd()
im.save(cwd + '/tmp.png','png')