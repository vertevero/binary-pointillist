#!/usr/bin/env python
#
# Copyright © 2011 vertevero
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


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
