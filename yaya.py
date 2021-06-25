class Class(object):
    def __init__(self):
        self.attributes = []
    
    def set_property(self, property_name,property_value):
        self.__dict__[property_name] = property_value

    def add_attributes(self,attributes):
        self.attributes = [attr for attr in attributes]




a = Class()
a.add_attributes([1,3,4,5,6,7])
print(a.__dict__)