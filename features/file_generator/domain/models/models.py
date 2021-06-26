
class Class:
    ATTRIBUTE_KEY = 'attributes'
    PROPERTY_KEY = 'properties'
    def __init__(self):
        self.attributes = []
        self.__dict__[Class.ATTRIBUTE_KEY] = []
        self.__dict__[Class.PROPERTY_KEY] = {}
    
    def set_property(self, property_name,property_value):
        self.__dict__[Class.PROPERTY_KEY][property_name] = property_value

    def p(self,property_name):
        return self.__dict__[Class.PROPERTY_KEY][property_name]
    def add_attributes(self,attributes):
        self.__dict__[Class.ATTRIBUTE_KEY] = [attr for attr in attributes]
    
    def from_json(self,json_object):
        self.__dict__[Class.ATTRIBUTE_KEY] = []
        self.__dict__[Class.PROPERTY_KEY] = {}
        for key in json_object.keys():
            item = json_object[key]
            if not key == Class.ATTRIBUTE_KEY:
                self.set_property(key,item)
            else:
                for attr in item:
                    attr_instance = Attribute()
                    attr_instance.from_json(attr)
                    self.__dict__[Class.ATTRIBUTE_KEY].append(attr_instance)

class Attribute:
    def set_property(self, property_name,property_value):
        self.__dict__[property_name] = property_value

    def from_json(self,json_object):
        for key in json_object.keys():
            item = json_object[key]
            self.set_property(key,item)
