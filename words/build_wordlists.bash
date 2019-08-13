#!/bin/bash

sed "s/[^A-Za-z'-]//g" sources/words_alpha.txt | sort | uniq -i > full_wordlist.txt
wc -l full_wordlist.txt

cat sources/google-10000-english*.txt | sed "s/[^A-Za-z'-]//g" | sort | uniq -i | sort full_wordlist.txt - | uniq -i -d > common_wordlist.txt
wc -l common_wordlist.txt
