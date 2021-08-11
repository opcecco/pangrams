#!/bin/bash

cat sources/unixwords.txt | egrep '^[a-z]+$' | sort | uniq -i > full_wordlist.txt
wc -l full_wordlist.txt

cat sources/google-10000-english*.txt | egrep '^[a-z]+$' | sort | uniq -i | sort full_wordlist.txt - | uniq -i -d > common_wordlist.txt
wc -l common_wordlist.txt
