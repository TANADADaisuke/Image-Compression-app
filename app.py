import glob
import os
import sys
from PIL import Image


# set variables
COMPRESE_RATE = 1.5
COMPRESS_STEP = 0.5
MEDIA_DIR = 'media'

# get file size
files = glob.glob('media/*.*')
file_size = os.stat(files[0]).st_size
print(files[0], ": ", file_size)


def compress_files():
    """
    compress all files in MEDIA_DIR.

    Return: None
    """
    files = get_files()
    pass
# this is a simple script to quickly identify a set of image files:
# for infile in sys.argv[1:]:
#     try:
#         with Image.open(infile) as im:
#             print(infile, im.format, f'{im.size}x{im.mode}')
#     except OSError:
#         pass

def compress_given_file(file, rate):
    """
    compress a given file with given rate
    """
    pass
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

def get_files():
    pass

def main():
    """
    main function
    """
    # in case with sys args
    if len(sys.args) == 2:
        compress_given_file(sys.args[1], sys.args[2])
    elif len(sys.args) == 1:
        compress_files()
    else:
        print(
            'Causion! App should run with no args or only with ' + \
            'one pair of file and compress rate.'
        )



