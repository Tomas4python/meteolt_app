import tkinter as tk
from tkinter import ttk
import csv
import statistics as st
import numpy as np
from pprint import pprint as pp


######################################
# Fill second TAB of notebook widget #
######################################

class Table(ttk.LabelFrame):
	"""The class to create table with treeview widget"""

	def __init__(self, parent, terminal_instance_ref):
		super().__init__(parent)
		self.terminal = terminal_instance_ref
		self.configure(text="Forecast data accuracy", labelanchor="n", padding=10)
		self.pack()
		self.create_widgets_s()
		self.insert_data()
		self.terminal.fill_terminal(log_text_message="Database analyzed, table filled up...\n")


	def create_widgets_s(self):

		# Create statistics table with treeview widget
		self.statistics_table = ttk.Treeview(self, columns=('Forecast duration','Amount of data', 'Average', 'Min', '25th percentile', 'Median', '75th percentile', 'Max'), show='headings', height=32)

		self.statistics_table.heading('Forecast duration', text='Forecast duration')
		self.statistics_table.column('Forecast duration', width=100, anchor="center")
		self.statistics_table.heading('Amount of data', text='Amount of data')
		self.statistics_table.column('Amount of data', width=100, anchor="center")
		self.statistics_table.heading('Average', text='Average')
		self.statistics_table.column('Average', width=100, anchor="center")
		self.statistics_table.heading('Min', text='First 5 min')
		self.statistics_table.column('Min', width=180, anchor="center")
		self.statistics_table.heading('25th percentile', text='25th percentile')
		self.statistics_table.column('25th percentile', width=100, anchor="center")
		self.statistics_table.heading('Median', text='Median')
		self.statistics_table.column('Median', width=100, anchor="center")
		self.statistics_table.heading('75th percentile', text='75th percentile')
		self.statistics_table.column('75th percentile', width=100, anchor="center")
		self.statistics_table.heading('Max', text='Last 5 max')
		self.statistics_table.column('Max', width=180, anchor="center")
		self.statistics_table.pack()

	def insert_data(self):

		# Insert data into the table
		self.data = Calculations().get_statistics()
		insertions = {
						0 : ["", "", "", "Vilnius", "airTemp"],
						1 : ["", "", "", "Vilnius", "feelslikeTemp"],
						2 : ["", "", "", "Klaipėda", "airTemp"],
						3 : ["", "", "", "Klaipėda", "feelslikeTemp"]
						}
		for index, dictionary in enumerate(self.data):
			self.statistics_table.insert(parent = '', index='end', values = insertions[index])
			for day in Calculations().days:
				self.statistics_table.insert(parent = '', index='end', values = dictionary[day])


