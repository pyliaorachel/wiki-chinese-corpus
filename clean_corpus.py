import argparse
import re


# Parse args
parser = argparse.ArgumentParser(description='Clean Chinese corpus')
parser.add_argument('filename', metavar='F', type=str,
                    help='file to be cleaned')

args = parser.parse_args()


# Clean corpus
with open(args.filename) as f:
    for line in f:
        for c in re.findall(r'[\u4e00-\u9fff|\s]+', line):
            print(c, end='')
        print('')
