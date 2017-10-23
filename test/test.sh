#!/bin/bash

# (deprecated) Not removing the tags; dirty
# python WikiExtractor.py -b 1000M -o extracted zhwiki-latest-pages-articles.xml.bz2 > output.txt

if [ -f test_wiki.zh.text ]; then
    echo "Cleaning corpus..."
    python3 ../clean_corpus.py test_wiki.zh.text > test_clean_corpus.txt

    echo "Converting script..."
    opencc -i test_clean_corpus.txt -o test_corpus.txt -c ../s2t.conf

    # Split files
    echo "Splitting corpus..."
    python3 ../split_file.py test_corpus.txt -o test_corpus.txt --chunksize 1 # 1KB

    # Join files
    echo "Joining files..."
    python3 ../join_file.py test_corpus -o test_corpus_join.txt
    
    # Test
    if diff test_corpus.txt test_corpus_join.txt
    then
        echo "Pass test"
    else
        echo "Split/join files differ"
    fi
fi
