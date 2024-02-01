from tkinter import (
    BOTH,
    BOTTOM,
    CENTER,
    E,
    END,
    LEFT,
    RIGHT,
    TOP,
    Y,
    Frame,
    Label,
    StringVar,
    Entry,
    Button,
    Text,
)
from tkinter import W
from tkinter import N, S
import json
from features.file_generator.access.tkinter.widgets.tabs_widget import TabsWidget
from core.widgets.widget_builder import WidgetBuilder


class ModelConfigWidget(Frame, WidgetBuilder):
    name = "LeftPanelWidget"

    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self)
        WidgetBuilder.__init__(self, cnf)
        self.status_var = StringVar()
        self.__name__ = "Frame"

        self._build()
        self._init_components()

    def _build(self):
        template = {
            "type": Frame,
            "pack": {
                "side": TOP,
                "expand": True,
                "fill": Y,
            },
            "properties": {"bg": "green"},
            "children": [
                # {
                #     "id": f"{self.name}.tab_widget",
                #     "type": TabsWidget,
                #     "pack": {
                #         "side": BOTTOM,
                #         "fill": BOTH,
                #         "expand": True,
                #     },
                # },
                {
                    "id": "button_status_widget",
                    "type": Frame,
                    "pack": {
                        "side": TOP,
                        "fill": BOTH,
                        "expand": False,
                    },
                    "properties": {"bg": "green"},
                    "children": [
                        {
                            "type": Button,
                            "properties": {
                                "textvariable": self.status_var,
                                "width": 10,
                                "text": "Evaluar",
                                "command": self.validate_json,
                                "fg": "black",
                                "bg": "#900",
                            },
                            "pack": {
                                "side": LEFT,
                                "fill": BOTH,
                                "expand": True,
                            },
                        },
                        {
                            "id": "status_widget",
                            "type": Entry,
                            "properties": {
                                "textvariable": self.status_var,
                                "width": 50,
                            },
                            "pack": {
                                "side": RIGHT,
                                "fill": BOTH,
                                "expand": True,
                            },
                        },
                    ],
                },
                {
                    "id": "seeeeetatus_widget",
                    "type": Frame,
                    "properties": {"bg": "purple"},
                    "pack": {
                        "side": BOTTOM,
                        "expand": True,
                        "fill": BOTH,
                    },
                    "children": [
                        {
                            "id": "class_container",
                            "type": Frame,
                            "pack": {
                                "side": TOP,
                                "expand": False,
                                "fill": Y,
                            },
                            "children": [
                                {
                                    "type": Label,
                                    "properties": {"text": "Clase"},
                                    "pack": {
                                        "side": TOP,
                                        "expand": False,
                                        "fill": BOTH,
                                    },
                                },
                                {
                                    "id": "text_class",
                                    "type": Text,
                                    "properties": {"height": 10},
                                    "pack": {
                                        "side": BOTTOM,
                                        "expand": False,
                                        "fill": BOTH,
                                    },
                                },
                            ],
                        },
                        {
                            "id": "attribute_container",
                            "type": Frame,
                            "properties": {"bg": "purple"},
                            "pack": {
                                "side": BOTTOM,
                                "expand": True,
                                "fill": Y,
                            },
                            "children": [
                                {
                                    "type": Label,
                                    "properties": {"text": "Atributos"},
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
        }
        self.render(self, template)

    def _init_components(self):
        self.init_values_json()

    def init_values_json(self):
        class_json = {
            "name": "service",
            "plural-name": "services",
            "company": "Fare",
            "table": "services",
            "imports": ["java.lang.String", "java.util.Date", "java.util.List"],
        }

        attributes_json = [
            {"name": "id", "column-name": "id", "type": "String"},
            {"name": "client-id", "column-name": "client_id", "type": "String"},
            {
                "name": "employee-ids",
                "column-name": "employee_ids",
                "type": "List<String>",
            },
            {"name": "date", "column-name": "date", "type": "Date"},
            {
                "name": "inner-observations",
                "column-name": "inner_observations",
                "type": "String",
            },
            {
                "name": "employee-observations",
                "column-name": "employee_observations",
                "type": "String",
            },
            {"name": "cost", "column-name": "cost", "type": "float"},
            {"name": "status", "column-name": "status", "type": "String"},
            {
                "name": "financial-status",
                "column-name": "financial_status",
                "type": "String",
            },
            {"name": "initial-hour", "column-name": "initial_hour", "type": "float"},
            {"name": "final-hour", "column-name": "final_hour", "type": "float"},
        ]

        self.components["text_attributes"].delete("1.0", END)
        self.components["text_attributes"].insert(
            "1.0", json.dumps(attributes_json, indent=2)
        )
        self.components["text_class"].delete("1.0", END)
        self.components["text_class"].insert("1.0", json.dumps(class_json, indent=2))

    def validate_json(self):
        response = ""
        index1 = self.components["text_attributes"].get("1.0", END)
        index0 = self.components["text_class"].get("1.0", END)

        try:
            response_json = json.loads(index0)
            formated_json = json.dumps(response_json, indent=2)
            self.components["text_class"].delete("1.0", END)

            self.components["text_class"].insert(
                "1.0", formated_json
            )
        except Exception as identifier:
            response += "Clase: " + str(identifier)
            
        try:
            response_json = json.loads(index1)
            formated_json = json.dumps(response_json, indent=2)
            self.components["text_attributes"].delete("1.0", END)

            self.components["text_attributes"].insert(
                "1.0", formated_json
            )
        except Exception as identifier:
            response += "Atributos: " + str(identifier)

        self.status_var.set(response)

    def get_class_representation(self):
        index0 = json.loads(self.components["text_class"].get("1.0", END))
        index1 = json.loads(self.components["text_attributes"].get("1.0", END))
        index0["attributes"] = index1
        return index0
