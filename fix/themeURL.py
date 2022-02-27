import sys
from pathlib import Path
import os


def toquit():
    print("Continue? (y/n)")
    str = input()
    if str == "y":
        print("...")
    elif str == "n":
        print("Exit")
        sys.exit()
    else:
        print("Input y/n")
        toquit()


def fix_css_path(arg):
    htmllist = arg.glob("**/*.html")
    for htmlpath in htmllist:
        content = htmlpath.read_text()
        for csspath in redict.keys():
            if content.find(csspath) != -1:
                print(str(htmlpath) + ": " + str(csspath) +
                      " -> " + str(redict[csspath]))
                content = content.replace(str(csspath), str(redict[csspath]))
                htmlpath.write_text(content)


redict = {"href=\"/_assets/theme/": "href=\"./../_assets/theme/",
          "href=\"./dist/theme/": "href=\"./../dist/theme/"}


args = sys.argv

arg = Path(args[1])


if (arg == '--help') or (arg == '-h'):
    print("fix custom CSS path\n\t> themeURL.py docs/")
    sys.exit()

fix_css_path(arg)
