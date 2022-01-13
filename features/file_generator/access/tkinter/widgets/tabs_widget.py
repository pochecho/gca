from tkinter.ttk import Notebook
from tkinter import PhotoImage, Label, Frame, Text, Tk, Button
from tkinter import LEFT, TOP, StringVar
from tkinter import N, NE, NO, W, E, S, CENTER, END
from core.widgets.widget_builder import WidgetBuilder

# help(Notebook)
#help(PhotoImage)

class TabsWidget(Notebook,WidgetBuilder):
    name = 'TabsWidget'
    def __init__(self, master=None, cnf={}, **kw):
        Notebook.__init__(self)
        WidgetBuilder.__init__(self)
        self.tabs_values = []
        self._build()

    def _build(self):
        template = {
            
            'children': [
                
                {
                    'id': '{}.frame_class'.format(self.name),
                    'type': Frame,
                    
                    'children': [
                        
                        {
                            'id': 'text_class',
                            'type': Text,
                            'properties': {
                                'height': 20,
                                'width': 50
                            },
                            'grid': {
                                'row': 0,
                                'column': 0,
                            }
                        },
                        
                        # {
                        #     'id': 'image_class',
                        #     'type': PhotoImage,
                        #     'properties': {
                        #         'file': 'assets/images/class.png'
                        #     }
                        # },
                    ],
                    'grid': {
                        'row': 0,
                        'column': 0,
                        # 'sticky': N,
                        'padx': 5,
                        'pady': 5
                    }
                },
                {
                    'id': 'frame_attributes',
                    'type': Frame,
                    'properties': {
                    },
                    'children': [
                        {
                            'id': 'text_attributes',
                            'type': Text,
                            'properties': {
                                'height': 20,
                                'width': 50
                            },
                            'grid': {
                                'row': 0,
                                'column': 0,
                                # 'sticky': N,
                                'padx': 5,
                                'pady': 5
                            }
                        },
                        
                        # {
                        #     'id': 'image_attributes',
                        #     'type': PhotoImage,
                        #     'properties': {
                        #         'file': 'assets/images/attributes.png'
                        #     }
                        # }
                    ],
                    'grid': {
                        'row': 0,
                        'column': 1
                    },
                }
            ],
        }
        self.render(self,template)
        self.tabs_values.append(self.components['text_class'])
        self.tabs_values.append(self.components['text_attributes'])
        # print(self.tabs_values)
        self.add(
            self.components['{}.frame_class'.format(self.name)],
            text="Class",
            compound=TOP,
            padding=20
        )
        self.add(
            self.components['frame_attributes'],
            text="Attributes",
            compound=TOP,
            padding=20
        )

    # def create_panel(self):
        # pass
        # self.web_label = self.create_inside_panel(self)
        # self.forum_label = self.create_inside_panel(self)

        # self.image_class = PhotoImage(file="assets/images/class.png")

        # self.add(self.web_label, text="Class",
                #  image=self.components['image_class'], compound=TOP, padding=20)

        # self.object_image = PhotoImage(file="assets/images/attributes.png")
        # self.add(self.forum_label, text="Attributes",
                #  image=self.components['image_class'], compound=TOP, padding=20)

    # def create_inside_panel(self, parent):
        # panel = Frame(parent)
        # text_area = Text(panel, height=20, width=50)
        # func = lambda x : self.evaluate[len(self.tabs_values)]
        # text_area.tag_bind("Enter>",func =  func)
        # self.tabs_values.append(text_area)
        # text_area.grid(row=0,column=0)
        # return panel
        # pass

    def get_value(self, index):
        return self.tabs_values[index].get('1.0', END)

    def set_value(self, index, value):
        # print()
        # print()
        # print()
        # print(self.tabs_values[index].delete)
        # print()
        # print()
        # print(self.components)
        self.tabs_values[index].delete('1.0', END)
        self.tabs_values[index].insert('1.0', value)
        pass
