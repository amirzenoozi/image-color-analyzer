from script.analyzer import preprocess, save_pie_chart

import argparse
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
    save_pie_chart(modified_image, args)

if __name__ == '__main__':
    main()
