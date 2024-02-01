from tkinter.ttk import Notebook
from tkinter import BOTH, PhotoImage, Label, Frame, Text, Tk, Button
from tkinter import LEFT, TOP, StringVar
from tkinter import N, NE, NO, W, E, S, CENTER, END
from core.widgets.widget_builder import WidgetBuilder
from features.file_generator.access.tkinter.widgets.image_widget import ImageWidget
from PIL import Image, ImageTk

# help(Notebook)
# help(PhotoImage)


class TabsWidget(Notebook, WidgetBuilder):
    name = "TabsWidget"

    def __init__(self, master=None, cnf={}, **kw):
        Notebook.__init__(self)
        WidgetBuilder.__init__(self, cnf)
        self.__name__ = "Notebook"
        self.tabs_values = []
        self._build()

    def _build(self):
        imagen_pillow = Image.open("assets/images/class.bmp")
        imagen = ImageTk.PhotoImage(imagen_pillow)

        template = {
            "pack": {
                "side": LEFT,
                "expand": True,
                "fill": BOTH,
            },
            "children": [
                {
                    "id": "text_class",
                    "type": Text,
                    "pack": {
                        "side": TOP,
                        "expand": False,
                        "fill": BOTH,
                    },
                },
                {
                    "id": "text_attributes",
                    "type": Text,
                    "pack": {
                        "side": LEFT,
                        "expand": False,
                        "fill": BOTH,
                    },
                },
            ],
        }
        self.render(self, template)
        self.tabs_values.append(self.components["text_class"])
        self.tabs_values.append(self.components["text_attributes"])
        self.add(
            self.components["text_class"],
            text="Entidad",
            compound=LEFT,
            padding=20,
        )
        self.add(
            self.components["text_attributes"],
            text="Atributos",
            compound=TOP,
            padding=20,
        )

    def get_value(self, index):
        return self.tabs_values[index].get("1.0", END)

    def set_value(self, index, value):
        self.tabs_values[index].delete("1.0", END)
        self.tabs_values[index].insert("1.0", value)
        pass
