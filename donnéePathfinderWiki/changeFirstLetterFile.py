import json
import re
from os import listdir
from os.path import isfile, join
import shutil

src = "C:\\Users\lapii\Desktop\donnéePathfinderWiki\Pathfinder-RPG"
dst = "C:\\Users\lapii\Desktop\donnéePathfinderWiki\PFRPGlower"
onlyfiles = [f for f in listdir(src) if isfile(join(src, f))]

for file in onlyfiles:
    sf = src +"\\" +file
    df = dst +"\\" +file.lower()
    shutil.copy(sf,df)