
import re
from core.helpers.token_extractor.constants import TOKEN_PATTERN, OPEN_CHARACTER, CLOSE_CHARACTER

class TokensExtractor:
    def __call__(self,content_file,cleaner =True):
        founded_tokens = re.findall(TOKEN_PATTERN,content_file)
        response = list(filter(lambda x : x != '',founded_tokens))
        if not cleaner:
            response = list(map(lambda x : '{}{}{}'.format(OPEN_CHARACTER.replace('\\',''),x,CLOSE_CHARACTER.replace('\\','')),response ))
        return response

# template = '''
#         hola <|griego|>
#         hola <|romano|>
#         '''
# a = TokensExtractor()
# b = a(template,False)
# for x in b:
#     print(x,len(x))

