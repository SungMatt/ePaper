from IT8951.display import AutoEPDDisplay
from IT8951.display import VirtualEPDDisplay
from IT8951 import constants
from PIL import Image
from time import sleep
import os

V_COM = -1.77

def main(path, virtual=False):
    if virtual:
        display = VirtualEPDDisplay(vcom=V_COM)
    else:
        display = AutoEPDDisplay(vcom=V_COM)

    # Make display clear

    display.clear()
    display.frame_buf.paste(0xFF, box=(0, 0, display.width, display.height))
    img = Image.open(path)
    dims = (display.width, display.height)
    img.thumbnail(dims)
    # Align image with bottom of display
    paste_coords = [dims[i] - img.size[i] for i in (0,1)]
    display.frame_buf.paste(img, paste_coords)
    # Display the image
    display.draw_full(constants.DisplayModes.GC16)

def clear_screen():
    display = AutoEPDDisplay(vcom=V_COM)
    display.clear()

def just_image(path, virtual=False):
    if virtual:
        display = VirtualEPDDisplay(vcom=V_COM)
    else:
        display = AutoEPDDisplay(vcom=V_COM)
    display.frame_buf.paste(0xFF, box=(0, 0, display.width, display.height))
    img = Image.open(path)
    dims = (display.width, display.height)
    img.thumbnail(dims)
    # Align image with bottom of display
    paste_coords = [dims[i] - img.size[i] for i in (0,1)]
    display.frame_buf.paste(img, paste_coords)
    # Display the image
    display.draw_full(constants.DisplayModes.GC16)


dir = "images/Wallpaper 1"
filelist = os.listdir(dir)
new_list = list(filter(lambda x: x[-4:] == ".png", filelist)).sort()
new_list.sort()

print(new_list)
for item in new_list:
    proper_item = dir + "/" + item
    main(proper_item)
    sleep(5)

clear_screen()