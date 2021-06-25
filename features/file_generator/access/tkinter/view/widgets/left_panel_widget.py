from tkinter import Frame, StringVar, Entry, Button
import json
from features.file_generator.access.tkinter.view.widgets.tabs_widget import TabsWidget
class LeftPanelWidget(Frame):
    def __init__(self,root,**kw):
        super(LeftPanelWidget,self).__init__()
        self.status_var = StringVar()
        self.components = {}
        self._init_components()

    def _init_components(self):

        self.components['main_widget'] = Frame(self,width=70)
        self.components['main_widget'].grid(column=0, row=0,padx=5,pady=5)

        self.components['status_widget'] = Entry(self.components['main_widget'],textvariable = self.status_var,width=70)
        self.components['status_widget'].grid(column=0, row=0,padx=5,pady=5)
        
        self.components['tab_widget'] = TabsWidget(self)
        self.components['tab_widget'] .grid(column=0,row=1)
        self.components['button_status_widget'] = Button(self.components['main_widget'],text='Eval',command = self.validate_json)
        self.components['button_status_widget'].grid(column=1, row=0,padx=5,pady=5)
    
        self.init_values_json()
    def init_values_json(self):
        class_json = {
                        "name": "vehicle",
                        "name-plural": "vehicles",
                        "display-name": "Vehículo",
                        "folder": "vehicle",
                        "widget-name": "layout-bds-widget"
                    }
        
        attributes_json =[
                    {
                        "name":"brand",
                        "display-name": "Marca",
                        "is-required": False,
                        "type": "string",
                        "encapsulation": "private"
                    },
                    {
                        "name":"model",
                        "display-name": "Model",
                        "is-required": False,
                        "type": "string",
                        "encapsulation": "private"
                    },
                    {
                        "name":"color",
                        "display-name": "Color",
                        "is-required": False,
                        "type": "string",
                        "encapsulation": "private"
                    }
                ]

        
        self.components['tab_widget'].set_value(1,json.dumps(attributes_json,indent=2))
        self.components['tab_widget'].set_value(0,json.dumps(class_json,indent=2))


    def validate_json(self):
        response = ''
        index0 =  self.components['tab_widget'].get_value(0)
        index1 =  self.components['tab_widget'].get_value(1)

        try:
            response_json = json.loads(index0)
            formated_json = json.dumps(response_json,indent=2)
            self.components['tab_widget'].set_value(0,formated_json)
        except Exception as identifier:
            response += '0: '+str(identifier)
        

        try:
            response_json = json.loads(index1)
            formated_json = json.dumps(response_json,indent=2)
            self.components['tab_widget'].set_value(1,formated_json)
        except Exception as identifier:
            response += '1: '+ str(identifier)


        self.status_var.set(response)

    def get_class_representation(self):
        index0 =  json.loads(self.components['tab_widget'].get_value(0))
        index1 =  json.loads(self.components['tab_widget'].get_value(1))
        index0['attributes'] = index1
        return index0