#!/usr/bin/env python3

import os, re, sys
import subprocess

if len(sys.argv)-1 == 0:
    print("Argument missing: [xdg desktop file]")
    exit()

file = sys.argv[1]
# i.e. "quickconvert.desktop"

f = open(file, "r")
for line in f.readlines():
    if "Comment=" in line:
        orig = line.split("=")[1]
        print(orig)
    if "Comment[" in line:
        m = re.search(r"\[([A-Za-z0-9_]+)\]", line)
        lang = m.group(1)
        #result = os.system("trans -b :" + lang + " \"" + orig + "\"")
        result = subprocess.run(["trans", "-b", ":" + lang, orig.strip()],
            stdout=subprocess.PIPE, text=True, check=True)
        part1 = line.split("=")[0]
        print(part1 + "=" + result.stdout.strip()) #.decode("utf-8"))