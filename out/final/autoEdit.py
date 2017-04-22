""" 
Generates a randomly edited video from a list of videos.
"""

import os
from os import system
from random import shuffle
import random
import subprocess
from path import path

inputDir = '/Users/dannymeyer/Documents/projects/audio_visual/audio/out/final'
videosToMix = os.listdir('/Users/dannymeyer/Documents/projects/audio_visual/audio/out/final/')

outputDir = '/Users/dannymeyer/Documents/projects/audio_visual/audio/out/final/autoEdit'
listDirOutput = os.listdir('/Users/dannymeyer/Documents/projects/audio_visual/audio/out/final/')


def videos_rand_order(folder):
  videos = []
  """ 
  Generates a list of all videos in 'folder' sorted randomly 
  """
  for video in folder:
    if video.endswith(('MOV', 'mov', 'mp4', '3gp')):
      videos.append(video)

  shuffle(videos)
  return videos

def generate_videos():
  n = 1
  for video in videoList:
    # print(video.rsplit('.', 1)[0])
    cmdVidLength = "ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 " + inputDir + "/" + '"' + video + '"' 
    # -sexagesimal for 00:00:00.000
    totalVidLength = subprocess.check_output(cmdVidLength, shell=True)
    
    rndVidLength = ("{0:.2f}".format(random.uniform(0.5, 1.5)))
    availRange = float(totalVidLength) - float(rndVidLength)
    
    # print 'total', totalVidLength
    print 'length', rndVidLength
    # print 'avail', availRange
    start = ("{0:.2f}".format(random.uniform(0, availRange)))
    print 'start', start

    cmd = "ffmpeg -ss " + start + " -i " + inputDir + "/" + video + " -t " + rndVidLength + " -c:v libx264 -c:a aac -strict experimental -b:a 128k " + outputDir + '/' + str('%0.2d' % n) + ".mov"
    n += 1
    print(cmd)
    os.system(cmd)


def join_videos():  
  listDirOutput = os.listdir('/Users/dannymeyer/Documents/projects/audio_visual/audio/out/final/')
  cmdIntJoin = 'ffmpeg -i "concat:'
  n = 1
  for vid in listDirOutput:
    if vid.endswith(('MOV', 'mov', 'mp4', '3gp')):
      print(vid)
      cmdIntermediate = "ffmpeg -i " + vid + " -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate" + str('%0.2d' % n) + ".ts"
      print(cmdIntermediate)
      os.system(cmdIntermediate)
      cmdIntJoin += "intermediate" + str('%0.2d' % n) + ".ts|"
      n += 1

  cmdIntJoin = cmdIntJoin[:-1] + '"'
  cmdIntJoin += " -c copy -bsf:a aac_adtstoasc output.mp4"

  print cmdIntJoin
  os.system(cmdIntJoin)
  print("Videos autoedited. You're welcome")


def clean_up():
  print('Cleaning up')
  outputDir = '/Users/dannymeyer/documents/projects/tia2/autoEdit/output'
  d = path(outputDir)
  files = d.walkfiles('*.mov')
  for file in files:
      file.remove()
      print "Removed {} file".format(file)
  files = d.walkfiles('*.ts')
  for file in files:    
      file.remove()
      print "Removed {} file".format(file)


videoList = videos_rand_order(videosToMix)

# generate_videos()

# os.chdir(outputDir)
os.system('ls')

join_videos()

clean_up()

os.system('open output.mp4')
