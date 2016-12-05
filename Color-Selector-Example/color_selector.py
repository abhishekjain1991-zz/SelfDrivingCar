import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


# Read in the image and print out some stats
image = mpimg.imread('test.jpg')
print('This image is: ',type(image), 
         'with dimensions:', image.shape)

# Grab the x and y size and make a copy of the image
ysize = image.shape[0]
xsize = image.shape[1]

# Next step just copies the array created in line number 6
# dimensions are rows columns and (r,g,b) values or 3
color_select = np.copy(image)
# Define our color selection criteria
red_threshold = 198
green_threshold = 198
blue_threshold = 198
rgb_threshold = [red_threshold, green_threshold, blue_threshold]

# See what the image looks like in pixels
# Explaination for image rendering using matplotlib
# http://matplotlib.org/users/image_tutorial.html
#print color_select

#for x in range (0,ysize):
#    for y in range (0,xsize):
#            for z in range (0,3):
#                    if color_select[x][y][z] < rgb_threshold[z]:
#                            color_select[x][y] = [0,0,0]
#                            break;
#                            
#
# complex but faster  way of doing this
# above method is crap for very large images 
# Use a "bitwise OR" to identify pixels below the threshold

# Each of these returns an array of booleans for each channel 
# (R G or B) and using or one gets Only those elements that 
# match the criteria 
#print image[:,:,0] < rgb_threshold[0]
thresholds = (image[:,:,0] < rgb_threshold[0]) \
            | (image[:,:,1] < rgb_threshold[1]) \
            | (image[:,:,2] < rgb_threshold[2])

color_select[thresholds] = [0,0,0]
# Display the image                 
plt.imshow(color_select)
plt.savefig('Output.jpg')
