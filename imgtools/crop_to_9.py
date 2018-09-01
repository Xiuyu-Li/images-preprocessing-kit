# -*- coding:utf-8 -*-
from PIL import Image
from PIL import ImageFile
import sys
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True


def fill_image(image):
    """
    Resize the image to square, and use white background
    to replace the part that does not fit the square shape
    """
    width, height = image.size
    # print(width, height)
    new_image_length = width if width > height else height
    # print(new_image_length)
    # print(image.mode)

    if image.mode != "RGB":
        image = image.convert("RGB")  # Convert the image to RGB mode if it is not in RGB

    new_image = Image.new(image.mode, (new_image_length,
                                       new_image_length), color='white')

    if width > height:
        new_image.paste(image, (0, int((new_image_length - height) / 2)))
    else:
        new_image.paste(image, (int((new_image_length - width) / 2), 0))
    return new_image


def cut_image(image):
    """Crop the image to 9 equal sized pieces"""
    width, height = image.size
    item_width = int(width / 3)
    box_list = []
    count = 0

    for j in range(0, 3):
        for i in range(0, 3):
            count += 1
            box = (i * item_width, j * item_width, (i + 1) * 
                   item_width, (j + 1) * item_width)
            box_list.append(box)

    # print(count)
    image_list = [image.crop(box) for box in box_list]
    return image_list


def save_images(image_list, index, name, fileDir):
    """Save the cropped images"""
    for image in image_list:
        if not os.path.exists(fileDir + '/' + name + '_cropped'):
            os.makedirs(fileDir + '/' + name + '_cropped')

        image.save(fileDir + '/' + name +
                   '_cropped/' + str(index) + '.jpg')
        index += 1


def crop():
    read_input = sys.stdin.readline
    print("Please input the directory that contains the image files (be sure to exclude the ending '/')")
    dir = str(read_input()).strip('\n')
    namelist = []
    print("Please input the number of files in which you want to crop the images")
    numFiles = int(read_input())  # The number of files that contains images to be cropped

    for num in range(numFiles):
        print("Please input the name of the files")
        file = str(read_input()).strip('\n')
        namelist.append(file)

    for name in namelist:
        filelist = os.listdir(dir + '/' + name)
        index = 0
        print(filelist)

        for file in filelist:
            image = Image.open(dir + '/' + name + '/' + file)
            image = fill_image(image)
            image_list = cut_image(image)
            save_images(image_list, index, name, dir)
            index += 9

        print("The number of cropped images are %d" %index)  # Output the number of cropped images

    print("Successfully cropped all images!")
