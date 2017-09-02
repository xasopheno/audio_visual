import cv2
import numpy as np
import random
import time
import math
import os
from scipy.stats import chi2
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


def gaussian_distribution(x, sigma, mu):
    probability = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )
    return probability


def sine_distribution(x):
    probability = (math.sin(100000000000000000 * x))/(math.pi * 10)
    return probability

def euclidean_distance(x0, y0, x1, y1):
    distance = math.sqrt(pow((x0 - x1), 2) + pow((y0 - y1), 2))
    return distance


def write_frame(frame):
    start = time.time()
    img = np.zeros((height,width,3), np.uint8)

    for yPos in range(0, height):
        for xPos in range(0, width):
           ed = euclidean_distance(width/random.randrange(2, 3), height/random.randrange(2, 3), xPos, yPos)
           prob = sine_distribution(ed)
           # prob = gaussian_distribution(ed, random.randrange(30,60), random.randrange(50,200))
           rand = random.uniform(0, .005)
           if rand < prob:
               img[yPos, xPos] = (230 + random.randrange(-20, 0), 200 + random.randrange(-20, 0), 190)
           else:
               img[yPos, xPos] = (0, 0, 0)


    # for yPos in range(0, height):
    #     for xPos in range(0, width):
    #         ed = euclidean_distance(width /2, height /2, xPos, yPos)
    #         # prob = sine_distribution(ed)
    #         prob = gaussian_distribution(ed, random.randrange(10,90), random.randrange(30,250))
    #         rand = random.uniform(0, .005)
    #         if rand < prob:
    #             img[yPos, xPos] = (random.randrange(80, 120), random.randrange(70, 120), 150)
    #
    #
    # for yPos in range(0, height):
    #     for xPos in range(0, width):
    #         ed = euclidean_distance(width/2, height/2, xPos, yPos)
    #         # prob = sine_distribution(ed)
    #         prob = gaussian_distribution(ed, random.randrange(20,70), random.randrange(20,500))
    #         rand = random.uniform(0, .004)
    #         if rand < prob:
    #             img[yPos, xPos] = (random.randrange(20, 40), random.randrange(0, 50), 90)


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
    # #
    os.chdir(os.getcwd() + '/' + finalDirectory)
    cmdBuild = 'ffmpeg -f image2 -r 30 -i %04d.png -c:v libx264 -pix_fmt yuv420p out.mp4'
    os.system(cmdBuild)

    # for i in range(1000):
    #     prob = gaussian_distribution(i, 50, 500)
    #     rand = random.uniform(0, .01)
    #     if rand < prob:
    #         print(1)
    #     else:
    #         print(0)

print ('It took', time.time()-totaltimestart, 'seconds.')
