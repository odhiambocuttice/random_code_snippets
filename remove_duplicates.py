import os
import hashlib

import tkinter as tk
from tkinter.filedialog import askdirectory


def hashing():
    """
    Takes a folder and its contents and pass them through a hash function,
    stores the hashes in the in a dictionary, then check for duplicates,
    then delets the filepath of the duplicates

    params: folders
    """
    unique_files = {}
    tk.Tk().withdraw()  # prevents the root window from appearing
    path = askdirectory()
    path_to_folder = os.walk(path)  # list all the files
    for folder, sub_folder, files in path_to_folder:
        for file in files:
            filepath = os.path.join(folder, file)
            filehash = hashlib.md5(open(filepath, 'rb').read()).hexdigest()

            if filehash in unique_files:
                os.remove(filepath)
                print(f"{filepath} deleted")
            else:
                unique_files[filehash] = path


if __name__ == '__main__':
    hashing()
