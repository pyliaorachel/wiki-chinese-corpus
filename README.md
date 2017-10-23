# Wiki Chinese Corpus

Clean Chinese corpus of Wikipedia dump.  

[Original data](http://linguatools.org/tools/corpora/wikipedia-monolingual-corpora/)

- `wiki.zh.text` (with [`process_wiki.py`](https://github.com/panyang/Wikipedia_Word2vec/blob/master/v1/process_wiki.py))
  - Converted/extracted XML to text
- `clean_corpus.txt` (with `clean_corpus.py`)
  - Non-Chinese charaters removed
  - Spaces kept
- `corpus.txt` (with [Opencc](https://github.com/BYVoid/OpenCC))
  - Convert script from Simplified Chinese to Traditional Chinese (`s2t.conf` configuration file)
  - Other configuration files can be found in their website

## Utilities

- `process_wiki.py`: extract XML to text
    ```bash
    $ python3 process_wiki.py <raw-corpus> <output-f>
    ```

- `clean_corpus.py`: remove non-Chinese characters & keep spaces
    ```bash
    $ python3 clean_corpus.py <input-f> > <output-f>
    ```
    
- `split_file.py`: split large files into smaller chunks
    ```bash
    $ python3 split_file.py <file-to-split> -o <output-f-suffix> --chunksize <size-in-KB>

    # files output in <output-f-basename>/nn_<output-f-suffix>
    ```

- `join_file.py`: joing smaller chunks into a single large file
    ```bash
    $ python3 join_file.py <folder-with-files-to-join> -o <output-f>

    # files aggregated to <output-f>
    ```
    
- `run.sh`: run the entire process to generate `corpus.txt`
    ```bash
    $ ./run.sh
    ```
