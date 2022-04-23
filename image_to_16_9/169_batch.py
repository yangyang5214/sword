# -*- coding: UTF-8 -*-
import os
import random
import re
import sys
from string import ascii_lowercase

from image_to_16_9 import main as image_169


def random_str():
    return ''.join(random.choice(ascii_lowercase) for _ in range(10))


def main(path):
    final_dir = os.path.join("/tmp", random_str())
    os.system("mkdir -p %s" % final_dir)
    for item in os.listdir(path):
        if item.startswith("."):
            continue
        if not re.match("(.*?)\.(jpe?g|png)", item, re.I):
            continue
        image_169(os.path.join(path, item), final_dir)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("😊: 169_batch.py [dir_name]")
        exit(-1)
    img_dir = sys.argv[1]
    if not os.path.isdir(img_dir):
        print("{} not directory".format(img_dir))
        exit(-1)
    main(img_dir)
