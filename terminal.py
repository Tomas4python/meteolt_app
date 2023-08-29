import tkinter as tk
from tkinter import ttk

###########################################
# Module for logging messages to terminal #
###########################################

class Terminal(ttk.LabelFrame):
	"""Class creates frame and widgets of the section Terminal window"""

	def __init__(self, parent):
		"""Initializes Terminal window label frame"""		

		super().__init__(parent)
		self.configure(text="Log terminal", labelanchor="n", padding=8)
		self.grid(row=0, column=2, padx=10, pady=10)
		self.create_widgets_t()
		self.fill_terminal("Terminal ok...\n")

	def create_widgets_t(self):
		"""Creates widgets in Terminal window label frame"""
		
		self.log_terminal_window = tk.Text(self, height=19, width=36, background='gray94', relief='flat', font='TkDefaultFont')
		self.log_terminal_window.pack()
		
	def fill_terminal(self, log_text_message):
		"""Fills log terminal window with log messages"""

		self.log_terminal_window['state'] = 'normal'
		self.log_text_message = log_text_message
		self.log_terminal_window.insert(tk.END, self.log_text_message)
		self.log_terminal_window['state'] = 'disabled'
		self.log_terminal_window.see('end')