from core.helpers.token_extractor.tokens_extractor import TokensExtractor
from features.file_generator.domain.use_cases.code_generator_use_case import CodeGeneratorUseCase
from functools import reduce
import json
import sys

from features.file_generator.domain.models.models import Class
class FileGeneratorCMD:
    '''
    -m=F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\model.json -t=F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\parser.dart -f=F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\tokens.json 

    -m=F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\model.json
    -t=F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\parser.dart
    -f=F:\Hasta 05-05-2020\Documentos\Python Projects\GCA\implementations\ma\tokens.json 
    '''
    def __init__(self, argv):
        self.argv = argv
        extractor = TokensExtractor()
        self.generadorArchivos = CodeGeneratorUseCase(extractor)

    def init(self):
        file, *params = self.argv
        def _(x,y):
            with open(y[1].replace('\\','/'), 'r',encoding='utf-8') as t:
                content = t.read()
            x.update({y[0]: content})
            return x

        if(len(params) != 3):
            raise Exception("{}".format(str(len(params))))
        
        
        formatted_params = reduce(lambda x,y : _(x,y), list(map(lambda x: x.split('='), params)),{})
        class_instance = Class()
        class_instance.from_json(json.loads(formatted_params['-m']))
        data = self.generadorArchivos(
            class_instance,
            formatted_params['-t'],
            json.loads(formatted_params['-f']),
        )
        return data
