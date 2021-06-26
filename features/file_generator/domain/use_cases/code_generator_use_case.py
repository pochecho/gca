import json
import os
class CodeGeneratorUseCase:
    """docstring for generadorArchivos"""

    def __call__(self,model,template,functions):
        """
            The model parameters contains all data from your model, this is the class you are building.
            It is a json
            Example:
            {
                "properties": {
                    "name":"cat"
                },
                "attributes": {
                    "name":"cat"
                }

            }
            The template parameter is the layout to generate new files.
                hola {[griego]}
                hola {[romano]}
        """
        self.content = template
        token_list = self.token_extractor(template)
        for token in token_list:           
            function_to_eval = functions[token]
            try:
                exec(function_to_eval)
            except SyntaxError as identifier:
                print("Error",identifier)
        return self.content
        

    def __init__(self,token_extractor):
        self.token_extractor = token_extractor

