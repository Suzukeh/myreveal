import sys
from pathlib import Path
import os


args = sys.argv

arg = os.path.abspath(args[1])

if (arg == '--help') or (arg == '-h'):
    print("fix custom CSS path\n\t> themeURL.py foo.html")
    sys.exit()


htmlpath = Path(arg)
print(htmlpath)

content = htmlpath.read_text()
content = content.replace('href=\"/_assets/theme/',
                          'href=\"./../_assets/theme/')
htmlpath.write_text(content)
