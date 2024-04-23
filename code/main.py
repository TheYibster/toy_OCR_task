import os
from fuctions import *

data_path = os.path.join(os.getcwd(), "..", "data")

if __name__ == '__main__':
    convert_str_to_txt(images_to_text(data_path))