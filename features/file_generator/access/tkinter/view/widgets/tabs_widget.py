from tkinter.ttk import Notebook
from tkinter import PhotoImage, Label, Frame, Text, Tk
from tkinter import LEFT, TOP,StringVar
from tkinter import N,NE,NO, W, E, S, CENTER, END

# help(Notebook)
class TabsWidget(Notebook):
    def __init__(self,root):
        super(TabsWidget, self).__init__()
        self._init_components()
    def _init_components(self):
        self.create_panel()

    def create_panel(self):
        self.tabs_values = []
        self.web_label = self.create_inside_panel(self)
        self.forum_label = self.create_inside_panel(self)
        
        self.class_image = PhotoImage(file="assets/images/class.png")
        self.add(self.web_label, text="Class", image=self.class_image, compound=TOP, padding=20)
 
        self.object_image = PhotoImage(file="assets/images/attributes.png")
        self.add(self.forum_label, text="Attributes", image=self.object_image, compound=TOP, padding=20)
        

    def create_inside_panel(self,parent):
        panel = Frame(parent)
        text_area = Text(panel, height=20, width=50)
        # func = lambda x : self.evaluate[len(self.tabs_values)]
        # text_area.tag_bind("Enter>",func =  func)
        self.tabs_values.append(text_area)
        text_area.grid(row=0,column=0)
        return panel

    def get_value(self,index):
        return self.tabs_values[index].get('1.0',END)
    
    def set_value(self,index,value):
        self.tabs_values[index].delete('1.0',END)
        self.tabs_values[index].insert('1.0',value)
    