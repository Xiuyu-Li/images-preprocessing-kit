# -*- coding:utf-8 -*-
import sys
import os


def removeImg(fileDir, imgType):
    """Remove the images that are not in certain type"""
    filelist = os.listdir(fileDir)
    for file in filelist:
        if os.path.splitext(file)[1] != '.' + imgType:
            os.remove(fileDir + '/' + file)


def remove():
    read_input = sys.stdin.readline
    print("Please input the directory that contains the image files (be sure to exclude the ending '/')")
    dir = str(read_input()).strip('\n') + '/'
    namelist = []
    print("Please input the number of files in which you want to remove the images")
    numFiles = int(read_input())  # The number of files that contains images to be removed

    for num in range(numFiles):
        print("Please input the name of the files")
        file = str(read_input()).strip('\n')
        namelist.append(file)

    for name in namelist:
        print("Please input the type of the images you want to remove")
        imgType = str(read_input()).strip('\n')
        removeImg(dir + name + '/', imgType)
        print("Successfully removed all images not ending with .%s!" %imgType)
