import os
import argparse


# Parse args
parser = argparse.ArgumentParser(description='Join files')
parser.add_argument('input', metavar='FI', type=str, 
                    help='name of folder with files to be joined')
parser.add_argument('--output', '-o', metavar='FO', type=str,
                    help='output file name')

args = parser.parse_args()


# Join file
dname = args.input
print(args.output)
foutname = args.output

def sortFile(filename):
    try:
        return int(filename.split('_')[0])
    except:
        return filename

with open(foutname, 'wb') as fout:
    filenames = sorted(os.listdir(dname), key=sortFile)
    for filename in filenames:
        print('Joining {}/{}...'.format(dname, filename))
        with open('{}/{}'.format(dname, filename), 'rb') as fin:
            fout.write(fin.read())
