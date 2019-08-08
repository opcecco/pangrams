#!/bin/bash

pushd sources
sed "s/[^A-Za-z'-]//g" 2of12inf.txt | sort | uniq -i > ../full_wordlist.txt
cat google-10000-english*.txt | sed "s/[^A-Za-z'-]//g" | sort | uniq -i | sort ../full_wordlist.txt - | uniq -i -d > ../common_wordlist.txt
popd
