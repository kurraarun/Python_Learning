

import os
from os import path
import shutil


if path.exists("Webpage.txt"):
   print("File exists")
   src = path.realpath("Webpage.txt")

   dst = src + ".bak"

   shutil.copy(src, dst)
   shutil.copystat(src, dst)


