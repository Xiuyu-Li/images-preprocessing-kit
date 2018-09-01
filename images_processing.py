# -*- coding:utf-8 -*-
import sys
from imgtools import crop_to_9
from imgtools import rename
from imgtools import move
from imgtools import remove
from imgtools import resize

if __name__ == '__main__':
    while(True):
        print("How do you want to manipulate images? 1. Crop to 9 pieces "
              "2. Rename 3. Move 4. Remove certain types 5. Resize 6. Exit")
        read_input = sys.stdin.readline
        arg = read_input().strip('\n')

        if (arg != '1' and arg != '2' and arg != '3' and
                arg != '4' and arg != '5' and arg != '6'):
            print("Invalid commend! Please retry.")

        if arg == '1':
            crop_to_9.crop()
            print('\n')

        if arg == '2':
            rename.rename()
            print('\n')

        if arg == '3':
            move.move()
            print('\n')

        if arg == '4':
            remove.remove()
            print('\n')

        if arg == '5':
            resize.resize()
            print('\n')

        if arg == '6':
            sys.exit(0)
