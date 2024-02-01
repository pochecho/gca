from tkinter import Tk
from core.color_constants import bg
from tkinter.ttk import *

class Window:
	def __init__(self, width, height):
		self.window = Tk()
		self.width = width
		self.height = height
		self.configure_button_styles()
		self.config_window()
		self.handlers = []
  
		self.__width = self.width
		self.__height = self.height

	def config_window(self):
		self.window.geometry(str(self.width)+"x"+str(self.height))
		self.window.configure(bg=bg)

	def on_resize(self,event):
		if(abs(self.__height - event.height) > 100 or abs(self.__width != event.width) > 100):
			self.__height = event.height
			self.__width = event.width
			for handler in self.handlers:
				handler(event)

	def init(self):
		self.window.bind("<Configure>", lambda x : self.on_resize(x))
     
		self.window.mainloop()
  
	def add_handler(self,handler):
		self.handlers.append(handler)

	def configure_button_styles(self):
		style = Style()
		style.configure("ABC.TButton",
                        width="10", height="100",
						background="#3180FF",
                        foreground="white")

		style.configure("AB.TButton",
                        background="#3180FF",
                        foreground="white")

		style.configure("RB.TButton",
                        background="#FF2300",
                        foreground="white")

		style.configure("SmallRB.TButton",
                        background="#FF2300",
						width=3,
                        foreground="white")

		style.configure("Green.TFrame",
                        background="#85FF8B",
						foreground="black")

		style.configure("Blue.TFrame",
                        background="#1e90FF",
						foreground="black")

		style.configure("Green.TLabel",
                        background="#85FF8B",
						foreground="black")

		style.configure("Blue.TLabel",
                        background="#1e90FF",
						foreground="black")

		style.configure("SmallGB.TButton",
                        background="green",
						width=3,
                        foreground="white")
