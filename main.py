from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import argparse
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

"""parsing and configuration"""

def parse_args():
    desc = "Simple Color Analyzer"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--clusters', type=int, default=5, help='How Many Cluster You Want?')
    parser.add_argument('--src', type=str, default='sample.jpg', help='What Is an Image Path?')
    parser.add_argument('--des', type=str, default='results', help='What Is The Result Folder Name?')

    return parser.parse_args()


def preprocess(raw):
    image = cv2.resize(raw, (900, 600), interpolation = cv2.INTER_AREA)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3)
    return image


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color


def analyze(img, args):
    clf = KMeans(n_clusters = args.clusters)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    plt.figure(figsize = (12, 8))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)

    plt.savefig(f'{args.des}/{os.path.basename(args.src).split(".")[0]}.png')
    print('===========================')
    print('Found the following colors:')
    for color in hex_colors:
        print(f'- {color}')
    print('===========================')


def main():
    args = parse_args()
    if args is None:
        exit()

    if not os.path.exists(args.des):
        os.makedirs(args.des)
        print('Result Directory Created Successfully!')

    image = cv2.imread(args.src)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    modified_image = preprocess(image)
    analyze(modified_image, args)

if __name__ == '__main__':
    main()
