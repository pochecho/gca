from tkinter.ttk import Entry
class EntryWithPlaceholder(Entry):
	def __init__(self, master=None, placeholder="PLACEHOLDER", color='grey'):
		Entry.__init__(self, master)

		self.placeholder = placeholder
		self.placeholder_color = color
		self.default_fg_color = self['foreground']

		self.bind("<FocusIn>", self.foc_in)
		self.bind("<FocusOut>", self.foc_out)
		self.put_placeholder()

	def put_placeholder(self):
		self.insert(0, self.placeholder)
		self['foreground'] = self.placeholder_color

	def foc_in(self, *args):
		if str(self['foreground']) == self.placeholder_color:
			self.delete('0', 'end')
			self['foreground'] = self.default_fg_color

	def foc_out(self, *args):
		if not self.get():
			self.put_placeholder()

