import os
import png
import array

filename = raw_input("Input filename: ")
reader = png.Reader(filename)

flat_data = reader.read_flat() # read as a tuple of (width, height, pixels, metadata) where pixels is an array of RGB values
outfile = open(raw_input("Output filename: "), 'wb')
rgblist = flat_data[2].tolist() # convert from (width, height, pixels, metadata) to a list of rgb values from the 2nd item (pixels)
padding_index = -1 # start at end of file
while rgblist[padding_index] == 255: # go from end of file (index -1) to the end of padding (when the RGB values no longer equal 255
    padding_index -= 1
cutlist = rgblist[0:padding_index+1] # cut out the trailing padding
outarray = array.array('B') # make an array of bytes
outarray.fromlist(cutlist) # take values from cutlist and convert to bytes
outarray.tofile(outfile) # write bytes to outfile
