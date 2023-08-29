# The app is created with the goal of learning python coding.

# The app "MeteoLT API requests data console with Tkinter" by Tomas Suslavicius.

# Coding was done with python 3.11.1.

# https://api.meteo.lt/

# Import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from copy import deepcopy
import textwrap
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

# Import necessary modules
from terminal import Terminal
from api_requests import ApiRequests
from calculations import Table
from analyze import Analyze
from forecast_db import ForecastDB
import backup
import rearrange_csv_by_date
import rearrange_json_by_date
import remove_duplicates_csv

# Set DPI Awareness
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

####################################
# Application main window and loop #
####################################

class App():
	def __init__(self):
		"""Initializes main window and runs main loop of the app"""
		
		# Main window setup
		self.main = tk.Tk()
		self.main.title("MeteoLT API requests data console with Tkinter")

		# Create widgets: Notebook and main frames, that organize sections for display data
		self.notebook = ttk.Notebook(self.main, padding=10)
		self.tab1 = ttk.Frame(self.notebook)
		self.tab1.pack()
		self.tab2 = ttk.Frame(self.notebook)
		self.tab2.pack()
		self.tab3 = ttk.Frame(self.notebook)
		self.tab3.pack()
		self.terminal = Terminal(self.tab1)
		self.measured = Measured(self.tab1, self.terminal)
		self.forecasted = Forecasted(self, self.tab1)
		self.graph = Graph(self, self.tab1)
		self.table = Table(self.tab2, self.terminal)
		self.analyze = Analyze(self.tab3, self.terminal)
		self.forecast_data = ForecastDB(self.terminal)
		self.notebook.add(self.tab1, text="Visualize API requests data")
		self.notebook.add(self.tab2, text="Analyze temperature forecast accuracy")
		self.notebook.add(self.tab3, text="Analyze temperature data in graph")
		self.notebook.pack(padx=5, pady=5, expand=True)
		self.terminal.fill_terminal(log_text_message="App launched successfully...\n")
	
		# Create menu widget
		menu = tk.Menu(self.main)
		file_menu = tk.Menu(menu, tearoff = False)
		file_menu.add_command(label = 'Backup files', command = lambda: backup.backup_data_files(self.terminal))
		file_menu.add_command(label = 'Update forecast json data files', command = self.forecast_data.run_forecast_data_update)
		file_menu.add_command(label = 'Rearrange json files data by date', command = lambda: rearrange_json_by_date.rearrange_json_data_by_date(self.terminal))
		file_menu.add_command(label = 'Rearrange csv files data by date', command = lambda: rearrange_csv_by_date.rearrange_csv_data_by_date(self.terminal))
		file_menu.add_command(label = 'Remove duplicates from csv files (disabled)', command = None) # Temporarily disabled, no duplicates generated
		menu.add_cascade(label = 'Manage data files', menu = file_menu)
		
		help_menu = tk.Menu(menu, tearoff = False)
		help_menu.add_command(label = 'Read help', command = self.open_help_window)
		menu.add_cascade(label = 'Help', menu = help_menu)

		self.main.configure(menu = menu)

	def open_help_window(self):
		"""Opens separate window with help text"""

		lines = []
		with open('help.txt', 'r') as file:
			for paragraph in file.read().split('\n'):
				if paragraph:
					lines.extend(textwrap.wrap(paragraph, 51))
				else:
					lines.append('') 
		help_window = tk.Toplevel()
		help_window.title('Help text')
		help_window.geometry('450x420+400+200')
		help_text_box = tk.Text(help_window, padx=20, pady=10, background='gray94')
		help_text_box.pack(expand=True, fill='both')
		help_text_box.config(state='normal')
		for line in lines:
			help_text_box.insert('end', f"{line}\n")
		help_text_box.config(state='disabled')

#####################################
# Fill first TAB of notebook widget #
#####################################

