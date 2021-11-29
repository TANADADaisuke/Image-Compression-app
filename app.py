import glob
import os
import sys
from PIL import Image
# im = Image.open('media/IMG_2934.JPG')

# you can now use instance attributes to examine the file content
# print(im.format, im.size, im.mode)

# let's display the image; we can use instance methods
# im.show()

# thumbnail
# size = (128, 128)
# im.thumbnail(size)
# im.save('media/IMG_2934.thumbnail', 'JPEG')

# this is a simple script to quickly identify a set of image files:
# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             print(infile, im.format, f'{im.size}x{im.mode}')
#     except OSError:
#         pass

# get file size
files = glob.glob('media/*.*')
file_size = os.stat(files[0]).st_size
print(files[0], ": ", file_size)


# Geometrical transform:
# compose_rate = 3
# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             xsize = im.size[0] // compose_rate
#             ysize = im.size[1] // compose_rate
#             out = im.resize( (xsize, ysize) )
#             print(f'{infile} is transformed in {xsize}x{ysize}')
#             outfile = '_resized.'.join(infile.split('.'))
#             out.save(outfile)
#     except OSError:
#         pass

