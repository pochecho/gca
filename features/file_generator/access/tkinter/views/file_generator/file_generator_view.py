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
                        # 'sticky': E+W,
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
                                    "Templates", None, 0,'#234'),
                                self.controller.create_panel_routes_configuration(
                                    "Tokens", None, 1, '#564'),
                                self.controller.create_panel_routes_configuration(
                                    "Paths", None, 2, '#20a')
                            ],
                            # 'grid': {
                            #     'row': 0,
                            #     'column': 0,
                            #     'sticky': N+S
                            # }
                            'pack': {
                                
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
                                        'text': "Generate",
                                        'bg': '#099',
                                        'fg': 'black'
                                    },
                                    'grid': {}
                                }
                            ],
                            # 'grid': {
                            #     'column': 0,
                            #     'row': 1,
                            #     'pady': 10
                            # }
                            'pack': {}
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
