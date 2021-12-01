import glob
import os
import shutil
import sys
from PIL import Image


# set variables
COMPRESE_RATE = 1.5
COMPRESS_STEP = 0.5
MEDIA_DIR = 'media'
ORIGINAL_DIR = 'original'


def is_exist_original_directory():
    """
    check if the original directory exist
    
    Return: None
    """
    original_dir = os.path.join(MEDIA_DIR, ORIGINAL_DIR)
    if not os.path.exists(original_dir):
        os.makedirs(original_dir)

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
    # move the origiinal file into original folder
    target_path = os.path.join(
        os.path.split(file)[0],
        ORIGINAL_DIR,
        os.path.split(file)[1]
    )
    shutil.move(file, target_path)

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

def get_file_path(file):
    """
    get original file path
    
    Return: file path
    """
    file = file.replace('_resized', '')
    for root, dirs, files in os.walk(MEDIA_DIR):
        if file in files:
            return os.path.join(root, file)

def main():
    """
    main function
    """
    # check if the original data store directory exists
    is_exist_original_directory()
    # in case with sys args
    if len(sys.argv) == 3:
        # retrieve file path and compress rate from sys.argv
        file = get_file_path(sys.argv[1])
        rate = float(sys.argv[2])
        # try compressing image file
        compressed = compress_given_file(file, rate)
        if not compressed:
            return None
        # get file size and print it
        file_size = get_file_size(compressed)
        print(f'{file} is compressed in {file_size}kB')
        # move compressed file into media folder
        shutil.move(
            compressed,
            os.path.join(MEDIA_DIR, os.path.split(compressed)[1])
        )
    # in case with no args
    elif len(sys.argv) == 1:
        compress_files()
    # otherwise, print caution message
    else:
        print(
            'Causion! App should run with no args or only with ' + \
            'one pair of file and compress rate.'
        )


if __name__ == '__main__':
    main()