class Measured(ttk.LabelFrame):
	"""The class defines the frame and widgets for the 'Measured data' section."""

	def __init__(self, parent, terminal_instance_ref):
		"""Initializes Measured data label frame"""		
		super().__init__(parent)
		self.configure(text="Measured data", labelanchor="n", padding=10)
		self.grid(row=0, column=0, padx=10, pady=10)
		
		# Initializes modules
		self.api = ApiRequests()

		# Store reference to instance of terminal module
		self.terminal = terminal_instance_ref

		# Displays initial values in measured section
		self.create_widgets_m()
		self.renew_observations()

	def renew_observations(self):
		"""Button function to show/update observations in measured data field"""
		self.fill_measured()
		self.fill_latest()
		self.terminal.fill_terminal(log_text_message="Measured data updated...\n")

	def create_widgets_m(self):
		"""Creates widgets in Measured data label frame"""

		# Display labels on top of the boxes
		self.label_date = ttk.Label(self, text="Enter the date", anchor="center")
		self.label_date_entry_form = ttk.Label(self, text="yyyy-mm-dd", anchor="center")
		self.label_hour = ttk.Label(self, text="Select an hour", anchor="center")
		self.label_station = ttk.Label(self, text="Select a station", anchor="center")
		self.label_historic = ttk.Label(self, text="Station measured data", anchor="center")
		self.label_latest = ttk.Label(self, text="Latest measurement data", anchor="center")
		self.label_date.grid(row=0, column=1, sticky="S", pady=0)
		self.label_date_entry_form.grid(row=2, column=1, sticky="N", pady=0)
		self.label_hour.grid(row=0, column=2, sticky="S", pady=0)
		self.label_station.grid(row=0, column=0, sticky="S", pady=0)
		self.label_historic.grid(row=3, column=0, columnspan=2, sticky="S", pady=10)
		self.label_latest.grid(row=3, column=2, columnspan=2, sticky="S", pady=10)

		# Create entry box for the date input
		self.yesterday = datetime.date.today() - datetime.timedelta(1)
		self.date = tk.StringVar()
		self.date_input_box = ttk.Entry(self, width=10, textvariable=self.date)
		self.date_input_box.insert(0, f"{self.yesterday}")
		self.date_input_box.grid(row=1, column=1, padx=0, pady=0, sticky="N")
		self.date_input_box.focus()

		# Create combobox to select the hour of the day
		self.start_hour = datetime.datetime.now().hour
		self.hour = tk.StringVar()
		self.hour_selection_box = ttk.Combobox(self, state="readonly", width=5, textvariable=self.hour)
		self.hour_selection_box["values"] = ("00:00", "01:00", "02:00", "03:00", "04:00", "05:00", "06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00","13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00", "22:00", "23:00")
		self.hour_selection_box.current(self.start_hour)
		self.hour_selection_box.grid(row=1, column=2, pady=0, sticky="N")

		# Create combobox for station selection
		self.station = tk.StringVar()
		self.station_selection_box = ttk.Combobox(self, state="readonly", width=13, textvariable=self.station)
		self.station_selection_box["values"] = ('birzu-ams', 'dotnuvos-ams', 'duksto-ams', 'kauno-ams', 'klaipedos-ams', 'kybartu-ams', 'laukuvos-ams', 'lazdiju-ams', 'nidos-ams', 'panevezio-ams', 'raseiniu-ams', 'siauliu-ams', 'silutes-ams', 'telsiu-ams', 'ukmerges-ams', 'utenos-ams', 'varenos-ams', 'vilniaus-ams')
		self.station_selection_box.current(17)
		self.station_selection_box.grid(row=1, column=0, padx=0, pady=0, sticky="N")

		# Create button to display observations
		self.show_observations = ttk.Button(self, text="Update observations", command=self.renew_observations)
		self.show_observations.grid(row=1, column=3, padx=0, pady=0, sticky="N")

		# Display observations values in text box in the middle of the frame
		self.display_values = tk.Text(self, height=12, width=36, background='gray94', relief='flat', font='TkDefaultFont')
		self.display_values.grid(row=4, column=0, columnspan=2, padx=0, pady=0, sticky="N")

		# Display observations values of latest hour in the text box at the bottom of the frame
		self.display_values_latest = tk.Text(self, height=12, width=36, background='gray94', relief='flat', font='TkDefaultFont')
		self.display_values_latest.grid(row=4, column=2, columnspan=2, padx=5, pady=0, sticky="N")		

	def fill_measured(self):
		"""Fills left text widget with measured weather data of the chosen station by date and hour"""
		station_code = self.station.get()
		date = self.date.get()
		hour = int(self.hour.get()[:2])  # Hour equals to the index in the list
		self.measured_weather_data = self.api.get_measured(station_code, date)
		try:
			tuple_list = reversed(self.measured_weather_data['observations'][hour].items())
		except (KeyError, IndexError):
			showerror(title='Error', message='Invalid date or hour input value.')
			tuple_list = deepcopy(self.old_tuple_list)
			return
		self.display_values['state'] = 'normal'
		self.display_values.delete("1.0", tk.END)
		for key, value in tuple_list:
			self.display_values.insert("1.0", f"{key}" + ": " + f"{value}\n")
		self.display_values['state'] = 'disabled'
		self.old_tuple_list = deepcopy(tuple_list)

	def fill_latest(self):
		"""Fills right text widget with latest measured weather data of the chosen station"""
		station_code = self.station.get()
		self.latest_weather_data = self.api.get_latest(station_code)
		tuple_list = reversed(self.latest_weather_data['observations'][-1].items())
		self.display_values_latest['state'] = 'normal'
		self.display_values_latest.delete("1.0", tk.END)
		for key, value in tuple_list:
			self.display_values_latest.insert("1.0", f"{key}" + ": " + f"{value}\n")
		self.display_values_latest['state'] = 'disabled'

