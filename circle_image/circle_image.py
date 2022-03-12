import os
from PIL import Image
import logging
import sys

logging.basicConfig(
    format='',
    level=logging.INFO
)


def main(source_img_path: str):
    path_dir_name = os.path.dirname(source_img_path)
    cir_path = os.path.join(path_dir_name, 'cir_img.png')
    ima = Image.open(source_img_path).convert("RGBA")
    size = ima.size

    r2 = min(size[0], size[1])
    if size[0] != size[1]:
        ima = ima.resize((r2, r2), Image.ANTIALIAS)

    r3 = int(r2 / 2)
    imb = Image.new('RGBA', (r3 * 2, r3 * 2), (255, 255, 255, 0))
    pima = ima.load()
    pimb = imb.load()
    r = float(r2 / 2)

    for i in range(r2):
        for j in range(r2):
            lx = abs(i - r)
            ly = abs(j - r)
            l = (pow(lx, 2) + pow(ly, 2)) ** 0.5
            if l < r3:
                pimb[i - (r - r3), j - (r - r3)] = pima[i, j]

    imb.save(cir_path)
    logging.info("result path: {}".format(cir_path))


if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except:
        help("python3 circle_image.py xxx.png")
