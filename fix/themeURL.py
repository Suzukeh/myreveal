import sys
import pathlib
import os

args = sys.argv

arg = args[0]

if (arg == '--help') or (arg == '-h'):
    print("fix custom CSS path\n\t> themeURL.py foo.html")
    sys.exit()


htmlpath = pathlib.Path("./../theme/")