class Calculations:
	"""The class with only one statistics function"""

	def __init__(self):
		"""Initializes statistics function"""
		self.days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']

	def get_statistics(self):
		"""Opens data files and calculates statistics"""
				
		# Create dictionaries to keep values lists
		list_vln_m = {}
		list_vln_f = {}
		list_klp_m = {}
		list_klp_f = {}

		# Create dictionaries to store data
		statistics_vln_m = {}
		statistics_vln_f = {}
		statistics_klp_m = {}
		statistics_klp_f = {}

		# Create lists of measured and forecasted temperature differences
		for day in self.days:
			list_vln_m[day] = []
			list_vln_f[day] = []
			list_klp_m[day] = []
			list_klp_f[day] = []
			with open(f'data/csv_combined_vln_{day}.csv', 'r') as vln_file:
				vln_reader = csv.reader(vln_file)
				header_row = next(vln_reader)
				for row in vln_reader:
					measured = float(row[2])
					forecasted = float(row[3])
					feelslike = float(row[4])
					f_feelslike = float(row[5])
					difference_temp = round(abs(float(measured - forecasted)), 2)
					difference_feels = round(abs(float(feelslike - f_feelslike)), 2)
					list_vln_m[day].append(difference_temp)
					list_vln_f[day].append(difference_feels)
			with open(f'data/csv_combined_klp_{day}.csv', 'r') as klp_file:
				klp_reader = csv.reader(klp_file)
				header_row = next(klp_reader)
				for row in klp_reader:
					measured = float(row[2])
					forecasted = float(row[3])
					feelslike = float(row[4])
					f_feelslike = float(row[5])
					difference_temp = round(abs(float(measured - forecasted)), 2)
					difference_feels = round(abs(float(feelslike - f_feelslike)), 2)
					list_klp_m[day].append(difference_temp)
					list_klp_f[day].append(difference_feels)


			# Create lists of statistics data for each forecast duration
			statistics_vln_m[day] = []
			statistics_vln_f[day] = []
			statistics_klp_m[day] = []
			statistics_klp_f[day] = []

			# Calculate forecast duration
			duration_vln = int(day[4])
			statistics_vln_m[day].append(duration_vln)
			statistics_vln_f[day].append(duration_vln)
			statistics_klp_m[day].append(duration_vln)
			statistics_klp_f[day].append(duration_vln)

			# Sort the list
			list_vln_m[day].sort()
			list_vln_f[day].sort()
			list_klp_m[day].sort()
			list_klp_f[day].sort()

			# Calculate amaunt of data
			data_amount_vln = len(list_vln_m[day])
			data_amount_klp = len(list_klp_m[day])
			statistics_vln_m[day].append(data_amount_vln)
			statistics_vln_f[day].append(data_amount_vln)
			statistics_klp_m[day].append(data_amount_klp)
			statistics_klp_f[day].append(data_amount_klp)

			# Calculate average
			average_vln_m = round(st.mean(list_vln_m[day]), 2)
			average_vln_f = round(st.mean(list_vln_f[day]), 2)
			average_klp_m = round(st.mean(list_klp_m[day]), 2)
			average_klp_f = round(st.mean(list_klp_f[day]), 2)
			statistics_vln_m[day].append(average_vln_m)
			statistics_vln_f[day].append(average_vln_f)
			statistics_klp_m[day].append(average_klp_m)
			statistics_klp_f[day].append(average_klp_f)

			# Calculate 5 min
			min_vln_m = "   ".join(map(str, (list_vln_m[day][0: 5])))
			min_vln_f = "   ".join(map(str, (list_vln_f[day][0: 5])))
			min_klp_m = "   ".join(map(str, (list_klp_m[day][0: 5])))
			min_klp_f = "   ".join(map(str, (list_klp_f[day][0: 5])))
			statistics_vln_m[day].append(min_vln_m)
			statistics_vln_f[day].append(min_vln_f)
			statistics_klp_m[day].append(min_klp_m)
			statistics_klp_f[day].append(min_klp_f)

			# Calculate 25th percentile
			p25_vln_m = round(np.percentile(list_vln_m[day], 25), 2)
			p25_vln_f = round(np.percentile(list_vln_f[day], 25), 2)
			p25_klp_m = round(np.percentile(list_klp_m[day], 25), 2)
			p25_klp_f = round(np.percentile(list_klp_f[day], 25), 2)
			statistics_vln_m[day].append(p25_vln_m)
			statistics_vln_f[day].append(p25_vln_f)
			statistics_klp_m[day].append(p25_klp_m)
			statistics_klp_f[day].append(p25_klp_f)

			# Calculate median
			median_vln_m = round(st.median(list_vln_m[day]), 2)
			median_vln_f = round(st.median(list_vln_f[day]), 2)
			median_klp_m = round(st.median(list_klp_m[day]), 2)
			median_klp_f = round(st.median(list_klp_f[day]), 2)
			statistics_vln_m[day].append(median_vln_m)
			statistics_vln_f[day].append(median_vln_f)
			statistics_klp_m[day].append(median_klp_m)
			statistics_klp_f[day].append(median_klp_f)

			# Calculate 75th percentile
			p75_vln_m = round(np.percentile(list_vln_m[day], 75), 2)
			p75_vln_f = round(np.percentile(list_vln_f[day], 75), 2)
			p75_klp_m = round(np.percentile(list_klp_m[day], 75), 2)
			p75_klp_f = round(np.percentile(list_klp_f[day], 75), 2)
			statistics_vln_m[day].append(p75_vln_m)
			statistics_vln_f[day].append(p75_vln_f)
			statistics_klp_m[day].append(p75_klp_m)
			statistics_klp_f[day].append(p75_klp_f)

			# Calculate 5 max
			max_vln_m = "   ".join(map(str, (list_vln_m[day][-5:])))
			max_vln_f = "   ".join(map(str, (list_vln_f[day][-5:])))
			max_klp_m = "   ".join(map(str, (list_klp_m[day][-5:])))
			max_klp_f = "   ".join(map(str, (list_klp_f[day][-5:])))
			statistics_vln_m[day].append(max_vln_m)
			statistics_vln_f[day].append(max_vln_f)
			statistics_klp_m[day].append(max_klp_m)
			statistics_klp_f[day].append(max_klp_f)

		return_data = (statistics_vln_m, statistics_vln_f, statistics_klp_m, statistics_klp_f)

		return return_data
