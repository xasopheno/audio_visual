import cv2
import numpy as np
import random
import time
import math
import os
# from multiprocessing import Pool

totaltimestart = time.time()
width = 1920
height = 1080
framesToProduce = 100
finalDirectory = 'cvart/'
videoDirectory = 'video/'


def check_or_create_directory(directory):
    pathNeeded = os.path.isdir(os.getcwd() + '/' + directory)
    if pathNeeded == False:
        os.mkdir(os.getcwd() + '/' + directory)


def write_frame(frame):
    start = time.time()
    img = np.zeros((height,width,3), np.uint8)


    for yPos in range(0, height):
        for xPos in range(0, width):
            img[yPos, xPos] = (xPos + random.randrange(-10, 10), yPos + random.randrange(-10, 10), xPos-yPos + random.randrange(-10, 10))


    # img[:, 0:width] = (255 - frame,255 - frame,0)      # (B, G, R)
    # img[:, width - frame * 55:width] = (0,255 - frame,255 - frame)

    print ('printing frame:', frame)

    print_image(img, frame, start)


def print_image(img, frame, start):
    file_name = finalDirectory + str('%04d') % frame + '.png'
    cv2.imwrite(file_name, img)
    print('It took', time.time()-start, 'seconds.')
    print('To make', str(file_name))


if __name__ == '__main__':
    check_or_create_directory(finalDirectory)
    for frame in range (1, framesToProduce):
        write_frame(frame)
    #
    os.chdir(os.getcwd() + '/' + finalDirectory)
    cmdBuild = 'ffmpeg -f image2 -r 30 -i %04d.png -c:v libx264 -pix_fmt yuv420p out.mp4'
    os.system(cmdBuild)

print ('It took', time.time()-totaltimestart, 'seconds.')
