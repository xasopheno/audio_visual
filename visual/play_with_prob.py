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
framesToProduce = 150
finalDirectory = 'cvart1/'
videoDirectory = 'video/'


def check_or_create_directory(directory):
    pathNeeded = os.path.isdir(os.getcwd() + '/' + directory)
    if pathNeeded == False:
        os.mkdir(os.getcwd() + '/' + directory)


def gaussian_distribution(x, sigma, mu):
    probability = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (x - mu)**2 / (2 * sigma**2) )
    return probability


def euclidean_distance(x0, y0, x1, y1):
    distance = math.sqrt(pow((x0 - x1), 2) + pow((y0 - y1), 2))
    return distance


def process(img, xCenter, yCenter, sigma, mu, threshold, thingColor, backgroundColor, i):
    for yPos in range(0, height):
        for xPos in range(0, width):
            ed = euclidean_distance(xCenter, yCenter, xPos, yPos)
            prob = gaussian_distribution(ed, sigma, mu)
            rand = random.uniform(0, threshold)
            if rand < prob:
                img[yPos, xPos] = thingColor
                img[yPos - 150, xPos] = thingColor
            else:
                if i == 0:
                    img[yPos, xPos] = backgroundColor

    print('printed: ', xCenter, yCenter, sigma, mu, threshold, thingColor, backgroundColor)


def write_frame(frame):
    start = time.time()
    img = np.zeros((height,width,3), np.uint8)

    xCenter = random.choice([width/2, width * 4/5, width * 1/5, width * 8/9, width * 1/9])
    yCenter = random.choice([height/2])
    sigma = random.randrange(10, 100)
    mu = random.randrange(0,400)
    threshold = 0.005
    thingColor = (random.randrange(0, 100) + random.randrange(0, 20),
                  random.randrange(40, 80) + random.randrange(0, 10),
                  random.randrange(50, 150) + random.randrange(0, 40))
    backgroundColor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))

    for i in range(1):
        process(img, xCenter, yCenter, sigma, mu, threshold, thingColor, backgroundColor, i)

    print ('printing frame:', frame)

    print_image(img, frame, start)

def write_frame_line(frame):
    start = time.time()
    img = np.zeros((height,width,3), np.uint8)

    xCenter = width * 8/9
    yCenter = height * 5/7
    sigma = 90
    mu = 160
    threshold = 0.005
    thingColor = (random.randrange(110, 130) + random.randrange(10, 39),
                  random.randrange(189, 210) + random.randrange(10, 20),
                  random.randrange(180, 190) + random.randrange(35, 40))
    backgroundColor = (0, 0, 0)

    thingColor2 = (54, 134, 112)
    process(img, width * 3/9, height * 3/7, sigma /2, mu /2 ,threshold /2, thingColor2, backgroundColor, 1)
    process(img, width * 6/9, height * 2/7, sigma, mu, threshold, thingColor, backgroundColor, 1)

    for xPos in range(0, width):
        for yPos in range(100, 218):
            img[yPos, xPos] = random.choice([(0,0,0),(185,155,22),(188,12,99),(200,25,62),(223,64,87),(18,65,23)])
        for yPos in range(200, 320):
            img[yPos, xPos] = random.choice([(0,0,0),(200,155,5),(108,12,9),(220,245,62),(123,64,87),(180,65,23)])

    for yPos in range(0, height):
        for xPos in range(200, 399):
            img[yPos, xPos] = random.choice([(0,0,0),(185,155,125),(111,12,109),(245,200,62),(223,64,87),(90,65,23)])
        for xPos in range(990, 1070):
            img[yPos, xPos] = random.choice([(0,0,0),(18,13,145),(1,1,209),(45,20,262),(2,64,207),(98,65,23)])

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
        write_frame_line(frame)

    os.chdir(os.getcwd() + '/' + finalDirectory)
    cmdBuild = 'ffmpeg -f image2 -r 30 -i %04d.png -c:v libx264 -pix_fmt yuv420p out.mp4'
    os.system(cmdBuild)


print ('It took', time.time()-totaltimestart, 'seconds.')
