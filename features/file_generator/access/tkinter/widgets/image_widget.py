from tkinter.ttk import Notebook
from tkinter import BOTH, PhotoImage, Label, Frame, Text, Tk, Button, Widget
from tkinter import LEFT, TOP, StringVar
from tkinter import N, NE, NO, W, E, S, CENTER, END
from core.widgets.widget_builder import WidgetBuilder

# help(Notebook)
# help(PhotoImage)


class ImageWidget(Label, WidgetBuilder):
    name = "ImageWidget"

    def __init__(self, master=None, cnf={}, **kw):
        Label.__init__(self,master,self.name)
        WidgetBuilder.__init__(self, cnf)
        print("MIREMOS ")
        print(cnf)
        print(kw)
        self.cnf = cnf
        self._build()

    def _build(self):
        template = {
            "children": [
                {
                    "id": f"{self.name}.frame_class",
                    "type": Frame,
                    "children": [
                        {
                            "id": "text_class",
                            "type": Text,
                            # "properties": {"height": 20, "width": 50},
                            "pack": {
                                "side": TOP,
                                "expand": True,
                                "fill": BOTH,
                            },
                        },
                    ],
                },
            ],
        }
        self.render(self, template)
