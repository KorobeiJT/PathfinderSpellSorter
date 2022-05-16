import json
import re
from os import listdir
from os.path import isfile, join
import shutil

name = "triple aspect.txt"

file = open(name, mode = 'r', encoding = 'utf-8')
lines = file.readlines()
file.close()

# info = ""
# for line in lines:
#     line = line.rstrip('\n')
#     if("[École] " in line):
#         res["École"] = line.lstrip("[École] ")


    