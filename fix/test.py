
import sys
from pathlib import Path
import os

redict = {"href=\"/_assets/theme/": "href=\"./../_assets/theme/",
          "href=\"./dist/theme/": "href=\"./../dist/theme/"}

args = sys.argv

arg = Path(args[1])

print(arg)

for htmlpath in arg.glob("**/*.html"):
    print(htmlpath)
    content = htmlpath.read_text()
    for csspath in redict.keys():
        if csspath in content:
            print(csspath)
