import os
import sys

file, *args = sys.argv
tasks = {
    'clean': lambda : os.system('pyclean .'),
    'start': lambda : os.system('py index.py'),
    'start:cmd': lambda : os.system('py index.py -m="F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\model.json" -t="F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\parser.dart" -f="F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\\tokens.json"'),
    'build': lambda : os.system('pyinstaller --onefile index.py')
}
if args != [] and args[0] in tasks.keys():
    tasks[args[0]]()

