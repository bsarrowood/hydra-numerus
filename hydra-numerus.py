# Created by:       Brad Arrowood
# Created on:       2021.08.12
# Last updated:     2021.08.17
# Script name:      hydra-numerus.py
# Python version:   3.9.6
# Description:      a script to create a truly random series of numbers
#                   an image is converted into a 3-dimensional array of the RGB values of each pixel
#                   a random pixel is chosen, the vaule is then multiplied by a random number, and then
#                       divided by a random number. the resulting number is set to be a 3-decimal number
#                       which stays between 0 and 1
#
# Requirements:     numpy
#                   pillow
#                   random-dog
#
# References:
# https://e2eml.school/images_to_numbers.html
# https://www.geeksforgeeks.org/get-random-dog-images-in-python/

import dog
import os
import numpy as np
import random
from os import system, name
from PIL import Image
from time import sleep

def clear():
    # for windows
    if name =='nt':
        _ = system('cls')
    # for linux & mac (here, os.name is 'posix')
    else:
        _ = system('clear')

def randomIMG():
    # this func can either generate a random pixel image or download a random dog photo
    # the image is saved as "output.jpg" and used as part of the random algorithm

    # this section is for creating a random pixel image
    data=np.random.randint(low=0,high=512,size=512*512*3, dtype=np.uint32)
    data=data.reshape(512,512,3)
    Image.fromarray(data,'RGB').save("output.jpg")

    # this section is for downloading a random dog photo
    #dog.getDog(filename='output')

def main():
    # this func is set to generate 5 truely random numbers
    # the tick counter is to control the number of iterations
    # the func to create/get a random image is triggered and saved to the dir
    # within the loop, the rando func is run 3 times to get a random 0, 1, or 2. this is used
    #   to randomly point to a pixel within the image array to get the color values for it.
    # a random number 1-9 is then made, converted to a string, concatenated to make it a
    #   hundreth demical value, and then converted to a float amount
    # the random pixel colour value is then multiplied by the random decimal value
    # another random number, ranging from 1-999, is divided by 10,000 before being multipled
    #   by the the previous resulting output to create a truely random decimal number
    # if the final random number is more than 0 and less than 1, it is then printed to the
    #   screen and counted towards the requested 5 random numbers. if the result is 0, 0.0, 
    #   1 or greater then loop runs again until it has 5 random numbers. the random numbers
    #   are never stored each time the script runs or from loop to loop
    # after the loop ends, the random image created for this is deleted

    tick = 1
    randomIMG()

    while tick < 6:
        def rando():
            ranNum = random.randint(0, 2)
            return ranNum
        
        img = np.asarray(Image.open("output.jpg"))
        n = img[rando(),rando(),rando()]
        r = random.randint(1, 9)
        r = float(str(.0) + str(r))
        n = n * r
        n = n * (random.randint(1, 999)/10000)

        if 0 < n < 1:
            dotZero = '0.0'
            if n != float(dotZero):
                print(round(n,3))
                tick = tick + 1
        
    if os.path.exists("output.jpg"):
        os.remove("output.jpg")

if __name__ == '__main__':
    clear()
    main()
