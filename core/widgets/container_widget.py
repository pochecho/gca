class ContainerWidget():
    def __init__(self):
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


