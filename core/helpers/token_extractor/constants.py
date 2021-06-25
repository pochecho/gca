OPEN_CHARACTER = r'\{\['
CLOSE_CHARACTER = r'\]\}'
TOKEN_PATTERN = r'{}([\w]+){}'.format(OPEN_CHARACTER,CLOSE_CHARACTER)


ATTRIBUTE_KEY = 'attributes'
PROPERTY_KEY = 'properties'