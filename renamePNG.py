from glob import glob
from os import rename
from os import path
import sys

lst = glob('*.jpg')
lst.extend(glob('*.png'))
lst.extend(glob('*.jpeg'))

pre = sys.argv[1] if len(sys.argv) > 1 else ""
for i, name in enumerate(lst, 1):
    rename(name, pre + str(i) + path.splitext(name)[1])
