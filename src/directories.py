import os
import logging
  
def create_dir(dir,directory):
    path_ = os.path.join(dir, directory)
    if not os.path.exists(path_):
        os.makedirs(path_)

def remove_output_file(path):
    try:
        os.remove(path)
    except:
        logging("No file")