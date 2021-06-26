from .imports.file_generator_view_imports import *

class FileGeneratorView(Window, WidgetBuilder):

    def __init__(self, width, height):
        Window.__init__(self, width, height)
        WidgetBuilder.__init__(self)
        self.controller = FileGeneratorController(self)
        self._build()

    def _build(self):
        template = {
            'children': [
                {
                    'type': LeftPanelWidget,
                    'id': '{}.leftPanel'.format(self.controller.name),
                    'grid': {
                        'row': 0,
                        'column': 0,
                        'sticky': E+W
                    }
                },

                {
                    'type': Frame,
                    'id': '{}.general_panel'.format(self.controller.name),
                    'grid': {
                        'row': 1,
                        'column': 1,
                        'sticky': N+S
                    },
                    'children': [
                        {
                            'type': Frame,
                            'id': '{}.inputs_panel'.format(self.controller.name),
                            'properties': {

                            },
                            'children': [
                                self.controller.create_panel_routes_configuration(
                                    "Templates", None, 0),
                                self.controller.create_panel_routes_configuration(
                                    "Tokens", None, 1),
                                self.controller.create_panel_routes_configuration(
                                    "Paths", None, 2)
                            ],
                            'grid': {
                                'row': 1,
                                'column': 0,
                                'sticky': N+S
                            }
                        },
                        {
                            'type': Frame,
                            'id': 'buttons_frame_widgets',
                            'children': [
                                {
                                    'type': Button,
                                    'properties': {
                                        'command': self.controller.generate_files,
                                        'text': "Generate"
                                    },
                                    'grid': {}
                                }
                            ],
                            'grid': {
                                'column': 0,
                                'row': 0,
                                'pady': 10
                            }
                        }
                    ]
                }
            ],
            'grid': {
                'row': 0,
                'column': 0
            }
        }
        self.render(self.window, template)
