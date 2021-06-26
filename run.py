import os
import sys

file, *args = sys.argv
print(args)
tasks = {
    'clean': lambda : os.system('pyclean .'),
    'start': lambda : os.system('py index.py'),
    'build': lambda : os.system('pyinstaller --onefile index.py')
}
if args != [] and args[0] in tasks.keys():
    tasks[args[0]]()
