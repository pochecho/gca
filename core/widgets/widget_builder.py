from random import randint
from copy import deepcopy

TYPE_NOT_FOUND_EXCEPTION = 'The "type" property was not found in the configuration.'
COMPONENT_NOT_FOUND_EXCEPTION = (
    "The component according with the given id does not exist in the TREE."
)
ALLOWED_GRID_PROPERTIES = (
    "column",
    "columnspan",
    "in",
    "ipadx",
    "ipady",
    "padx",
    "pady",
    "row",
    "rowspan",
    "sticky",
)
ALLOWED_PACK_PROPERTIES = (
    "side",
    "fill",
    "expand",
    "anchor",
    "after",
    "padx",
    "pady",
    "ipadx",
    "ipady",
)

ALLOWED_PROPERTIES_BY_COMPONENT = {
    "Frame": [
        "bg",
        "bd",
        "width",
        "height",
        "cursor",
        "highlightbackground",
        "highlightcolor",
        "highlightthickness",
        "relief",
    ],
    "Notebook": [
        "bg",
        "bd",
        "width",
        "height",
        "cursor",
        "highlightbackground",
        "highlightcolor",
        "highlightthickness",
        "relief",
    ],
    "Label": [
        "image",
        "text",
    ],
    "Button": [
        "activebackground",
        "activeforeground",
        "bg",
        "background",
        "bd",
        "command",
        "fg",
        "font",
        "height",
        "highlightcolor",
        "image",
        "justify",
        "padx",
        "pady",
        "relief",
        "state",
        "text",
        "underline",
        "width",
        "wraplength",
    ],
    "Entry": [
        "bg",
        "bd",
        "command",
        "cursor",
        "font",
        "exportselection",
        "fg",
        "highlightcolor",
        "Justify",
        "relief",
        "selectbackground",
        "selectborderwidth",
        "selectforeground",
        "show",
        "State",
        "width",
        "xscrollcommand",
        "set",
        "textvariable",
        "insert",
    ],
    "ImageWidget": ["path"],
    "Text": [
        "bg",
        "fg",
        "bd",
        "height",
        "width",
        "font",
        "cursor",
        "insetofftime",
        "insertontime",
        "padx",
        "pady",
        "state",
        "highligththickness",
        "insertionwidth",
        "relief",
        "yscrollcommand",
        "xscrollcommand",
    ],
}


class WidgetBuilder:
    def __init__(self, cnf):
        """
        Each component will have the next structure:

        {
            "main_frame": {
                "data":{},
                "widget":{}
                "children":[]
            }
        }
        """
        self.components = {}
        self.cnf = cnf
        print(9, self.cnf)

    def render(self, parent, configuration):
        new_id = self.get_radmon_id()
        id = self.get_property("id", configuration, new_id)
        children = self.get_property("children", configuration)
        constructor = self.get_property("type", configuration)

        if id is None or constructor is None:
            if children is not None:
                if hasattr(parent, "__name__"):
                    name = str(parent.__name__)
                    print(parent, parent.cnf, 78)
                    parent.config(parent.cnf)
                for child in children:
                    self.__render(parent, child, self.components)

        elif id is not None or constructor is not None:
            self.__render(parent, configuration, self.components)

    def __render(self, parent, configuration, components):
        new_id = self.get_radmon_id()
        id = self.get_property("id", configuration, new_id)
        children = self.get_property("children", configuration)
        constructor = self.get_property("type", configuration)
        properties = self.get_property("properties", configuration)
        name = str(constructor.__name__)

        valid_properties = (
            ALLOWED_PROPERTIES_BY_COMPONENT[name]
            if name in ALLOWED_PROPERTIES_BY_COMPONENT
            else None
        )
        if constructor != None:
            cleaned_properties = {}
            if properties is not None:
                if valid_properties is not None:
                    cleaned_properties = self.__clean_not_allowed_properties(
                        id, properties, valid_properties
                    )
                else:
                    # indica que el objeto no está mapeado, en el objeto de propiedades peritidas por compoente
                    #  es decir toca agregarlo en este objeto ALLOWED_PROPERTIES_BY_COMPONENT
                    pass
            # print(id,cleaned_properties)
            components[id] = constructor(parent, cleaned_properties)
            components[id].config(cleaned_properties)

            self.__configure_position(id, configuration, components)
            if children is not None:
                for child in children:
                    self.__render(components[id], child, components)
        else:
            raise Exception(TYPE_NOT_FOUND_EXCEPTION)

    def __configure_position(self, id, configuration, components):
        constructor = self.get_property("type", configuration)
        name = str(constructor.__name__)
        if name == "PhotoImage":
            components[id].grid(column=0, width=0)
        else:
            grid_place_method = (
                configuration["grid"] if "grid" in configuration else None
            )
            pack_place_method = (
                configuration["pack"] if "pack" in configuration else None
            )

            if grid_place_method is not None or pack_place_method is not None:
                if grid_place_method is not None:
                    cleaned_properties = self.__clean_not_allowed_properties(
                        id, grid_place_method, ALLOWED_GRID_PROPERTIES
                    )
                    components[id].grid(cleaned_properties)
                if pack_place_method is not None:
                    cleaned_properties = self.__clean_not_allowed_properties(
                        id, pack_place_method, ALLOWED_PACK_PROPERTIES
                    )
                    components[id].pack(cleaned_properties)
            else:
                components[id].pack()

    def __clean_not_allowed_properties(self, id, config, allowed_properties):
        formatted_data = {}
        if len(config.keys()) == 0:
            return formatted_data

        for allowed_property in allowed_properties:
            allowed_property_value = self.get_property(allowed_property, config)
            if allowed_property_value is not None:
                formatted_data[allowed_property] = allowed_property_value
        return formatted_data

    def get_property(self, property, configuration, default=None):
        if property in configuration:
            return configuration[property]
        else:
            return default

    def add_listener(self, id, listener, callback):
        component = self.components[id] if id in self.components else None
        if component is None:
            raise Exception(COMPONENT_NOT_FOUND_EXCEPTION)
        component.config({"command": callback})

    def get_radmon_id(self):
        return str(randint(10000, 99000))
