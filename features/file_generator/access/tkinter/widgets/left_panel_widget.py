from tkinter import Frame, StringVar, Entry, Button
from tkinter import W
from tkinter import N
import json
from features.file_generator.access.tkinter.widgets.tabs_widget import TabsWidget
from core.widgets.widget_builder import WidgetBuilder

class LeftPanelWidget(Frame,WidgetBuilder):
    name = 'LeftPanelWidget'
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self)
        WidgetBuilder.__init__(self)
        self.status_var = StringVar()
        self._build()
        self._init_components()

    def _build(self):
        template = {
            'type':Frame,
            'properties': {
            },
            'children': [
                {
                    'id': '{}.main_widget'.format(self.name),
                    'type': Frame,
                    'grid':{
                        'column': 0,
                        'row': 0,
                        'padx': 5,
                        'pady': 5
                    },
                    'children': [
                        {
                            'id': 'status_widget',
                            'type': Entry,
                            'properties': {
                                'textvariable': self.status_var,
                                'width': 70
                            },
                            'grid': {
                                'column': 0,
                                'row': 0,
                                'padx': 5,
                                'pady': 5
                            }
                        },
                        {
                            'id': 'button_status_widget',
                            'type': Button,
                            'properties': {
                                'textvariable': self.status_var,
                                'width': 10,
                                'text': 'Eval',
                                'command' : self.validate_json,
                                'fg': 'black',
                                'bg': '#900'
                            },
                            'grid': {
                                'column': 1,
                                'row': 0,
                                'padx': 5,
                                'pady': 5
                            }
                        }

                    ]
                },
                {
                    'id': '{}.tab_widget'.format(self.name),
                    'type': TabsWidget,
                    'grid':{
                        'column': 0,
                        'row': 1,
                        'sticky': N
                    },

                }
               
            ],
            'grid': {
                'column': 0,
                'row': 0,
            }
        }
        self.render(self,template)

    def _init_components(self):
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

        
        self.components['{}.tab_widget'.format(self.name)].set_value(1,json.dumps(attributes_json,indent=2))
        self.components['{}.tab_widget'.format(self.name)].set_value(0,json.dumps(class_json,indent=2))


    def validate_json(self):
        response = ''
        index0 =  self.components['{}.tab_widget'.format(self.name)].get_value(0)
        index1 =  self.components['{}.tab_widget'.format(self.name)].get_value(1)

        try:
            response_json = json.loads(index0)
            formated_json = json.dumps(response_json,indent=2)
            self.components['{}.tab_widget'.format(self.name)].set_value(0,formated_json)
        except Exception as identifier:
            response += '0: '+str(identifier)
        

        try:
            response_json = json.loads(index1)
            formated_json = json.dumps(response_json,indent=2)
            self.components['{}.tab_widget'.format(self.name)].set_value(1,formated_json)
        except Exception as identifier:
            response += '1: '+ str(identifier)


        self.status_var.set(response)

    def get_class_representation(self):
        index0 =  json.loads(self.components['{}.tab_widget'.format(self.name)].get_value(0))
        index1 =  json.loads(self.components['{}.tab_widget'.format(self.name)].get_value(1))
        index0['attributes'] = index1
        return index0