#!/usr/bin/env bash

mv wordlist.merged.json wordlist
gzip wordlist
mv wordlist.gz wordlist.merged.bin