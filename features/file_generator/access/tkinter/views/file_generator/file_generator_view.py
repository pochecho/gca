from tkinter import BOTH, BOTTOM, LEFT, RIGHT, TOP, X, Y, Entry
from .imports.file_generator_view_imports import *
import pprint


class FileGeneratorView(Window, WidgetBuilder):
    def __init__(self, width, height):
        Window.__init__(self, width, height)
        WidgetBuilder.__init__(self, {})
        self.controller = FileGeneratorController(self)
        self._build()

    def hola(self, event):
        print(" - - ", event)
        if "FileGeneratorView.leftPanel" in self.components:
            t: Entry = self.components["FileGeneratorView.leftPanel"].components[
                "status_widget"
            ]
            new_width = event.width
            new_height = event.height
            if new_width < self.width:
                n = int(new_width * 0.5)
                print(new_width, new_height)
                print(n)
                pprint.pprint(t)

    def _build(self):
        # self.add_handler(self.hola)

        template = {
            "children": [
                {
                    "type": ModelConfigWidget,
                    "id": f"{self.controller.name}.leftPanel",
                    "pack": {
                        "side": LEFT,
                        "fill": Y,
                    },
                },
                {
                    "type": Frame,
                    "id": f"{self.controller.name}.general_panel",
                    "pack": {
                        "side": RIGHT,
                        "expand": True,
                        "fill": BOTH,
                    },
                    "children": [
                        {
                            "type": Frame,
                            "id": f"{self.controller.name}.inputs_panel",
                            "properties": {},
                            "children": [
                                self.controller.create_panel_routes_configuration(
                                    "Templates", None, 0, "#234"
                                ),
                                self.controller.create_panel_routes_configuration(
                                    "Tokens", None, 1, "#564"
                                ),
                                self.controller.create_panel_routes_configuration(
                                    "Paths", None, 2, "#20a"
                                ),
                            ],
                            "pack": {
                                "side": TOP,
                                "fill": BOTH,
                            },
                        },
                        {
                            "type": Frame,
                            "properties": {
                                "bg": "",
                            },
                            "pack": {
                                "side": BOTTOM,
                                "expand": True,
                                "fill": BOTH,
                            },
                            "children": [
                                {
                                    "type": Button,
                                    "properties": {
                                        "command": self.controller.generate_files,
                                        "text": "Generar",
                                        "bg": "#099",
                                        "fg": "black",
                                    },
                                    "pack": {
                                        "side": TOP,
                                        "fill": X,
                                        "padx": 15,
                                        "pady": 15,
                                    },
                                },
                                {
                                    "type": Frame,
                                    "id": "files_container",
                                    "properties": {"bg": ""},
                                    "children": [],
                                    "pack": {
                                        "side": BOTTOM,
                                        "expand": True,
                                        "fill": BOTH,
                                    },
                                },
                            ],
                        },
                    ],
                },
            ],
            # "grid": {"row": 0, "column": 0},
        }
        self.render(self.window, template)
