
import sys
from pathlib import Path
import os

redict = {"href=\"/_assets/theme/": Path("./_assets/theme/"),
          "href=\"./dist/theme/": Path("./dist/theme/")}

args = sys.argv

arg = Path(args[1])

print(arg)

themepath = Path("./_assets/theme")
print(themepath)

if (arg/themepath).exists():
    print("Custom theme exists")
else:
    print("Custom theme not exists")
    sys.exit()

htmllist = arg.glob("**/*.html")
for htmlpath in htmllist:
    print(htmlpath)
    content = htmlpath.read_text()
    for csspath in redict.keys():
        if content.find(csspath) != -1:
            print(str(arg / redict[csspath]))
            relcss = Path(os.path.relpath(
                arg / redict[csspath], htmlpath.parent))
            reptext = "href=\"./" + str(relcss)
            print(str(htmlpath) + ": " + str(csspath) + " -> " + str(reptext))
            #content = content.replace(str(csspath), str(reptext))
            # htmlpath.write_text(content)
