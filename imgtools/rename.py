# -*- coding:utf-8 -*-
import os
import sys


def renameImg(fileDir):
    """Rename the images to target names"""
    filelist = os.listdir(fileDir)
    total_num = len(filelist)
    i = 0  # Order of the images to be renamed

    for item in filelist:
        src = os.path.join(os.path.abspath(fileDir), item)
        dst = os.path.join(os.path.abspath(
            fileDir), str(i) + '.jpg')
        os.rename(src, dst)
        i += 1
        print ('converting %s to %s ...' % (src, dst))
        print ('total %d to rename & converted %d jpgs' % (total_num, i))


def rename():
    read_input = sys.stdin.readline
    print("Please input the directory that contains the image files (be sure to exclude the ending '/')")
    dir = str(read_input()).strip('\n') + '/'
    namelist = []
    print("Please input the number of files in which you want to rename the images")
    numFiles = int(read_input())  # The number of files that contains images to be renamed

    for num in range(numFiles):
        print("Please input the name of the files")
        file = str(read_input()).strip('\n')
        namelist.append(file)

    for name in namelist:
        renameImg(dir + name + '/')

    print("Successfully renamed all images!")