class Forecasted(ttk.LabelFrame):
	"""The class defines the frame and widgets for the 'Forecasted data' section."""
	def __init__(self, app_class_instance, parent):
		"""Initializes Forecasted data label frame"""
		
		super().__init__(parent)
		
		# Initializes API requests module
		self.api = ApiRequests()

		# Store reference to instances of App
		self.app = app_class_instance

		# Create label frame for graph
		self.configure(text="Forecasted data", labelanchor="n", padding=10)
		self.grid(row=0, column=1, padx=10, pady=10)
		self.create_widgets_f()
		self.fill_4day_forecast()
		self.app.terminal.fill_terminal(log_text_message="4 day forecast data updated...\n")
	
	def update_forecast(self, *args):
		"""Updates 4day forecast table"""
		self.frame_4day_forecast.pack_forget()
		self.fill_4day_forecast()
		self.app.graph.canvas_for_graph.pack_forget()
		self.app.graph.create_widgets_g()
		self.app.terminal.fill_terminal(log_text_message="Forecast data updated...\n")
		
	def create_widgets_f(self):
		"""Creates widgets in Forecasted data label frame"""

		# Create label for place selection combobox
		self.label_place_forecast = ttk.Label(self, text='Select forecast place').pack()

		# Create combobox for forecast place selection
		self.forecast_places = tk.StringVar()
		self.forecast_places_list = self.api.get_places()
		self.f_places_list = []
		self.f_places_list_code = {}
		for place_dictionary in self.forecast_places_list:
		    self.f_places_list.append(place_dictionary.get('administrativeDivision') + ": " + place_dictionary.get('name'))
		    self.f_places_list_code[(place_dictionary.get('administrativeDivision') + ": " + place_dictionary.get('name'))] = place_dictionary.get('code')
		self.f_places_list.sort()
		self.place_forecast_selection_box = ttk.Combobox(self, state="readonly", width=50, textvariable=self.forecast_places)   
		self.place_forecast_selection_box["values"] = self.f_places_list
		self.place_index = self.f_places_list.index(('Vilniaus miesto savivaldybė: Vilnius'))
		self.place_forecast_selection_box.current(self.place_index)
		self.place_forecast_selection_box.pack()

	
		# Create label for 4day forecast table
		self.label_4day_forecast = ttk.Label(self, text='4 day forecast').pack()

		# Bind event for combobox place selection
		self.place_forecast_selection_box.bind("<<ComboboxSelected>>", self.update_forecast)
		
	def fill_4day_forecast(self):
		"""Draws 4day forecast table"""

		# Create frame for 4day forecast table
		self.frame_4day_forecast = ttk.Frame(self)
		self.frame_4day_forecast.pack()

		# Display 4 day forecast data in the table
		administrative_division = self.forecast_places.get()
		place = self.f_places_list_code[administrative_division]
		global value_forecast
		value_forecast = self.api.get_forecast(place)['forecastTimestamps'][:]
		items_forecast = len(value_forecast)
		value_forecast_shortlisted = []
		time_stamp_list = []
		for index in range(items_forecast):
		    item_dict = value_forecast[index]
		    time_stamp = value_forecast[index]['forecastTimeUtc'][11:13]
		    # Shorten the data list and split datetime to fit in window
		    if time_stamp == '00' or time_stamp == '12' or time_stamp == '15':
		        item_dict_copy = item_dict.copy()
		        item_dict_copy['forecastDate'] = item_dict_copy['forecastTimeUtc'][:10]
		        item_dict_copy['forecastTimeUtc'] = item_dict_copy['forecastTimeUtc'][11:]
		        # Set the background colour for the night and the day
		        if time_stamp == '00':
		            item_dict_copy['background'] = '#191970'
		            item_dict_copy['foreground'] = '#FFFFFF'
		        elif time_stamp == '12':
		            item_dict_copy['background'] = '#ADD8E6'
		            item_dict_copy['foreground'] = '#000000'
		        elif time_stamp == '15':
		            item_dict_copy['background'] = '#A7C7E7'
		            item_dict_copy['foreground'] = '#000000'
		        value_forecast_shortlisted.append(item_dict_copy)

		# Set the index order for the rows
		table_keys = [  'forecastDate',
		                'forecastTimeUtc',
		                'airTemperature',
		                'feelsLikeTemperature',
		                'windSpeed',
		                'windGust',
		                'windDirection',
		                'cloudCover',
		                'seaLevelPressure',
		                'relativeHumidity',
		                'totalPrecipitation',
		                'conditionCode',                
		                ]
		table_rows = len(table_keys)
		table_columns = len(value_forecast_shortlisted[0:14])

		# Generate the forecast data table
		for row in range(table_rows):
		    entry_key = tk.Entry(self.frame_4day_forecast, width=20, relief='flat', background='gray94')
		    entry_key.grid(row=row, column=0)
		    entry_key.insert(0, table_keys[row])
		    for column in range(table_columns):
		        entry_forecast = tk.Entry(self.frame_4day_forecast, justify="center", width=10, relief='flat', background=value_forecast_shortlisted[column]['background'], foreground=value_forecast_shortlisted[column]['foreground'])
		        entry_forecast.grid(row=row, column=column + 1)
		        entry_forecast.insert(0, f"{value_forecast_shortlisted[column][table_keys[row]]}")

