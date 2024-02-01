import sys
from features.file_generator.access.tkinter.views.file_generator.file_generator_view import FileGeneratorView
from features.file_generator.access.cmd.file_generator_cmd import FileGeneratorCMD
index = FileGeneratorView(1300, 800)
#index = FileGeneratorCMD(sys.argv)
data = index.init()
#with(open('data-result','w',encoding='utf-8')) as t:
#    t.write(data)