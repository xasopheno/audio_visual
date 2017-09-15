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


def distribution(x, height, width, frame):
    probability = 0
    if x != 0:
        probability = math.atan(1/math.sin(x * 10000 * height/width * 1/frame - height + width))
    return probability


def euclidean_distance(x0, y0, x1, y1):
    distance = math.sqrt(pow((x0 - x1), 2) + pow(y0 - y1, 2))
    return distance


def write_frame(frame):
    start = time.time()
    img = np.zeros((height ,width, 3), np.uint8)

    for yPos in range(0, height):
        for xPos in range(0, width):
            ed = euclidean_distance(width / 5, height / 5 , xPos, yPos)
            dist = distribution(ed, height, width, frame)
            prob = gaussian_distribution(ed, random.randrange(30,60), random.randrange(50,80))
            rand = random.uniform(0, .0045)
            if rand < prob:
                # img[yPos, xPos] = (ed - xPos / frame + 1, ed - xPos / frame + 1, ed + xPos / frame + 1)
                img[yPos, xPos] = (70 + random.choice([frame, 20, -20, 10, -10]),
                                   95 + random.randrange(-30, 30, 2),
                                   10 + random.randrange(10, 40))
            else:
                img[yPos, xPos] = (50 + random.randrange(0, 20, 2),
                                   30 + random.randrange(0, 20, 2),
                                   20 + random.randrange(0, 10))

    print('1')
    for yPos in range(0, height):
        for xPos in range(0, width):
            ed = euclidean_distance(width * 2/3, height * 3/4, xPos, yPos)
            dist = distribution(ed, height, width, frame)
            prob = gaussian_distribution(ed, random.randrange(30,70), random.randrange(20,40))
            rand = random.uniform(0, .0065)
            if rand < prob:
                # img[yPos, xPos] = (ed - xPos / frame + 1, ed - xPos / frame + 1, ed + xPos / frame + 1)
                img[yPos, xPos] = (100 + random.choice([frame, 20, -20, 10, -10]),
                                   25 + random.randrange(-30, 30, 2),
                                   205 + random.randrange(10, 40))

    print('2')
    for yPos in range(0, height):
        for xPos in range(0, width):
            ed = euclidean_distance(width * 2/3, height / 4.5, xPos, yPos)
            dist = distribution(ed, height, width, frame)
            prob = gaussian_distribution(ed, random.randrange(30,40), random.randrange(20,60))
            rand = random.uniform(0, .0055)
            if rand < prob:
                # img[yPos, xPos] = (ed - xPos / frame + 1, ed - xPos / frame + 1, ed + xPos / frame + 1)
                img[yPos, xPos] = (110 + random.choice([frame, 20, -20, 10, -10]),
                                   130 + random.randrange(-30, 30, 2),
                                   110 + random.randrange(10, 40))

    print('3')
    for yPos in range(0, height):
        for xPos in range(0, width):
            ed = euclidean_distance(width * 1/3, height * 1/2, xPos, yPos)
            dist = distribution(ed, height, width, frame)
            prob = gaussian_distribution(ed, random.randrange(30,60), random.randrange(50,180))
            rand = random.uniform(0, .005)
            if rand < prob:
                # img[yPos, xPos] = (ed - xPos / frame + 1, ed - xPos / frame + 1, ed + xPos / frame + 1)
                img[yPos, xPos] = (40 + random.choice([frame, 20, -20, 10, -10]),
                                   80 + random.randrange(-30, 30, 2),
                                   120 + random.randrange(10, 40))

    print('4')
    for yPos in range(0, height):
        for xPos in range(0, width):
            ed = euclidean_distance(width * 1/5, height * 1/5, xPos, yPos)
            dist = distribution(ed, height, width, frame)
            prob = gaussian_distribution(ed, random.randrange(30,90), random.randrange(40,90))
            rand = random.uniform(0, .0045)
            if rand < prob:
                # img[yPos, xPos] = (ed - xPos / frame + 1, ed - xPos / frame + 1, ed + xPos / frame + 1)
                img[yPos, xPos] = (110 + random.choice([frame, 20, -20, 10, -10]),
                                   17 + random.randrange(-30, 30, 2),
                                   50 + random.randrange(10, 40))
    print('5')


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
    # # generate frames
    # check_or_create_directory(finalDirectory)
    # for frame in range (1, framesToProduce):
    #     write_frame(frame)

    # build video
    os.chdir(os.getcwd() + '/' + finalDirectory)
    cmdBuild = 'ffmpeg -f image2 -r 30 -i %04d.png -c:v libx264 -pix_fmt yuv420p out.mp4'
    os.system(cmdBuild)

print ('It took', time.time()-totaltimestart, 'seconds.')
