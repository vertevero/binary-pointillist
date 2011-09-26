import os
import png
import array

hexarray = []

counter = 0

infilename = raw_input("Input filename: ")
infilesize = os.path.getsize(infilename)
print 'Loading a ' + str(infilesize) + ' byte file...'
with open(infilename, "rb") as f:  # open input file
    byte = f.read(1) # read the first byte
    counter += 1
    while byte: # while there are more bytes to read
        if counter <= 3: # group bytes by three (R,G,B)
           as_int = int(byte.encode('hex'), 16) # turn hex value into int
           hexarray.append(as_int) # and append to the array
        byte = f.read(1) # read next byte

outfilename = raw_input('Output file name: ')
outfile = open(outfilename, 'wb')
width = int(raw_input('Width: '))
height = int(raw_input('Height: '))
writer = png.Writer(width, height)
area = width * height
while (len(hexarray) < (area*3)): # fill in all pixels after as white
    hexarray.append(255)
writer.write_array(outfile, hexarray)
outfile.close()
