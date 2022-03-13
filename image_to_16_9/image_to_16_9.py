# -*- coding: UTF-8 -*-
import os
import sys

import cv2


def main(source_img_path: str):
    img = cv2.imread(source_img_path)
    height, width, _ = img.shape
    new_height = int(width // 16 * 9)
    gap = (height - new_height) // 2
    cropped = img[gap:new_height + gap, 0:width]
    final_path = '/tmp/result_{}'.format(source_img_path.split('/')[-1])
    cv2.imwrite(final_path, cropped, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
    print(final_path)


if __name__ == '__main__':
    img_path = None
    try:
        img_path = sys.argv[1]
    except:
        print("python3 circle_image.py xxx.png")

    if img_path.startswith('file://'):
        img_path = img_path[6:]

    if '%20' in img_path:
        img_path = img_path.replace('%20', ' ')

    if not os.path.exists(img_path):
        print("img_path: {} not exists".format(img_path))
        exit(-1)
    main(img_path)
