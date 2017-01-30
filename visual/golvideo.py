import cv2
import numpy as np
import random
import time
import math
import os
# from multiprocessing import Pool

from npgol import iterate 

totaltimestart = time.time()
width = 1920
height = 1080
framesToProduce = 350 
finalDirectory = 'cvart/'
# create 'video/' folder. use this command to separate video into frames
# ffmpeg -i beachsydney.mp4 -r 30/1 $filename%04d.png
videoDirectory = 'video/'

def check_or_create_directory(directory):
  pathNeededExists = os.path.isdir(os.getcwd() + '/' + directory)
  if pathNeededExists == False:
    os.mkdir(os.getcwd() + '/' + directory)

def iterate_gol(past_image, current_image, video_image):
  "Iterate Game of Life and encode video color data"
  past_image = cv2.imread(past_image)
  video_image = cv2.imread(video_image)
  
  for yPos in range(0, height):
      for xPos in range(0, width):
        if any(val > 1 for val in past_image[yPos, xPos]):
          past_image[yPos, xPos] = 1  

  new_img = np.zeros(past_image.shape, dtype=int)

  for yPos in range(0, height):
    for xPos in range(0, width):      
      if all(val == 1 for val in past_image[yPos, xPos]):
        new_img[yPos, xPos] = video_image[yPos, xPos]  
          
  return new_img

def write_frame(frame):
  start = time.time()
  img = np.random.randint(0,2,(1080,1920))
  
  print 'printing frame:', frame
  
  past_image = finalDirectory + str('%04d') % (frame - 1) + '.png'
  current_image = finalDirectory + str('%04d') % frame + '.png'
  video_image = videoDirectory + str('%04d') % frame + '.png'

  if os.path.exists(past_image):
    print 'comparing ', past_image, ' to, ', current_image
    print 'video frame: ', video_image
    img = iterate_gol(past_image, img, video_image)

  print_image(img, frame, start) 

def print_image(img, frame, start):
  file_name = finalDirectory + str('%04d') % frame + '.png'
  cv2.imwrite(file_name, img)
  print 'It took', time.time()-start, 'seconds.'
  print 'To make', str(file_name)

if __name__ == '__main__':
    check_or_create_directory(finalDirectory) #check if directory exists, if not create it
    # pool = Pool(6)  # Create a multiprocessing Pool
    # pool.map(write_frame, xrange(framesToProduce))  # process write_frame iterable with pool
    for frame in range (1, framesToProduce):
      write_frame(frame)

    os.chdir(os.getcwd() + '/' + finalDirectory)
    cmdBuild = 'ffmpeg -f image2 -r 30 -i %04d.png -c:v libx264 -pix_fmt yuv420p out.mp4'
    os.system(cmdBuild)

print 'It took', time.time()-totaltimestart, 'seconds in total.'
