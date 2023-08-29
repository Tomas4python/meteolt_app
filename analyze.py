import tkinter as tk
from tkinter import ttk
import csv
import datetime

from pprint import pprint as pp

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
    )

######################################
# Fill third TAB of notebook widget #
######################################

class Analyze(ttk.LabelFrame):
	"""The class to create widgets in section analyze of notebook"""

	def __init__(self, parent, terminal_instance_ref):
		"""Initializes some parameters"""
		super().__init__(parent)
		self.terminal = terminal_instance_ref
		self.configure(text="Analyze temperature data with graph", labelanchor="n", padding=10)
		self.pack()
		self.create_widgets_a()
		self.create_widgets_ag()
		self.get_data()
		self.show_analyze()
		self.terminal.fill_terminal(log_text_message="Analyze with graph updated...\n")


	def get_data(self, *args):
		# Get list of selected items in the listbox
		selected_items = self.listbox_f_duration.curselection()
		list_selected_items = []
		for index in selected_items:
			key = self.listbox_f_duration.get(index)
			list_selected_items.append(key)

		# Get the shortest list of datatime stamps in selected csv files
		row_count_initial = 10**10
		shortest = {}
		for item in list_selected_items:
			file_name = self.dictionary_for_listbox[item][0]
			with open("data/" + file_name, 'r') as file:
				file.seek(0)				
				reader = csv.reader(file)
				data = list(reader)
				row_count = len(data)
				if row_count < row_count_initial:
					row_count_initial = row_count
					shortest["file_name"] = file_name
		datatime_stamps = []
		with open("data/" + f"{shortest['file_name']}", 'r') as file:
			file.seek(0)
			reader = csv.reader(file)
			header_row = next(reader)
			for row in reader:
				datatime_stamps.append(row[0])

		# Get all data needed for graph from all selected files by the datetime stamps
		self.data_for_graph = {}
		for item in list_selected_items:
			# Get temperature values from files
			file_name = self.dictionary_for_listbox[item][0]
			with open("data/" + file_name, 'r') as file:
				file.seek(0)
				reader = csv.reader(file)
				header_row = next(reader)
				temperature_values = []
				datatime_stamps_actual = []
				for row in reader:
					if row[0] in datatime_stamps:
						temperature_values.append(float(row[self.dictionary_for_listbox[item][1]]))
						datatime_stamps_actual.append(row[0])
			self.data_for_graph[item] = (datatime_stamps_actual, temperature_values, self.dictionary_for_listbox[item][2])

	def create_widgets_a(self):
		"""Deploys listbox and canvas"""

		# Create frame for listboxes section
		self.frame_listbox = ttk.LabelFrame(self, text='Select data to show in graph', labelanchor="n", padding=10)
		self.frame_listbox.pack(side=tk.LEFT)

		# Create dictionary for listbox creation, choose different color for different items
		self.dictionary_for_listbox = {
		"Vilnius airTemp measured": ('csv_combined_vln_Day 1.csv', 2, "#e1c62b"),
		"Vilnius Temp feelslike": ('csv_combined_vln_Day 1.csv', 4, "#5342c6"),
		"Klaipėda airTemp measured": ('csv_combined_klp_Day 1.csv', 2, "#1e8500"),
		"Klaipėda Temp feelslike": ('csv_combined_klp_Day 1.csv', 4, "#b36bf6"),
		"Vilnius airTemp 1 day forecast": ('csv_combined_vln_Day 1.csv', 3, "#acd45a"),
		"Vilnius airTemp 2 days forecast": ('csv_combined_vln_Day 2.csv', 3, "#b10091"),		
		"Vilnius airTemp 3 days forecast": ('csv_combined_vln_Day 3.csv', 3, "#24e0a0"),
		"Vilnius airTemp 4 days forecast": ('csv_combined_vln_Day 4.csv', 3, "#ce0042"),
		"Vilnius airTemp 5 days forecast": ('csv_combined_vln_Day 5.csv', 3, "#4adad7"),
		"Vilnius airTemp 6 days forecast": ('csv_combined_vln_Day 6.csv', 3, "#c03900"),
		"Vilnius airTemp 7 days forecast": ('csv_combined_vln_Day 7.csv', 3, "#00a4fd"),
		"Vilnius feelslikeTemp 1 day forecast": ('csv_combined_vln_Day 1.csv', 5, "#fda412"),
		"Vilnius feelslikeTemp 2 days forecast": ('csv_combined_vln_Day 2.csv', 5, "#0163ce"),
		"Vilnius feelslikeTemp 3 days forecast": ('csv_combined_vln_Day 3.csv', 5, "#ffae43"),
		"Vilnius feelslikeTemp 4 days forecast": ('csv_combined_vln_Day 4.csv', 5, "#0d52a0"),
		"Vilnius feelslikeTemp 5 days forecast": ('csv_combined_vln_Day 5.csv', 5, "#ff6f50"),
		"Vilnius feelslikeTemp 6 days forecast": ('csv_combined_vln_Day 6.csv', 5, "#52d5fd"),
		"Vilnius feelslikeTemp 7 days forecast": ('csv_combined_vln_Day 7.csv', 5, "#963005"),
		"Klaipėda airTemp 1 day forecast": ('csv_combined_klp_Day 1.csv', 3, "#01a7ca"),
		"Klaipėda airTemp 2 days forecast": ('csv_combined_klp_Day 2.csv', 3, "#af0062"),		
		"Klaipėda airTemp 3 days forecast": ('csv_combined_klp_Day 3.csv', 3, "#006230"),
		"Klaipėda airTemp 4 days forecast": ('csv_combined_klp_Day 4.csv', 3, "#ff75df"),
		"Klaipėda airTemp 5 days forecast": ('csv_combined_klp_Day 5.csv', 3, "#786400"),
		"Klaipėda airTemp 6 days forecast": ('csv_combined_klp_Day 6.csv', 3, "#adafff"),
		"Klaipėda airTemp 7 days forecast": ('csv_combined_klp_Day 7.csv', 3, "#ffa473"),
		"Klaipėda feelslikeTemp 1 day forecast": ('csv_combined_klp_Day 1.csv', 5, "#494e83"),
		"Klaipėda feelslikeTemp 2 days forecast": ('csv_combined_klp_Day 2.csv', 5, "#daa781"),
		"Klaipėda feelslikeTemp 3 days forecast": ('csv_combined_klp_Day 3.csv', 5, "#783983"),
		"Klaipėda feelslikeTemp 4 days forecast": ('csv_combined_klp_Day 4.csv', 5, "#814031"),
		"Klaipėda feelslikeTemp 5 days forecast": ('csv_combined_klp_Day 5.csv', 5, "#ff81b4"),
		"Klaipėda feelslikeTemp 6 days forecast": ('csv_combined_klp_Day 6.csv', 5, "#952a47"),
		"Klaipėda feelslikeTemp 7 days forecast": ('csv_combined_klp_Day 7.csv', 5, "#db93ab"),
					}
		# Create listbox
		self.list_items = []
		for key in self.dictionary_for_listbox:
			self.list_items.append(key)
		self.forecast_duration = tk.StringVar(value=self.list_items)
		self.listbox_f_duration = tk.Listbox(self.frame_listbox, listvariable=self.forecast_duration, height=32, width=38, selectmode="extended")
		self.listbox_f_duration.select_set(0, 1)
		self.listbox_f_duration.pack()

		
		# Create button update graph
		self.button_update = ttk.Button(self.frame_listbox, text="Update graph", command=self.update_analyze)
		self.button_update.pack()

	def update_analyze(self, *args):
		"""Updates graph"""
		self.frame_graph.pack_forget()
		self.create_widgets_ag()
		self.get_data()
		self.show_analyze()
		self.terminal.fill_terminal(log_text_message="Analyze with graph updated...\n")


	def create_widgets_ag(self):
		"""Creates widgets for placing the analyze matplotlib graph"""
		
		# Create frame for graph section
		self.frame_graph = ttk.LabelFrame(self, text='Graph view', labelanchor="n", padding=10)
		self.frame_graph.pack(side=tk.LEFT)

		# Create widgets for matplotlib graph
		self.canvas_for_graph = tk.Canvas(self.frame_graph, bg="grey94", height=820,
    width=1500, scrollregion=(0, 0, 3000, 820))
		self.canvas_for_graph.pack(expand=True, fill='both')
		self.frame_for_graph = ttk.Frame(self.frame_graph)
		self.canvas_for_graph.create_window((0, 0), window = self.frame_for_graph, anchor="nw", width=3000, height=790)
		
		self.scrollbar_for_canvas = ttk.Scrollbar(self.frame_graph, orient='horizontal', command=self.canvas_for_graph.xview)
		self.canvas_for_graph.configure(xscrollcommand=self.scrollbar_for_canvas.set)
		self.scrollbar_for_canvas.place(relx=0, rely=1, relwidth=1, anchor='sw')
		self.canvas_for_graph.bind('<MouseWheel>', lambda event: self.canvas_for_graph.xview_scroll(int(event.delta / 60), "units"))

	def show_analyze (self):
		"""Prepare and diplay forecast data line graph"""
		plt.style.use('ggplot')
		graph = Figure(figsize=(25, 13), dpi=100)
		graph_canvas = FigureCanvasTkAgg(graph, self.frame_for_graph)
		NavigationToolbar2Tk(graph_canvas, self.frame_for_graph)
		ax = graph.add_subplot()
		# self.data_for_graph[label] = (datatime_stamps, temperature_values, 				self.dictionary_for_listbox[item][2])
		#       key = label				date/time list    temperature list				color
		for label in self.data_for_graph:
			date_time_list = []
			for date_time in self.data_for_graph[label][0]:
				date_datetime_format = datetime.datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
				date_time_list.append(date_datetime_format)
				temperature = self.data_for_graph[label][1]
				color = self.data_for_graph[label][2]
			ax.plot(date_time_list, temperature, label=f"{label}", c=f'{color}', alpha=0.5)
			ax.scatter(date_time_list, temperature, s=8, c=f'{color}')
		ax.set_title('Air/feelslike temperature', fontsize=8)
		ax.set_xlabel('dateTime', fontsize=8)
		ax.set_ylabel('temperatureCelsius', fontsize=8)
		ax.legend(loc="upper left")
		graph.autofmt_xdate()
		graph.tight_layout()
		ax.tick_params(axis='both', labelsize=8)
		graph_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

