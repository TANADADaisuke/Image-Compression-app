import glob
import os
import sys
from PIL import Image


# set variables
COMPRESE_RATE = 1.5
COMPRESS_STEP = 0.5
MEDIA_DIR = 'media'


def compress_files():
    """
    compress all files in MEDIA_DIR.

    Return: None
    """
    files = get_files()
    
    # iterate over files
    for file in files:
        # compress each file until the file size < 300kB
        compress_file_recursive(file, COMPRESE_RATE)

def compress_file_recursive(file, rate):
    """
    recursively compress file until the file size < 300kB
    
    Return: None
    """
    compressed = compress_given_file(file, rate)
    # return None if the file is not image format
    if not compressed:
        return None
    # check file size and call the function recursively
    file_size = get_file_size(compressed)
    if file_size > 300:
        return compress_file_recursive(file, rate + COMPRESS_STEP)
    # finally announce the compressed file size
    print(f'{file} is compressed in {file_size}kB.')

def compress_given_file(file, rate):
    """
    compress a given file with given rate
    
    Return: filename of compressed file
    """
    try:
        # open image file and resize it
        with Image.open(file) as im:
            xsize = int(im.size[0] // rate)
            ysize = int(im.size[1] // rate)
            out = im.resize( (xsize, ysize) )
            outfile = '_resized.'.join(file.split('.'))
            out.save(outfile)
            return outfile
    except OSError:
        # if the file is not image format, print the causion message
        # and return None
        print(f'Caution! {file} is not image format.')
        return None

def get_file_size(file):
    """
    Return: the size of file(kB/integer)
    """
    file_size = os.stat(file).st_size
    return int(file_size) // 1000

def get_files():
    """
    get all file in media folder
    """
    files = sorted(glob.glob(f'{MEDIA_DIR}/*.*'))
    return files

def main():
    """
    main function
    """
    # in case with sys args
    if len(sys.argv) == 2:
        compress_given_file(sys.args[1], sys.args[2])
    elif len(sys.argv) == 1:
        compress_files()
    else:
        print(
            'Causion! App should run with no args or only with ' + \
            'one pair of file and compress rate.'
        )


if __name__ == '__main__':
    main()
