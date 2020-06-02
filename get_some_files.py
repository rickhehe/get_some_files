import os
import re
import ctypes
import shutil

from time import sleep

def sth_fun(source_file, destination_folder):

    try:
        shutil.copy(source_file, destination_folder)

    except PermissionError:
        print('permission denied')
        sleep(3)
        sth_fun() # recursive...

def walk(source, destination, pat):

    for root, dirs, files in os.walk(source):

        for name in files:
            if re.search(
                pat,
                name,
                flags=re.I
            ):
                sth_fun(
                    os.path.join(root, name),
                    f'{destination}\{name}'
                )

def main():

    # define i/o
    source = r'src'
    destination = r'dest'

    # make sure there is a place to go
    try:
        os.makedirs(destination)

    except FileExistsError:
        print('it is there')

    # define a pat
    pat = '^1156-.+[^46]\d\d\.csv$|^a-00335'

    walk(source, destination, pat)

if __name__ == '__main__':
    main()
    print('done')
