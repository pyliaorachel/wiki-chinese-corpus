import os
import argparse


# Parse args
parser = argparse.ArgumentParser(description='Split file nto smaller chunks')
parser.add_argument('input', metavar='FI', type=str, nargs=1, 
                    help='file to be split')
parser.add_argument('--output', '-o', metavar='FO', type=str, nargs=1,
                    help='output file name')
parser.add_argument('--chunksize', metavar='S', type=float, default=50000,
                    help='small chunk size (KB)')

args = parser.parse_args()


# Make new folder for split files
dname, _ = os.path.splitext(args.output[0])
if not os.path.exists(dname):
    os.makedirs(dname)

# Split file
finname = args.input[0]
foutname = args.output[0]
chunk_size = args.chunksize * 1000
read_size = 0
i = 0

with open(finname, 'rb') as fin:
    for j, line in enumerate(fin):
        if read_size == 0:
            fout = open('{}/{}_{}'.format(dname, i, foutname), 'wb')

        line_size = len(line)

        fout.write(line)
        read_size += line_size

        # if exceeding chunk size limit, start a new file
        if read_size > chunk_size:
            print('Written {}B to {}...'.format(read_size, fout.name))
            fout.close()
            read_size = 0
            i += 1

    if read_size != 0:
        print('Written {}B to {}...'.format(read_size, fout.name))
        fout.close()