class Graph(ttk.LabelFrame):
	"""The class defines 7-day forecast graph"""

	def __init__(self, app_class_instance, parent):
		"""Initializes graph"""
		super().__init__(parent)

		# Store reference to instances of App
		self.app = app_class_instance

		# Create label frame for graph
		self.configure(text="7- day forecasted temperature", labelanchor="n", padding=10)
		self.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
		self.create_widgets_g()
		self.app.terminal.fill_terminal(log_text_message="7 day forecast graph updated...\n")


	def create_widgets_g(self):
		"""Creates widgets for placing the 7day matplotlib graph"""

		self.canvas_for_graph = tk.Canvas(self, bg="grey94", height=450, width=1780, scrollregion=(0, 0, 3000, 450))
		self.canvas_for_graph.pack(expand=True, fill='both')
		self.frame_for_graph = ttk.Frame(self.canvas_for_graph)
		self.canvas_for_graph.create_window((0, 0), window = self.frame_for_graph, anchor="nw", width=3000, height=430)
		
		self.scrollbar_for_canvas = ttk.Scrollbar(self.canvas_for_graph, orient='horizontal', command=self.canvas_for_graph.xview)
		self.canvas_for_graph.configure(xscrollcommand=self.scrollbar_for_canvas.set)
		self.scrollbar_for_canvas.place(relx=0, rely=1, relwidth=1, anchor='sw')
		self.canvas_for_graph.bind('<MouseWheel>', lambda event: self.canvas_for_graph.xview_scroll(int(event.delta / 60), "units"))
		self.show_graph()

	def show_graph(self):
	    """Prepare and display forecast data line graph"""
	    forecast_date_time = []
	    forecast_temperature = []
	    forecast_feelslike = []
	    for item_graph in value_forecast:
	        date_graph = datetime.datetime.strptime(item_graph['forecastTimeUtc'], '%Y-%m-%d %H:%M:%S')
	        forecast_date_time.append(date_graph)
	        forecast_temperature.append(item_graph['airTemperature'])
	        forecast_feelslike.append(item_graph['feelsLikeTemperature'])
	    plt.style.use('ggplot')
	    graph = Figure(figsize=(25,4), dpi=100)
	    graph_canvas = FigureCanvasTkAgg(graph, self.frame_for_graph)
	    NavigationToolbar2Tk(graph_canvas, self.frame_for_graph)

	    ax = graph.add_subplot()
	    ax.plot(forecast_date_time, forecast_temperature, label="airtemp")
	    ax.scatter(forecast_date_time, forecast_temperature, s=8, c='blue')
	    ax.plot(forecast_date_time, forecast_feelslike, label="feelslike")
	    ax.scatter(forecast_date_time, forecast_feelslike, s=8, c='red')
	    ax.set_title('7-day air/feelslike temperatureForecast', fontsize=8)
	    ax.set_xlabel('dateTime', fontsize=8)
	    ax.set_ylabel('temperatureCelsius', fontsize=8)
	    ax.legend(loc="upper left")
	    graph.autofmt_xdate()
	    graph.tight_layout()
	    ax.tick_params(axis='both', labelsize=8)
	    graph_canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)


# Run the app
if __name__ == "__main__":
	app = App()
	app.main.mainloop()