# -*- coding:utf-8 -*-
import os
import sys
from PIL import Image


def resizeImg(img, a, b):
    """Resize the image to (a, b)"""
    if img.size != (a, b):
        img = img.resize((a, b))
    return img


def conver2RGB(img):
    """Convert the image to RGB mode if it is not in RGB"""
    if img.mode != ('RGB'):
        img = img.convert('RGB')
    return img


def resize():
    read_input = sys.stdin.readline
    print("Please input the directory that contains the image files (be sure to exclude the ending '/')")
    dir = str(read_input()).strip('\n') + '/'
    namelist = []
    print("Please input the number of files in which you want to resize the images")
    numFiles = int(read_input())  # The number of files that contains images to be removed

    for num in range(numFiles):
        print("Please input the name of the files")
        file = str(read_input()).strip('\n')
        namelist.append(file)

    for name in namelist:
        index = 0
        filelist = os.listdir(dir + name)
        print(filelist)
        for file in filelist:
            image = Image.open(dir + name + '/' + file)
            image = conver2RGB(image)
            image = resizeImg(image, 362, 362)
            image.save(dir + name + '/' + file)
            index += 1

        print("Successfully resized all images in this file!")
