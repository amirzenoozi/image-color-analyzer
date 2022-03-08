from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os

def preprocess(raw):
    image = cv2.resize(raw, (900, 600), interpolation = cv2.INTER_AREA)                                          
    image = image.reshape(image.shape[0]*image.shape[1], 3)
    return image


def rgb_to_hex(rgb_color):
    hex_color = "#"
    for i in rgb_color:
        hex_color += ("{:02x}".format(int(i)))
    return hex_color

def save_pie_chart(img, args):
    color_labels, hex_colors = analyze(img, args)
    counts = Counter(color_labels)
    plt.figure(figsize = (12, 8))
    plt.pie(counts.values(), labels = hex_colors, colors = hex_colors)

    plt.savefig(f'{args.des}/{os.path.basename(args.src).split(".")[0]}.png')


def analyze(img, args):
    clustersCount = args or 5
    clf = KMeans(n_clusters = clustersCount)
    color_labels = clf.fit_predict(img)
    center_colors = clf.cluster_centers_
    counts = Counter(color_labels)
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]

    print('===========================')
    print('Found the following colors:')
    for color in hex_colors:
        print(f'- {color}')
    print('===========================')

    return color_labels, hex_colors
