# -*- coding:utf-8 -*-
import os
import random
import shutil
import sys


def moveImg(fileDir, n):
    """move n% of the images in one directory to the other"""
    pathDir = os.listdir(fileDir)
    tarDir = fileDir[:-1] + '_test/'
    num = len(pathDir)
    sample = random.sample(pathDir, int(num * n / 100))
    print(sample)

    for name in sample:
        shutil.move(fileDir + name, tarDir + name)


def move():
    read_input = sys.stdin.readline
    print("Please input the directory that contains the image files (be sure to exclude the ending '/')")
    dir = str(read_input()).strip('\n') + '/'
    namelist = []
    print("Please input the number of files in which you want to move the images")
    numFiles = int(read_input())  # The number of files that contains images to be moved

    for num in range(numFiles):
        print("Please input the name of the files")
        file = str(read_input()).strip('\n')
        namelist.append(file)

    for name in namelist:
        if not os.path.exists(dir + name + '_test/'):
                os.makedirs(dir + name + '_test/')  # The new files are used as testing sets for the old ones

        print("Please input the percentage of the total images you want to use in the testing set")
        n = int(read_input())
        moveImg(dir + name + '/', n)
        print("Successfully move all images in this file to a testing set!")
