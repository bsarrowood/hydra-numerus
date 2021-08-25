# Created by:       Brad Arrowood
# Created on:       2021.08.12
# Last updated:     2021.08.25
# Script name:      numerus-hydra.py
# Python version:   3.9.6
# Description:      a script to create a truly random set of numbers
#                   a random pixel image is created and converted into a 3-dimensional array of the RGB values
#                   a random pixel is then chosen and the RGB value is multiplied by another random number
#                   the result is then divided by yet another random number resulting in a 3-digit decimal
#                       number between the values of 0 and 1
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
    # opted for creating a random pixel image so script doesn't need internet access

    # this section is for creating a random pixel image
    data=np.random.randint(low=0,high=512,size=512*512*3, dtype=np.uint32)
    data=data.reshape(512,512,3)
    Image.fromarray(data,'RGB').save("output.jpg")

    # this section is for downloading a random dog photo but requests internet access
    #dog.getDog(filename='output')

def main():
    # this func is set to generate 5 random numbers to output 5 truly random results:
    #       3 numbers between 0-2 to choose a random pixel from the 3-dimensional array of the RGB values
    #       a number between 1-9 to multiple the RGB value by a hundreth value (0.01-0.09)
    #       a number between 1-999 to multiple the decimal value followed by dividing it by 1,000
    # the tick counter is to control the number of iterations for 5 output results
    # the randomIMG func creates a random pixel image to work with
    # within the loop, the rando func is run 3 times to get a random 0, 1, or 2. this is used
    #       to randomly point to a pixel within the image array to get the color values for it.
    # a random number 1-9 is then made, converted to a string, concatenated to make it a
    #       hundreth demical value, and then converted to a float amount
    # the random pixel colour value is then multiplied by the random decimal value
    # another random number, ranging from 1-999, is divided by 1,000 before being multipled
    #       by the the previous resulting output to create a truely random decimal number
    # if the final random number is more than 0 and less than 1, it is then printed to the
    #       screen and counted towards the requested 5 random numbers. if the result is 0, 0.0, 
    #       1 or greater then loop runs again until it has 5 random numbers. the random numbers
    #       are never stored each time the script runs or from loop to loop
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
        n = n * (random.randint(1, 999)/1000)

        if 0 < n < 1:
            dotZero = '0.0'
            n = round(n,3)
            if n != float(dotZero):
                #print(round(n,3))
                print(n)
                tick = tick + 1
        
    if os.path.exists("output.jpg"):
        os.remove("output.jpg")

if __name__ == '__main__':
    clear()
    main()
