import os
import sys
import subprocess
command = 'py'
file = 'index.py'
params = '-m="F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\model.json" -t="F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\parser.dart" -f="F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\\tokens.json"'
script = '{} {} {}'.format(command, file,params)
# s2_out = subprocess.getoutput('{} {}'.format(file,params))
# s2_out = subprocess.Popen('{} {}'.format(file,params))
# print (s2_out)
# # print(data,5)
os.system(script)