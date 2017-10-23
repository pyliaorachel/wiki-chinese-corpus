#!/bin/bash

# (deprecated) Not removing the tags; dirty
# python WikiExtractor.py -b 1000M -o extracted zhwiki-latest-pages-articles.xml.bz2 > output.txt

if [ ! -f wiki.zh.text ]; then
    echo "Processing raw Wiki dump..."
    python3 process_wiki.py zhwiki-latest-pages-articles.xml.bz2 wiki.zh.text
fi

echo "Cleaning corpus..."
python3 clean_corpus.py wiki.zh.text > clean_corpus.txt

echo "Converting script..."
opencc -i clean_corpus.txt -o corpus.txt -c s2t.conf

# Split files if needed
# echo "Splitting corpus..."
# python3 split_file.py corpus.txt -o corpus.txt --chunksize 50000 # 50MB

# Join files if needed
# echo "Joining files..."
# python3 join_file.py corpus -o corpus.txt
