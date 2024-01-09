import requests
import json
import csv
import datetime
import matplotlib
import matplotlib.pyplot as plt
from pprint import pprint as pp # Used for manual debugging

#################################
# Module for creating databases #
#################################

class ForecastDB:
	"""Downloads and saves to files measured and forecast data for further analysis"""

	def __init__(self, terminal_instance_ref):
		"""Initializes variables and file"""
		self.terminal = terminal_instance_ref
		
	def run_forecast_data_update(self):

		self.get_forecast()
		self.get_measured()
		self.create_csv()
		self.analyze()
		self.terminal.fill_terminal(log_text_message="ForecastDB updated successfully...\n")

	def get_forecast(self):
		"""Gets from MeteoLT API current forecast data from Vilnius and Klaipeda places, saves data to file"""
		
		# Make API request for forecast
		self.url_vln_forecast = "https://api.meteo.lt/v1/places/vilnius/forecasts/long-term"
		self.url_klp_forecast = "https://api.meteo.lt/v1/places/klaipeda/forecasts/long-term"
		self.get_data_vln = requests.get(self.url_vln_forecast)
		self.get_data_klp = requests.get(self.url_klp_forecast)
		self.data_vln_forecast = self.get_data_vln.json()['forecastTimestamps']
		# pp(self.data_vln_forecast) # Used for manual debugging
		data_length_vln = len(self.data_vln_forecast)
		self.data_klp_forecast = self.get_data_klp.json()['forecastTimestamps']
		data_length_klp = len(self.data_klp_forecast)
		data_length = min(data_length_vln, data_length_klp)
		assert data_length in [74, 77, 78, 79, 80, 82, 83, 84, 85, 86, 87], f'MeteoLT API changed data length to {data_length}!'
		
		# Take from entire forecast data timestamp, airtemp, feelsliketemp and sort by forecast days from 1 to 7
		if data_length == 74:
		    loop_list = [(0, 24), (24, 40), (40, 48), (48, 56), (56, 64), (64, 70), (70, 74)]
		elif data_length == 77:
		    loop_list = [(0, 24), (24, 44), (44, 52), (52, 60), (60, 68), (68, 73), (73, 77)]
		elif data_length == 78:
		    loop_list = [(0, 24), (24, 44), (44, 52), (52, 60), (60, 68), (68, 73), (73, 77)]
		elif data_length == 79:
		    loop_list = [(0, 24), (24, 44), (44, 52), (52, 60), (60, 68), (68, 73), (75, 79)]
		elif data_length == 80:
		    loop_list = [(0, 24), (24, 45), (45, 53), (53, 61), (61, 69), (69, 76), (76, 80)]
		elif data_length == 82:
		    loop_list = [(0, 24), (24, 47), (47, 55), (55, 63), (63, 71), (71, 78), (78, 82)]
		elif data_length == 83:
		    loop_list = [(0, 24), (24, 48), (48, 57), (57, 65), (65, 73), (73, 79), (79, 83)]
		elif data_length == 84:
		    loop_list = [(0, 24), (24, 48), (48, 59), (59, 67), (67, 75), (75, 80), (80, 84)]
		elif data_length == 85:
		    loop_list = [(0, 24), (24, 48), (48, 59), (59, 67), (67, 75), (75, 81), (81, 85)]
		elif data_length == 86:
		    loop_list = [(0, 24), (24, 48), (48, 59), (59, 67), (67, 75), (75, 82), (82, 86)]
		elif data_length == 87:
		    loop_list = [(0, 24), (24, 48), (48, 60), (60, 68), (68, 76), (76, 83), (83, 87)]
		else:
		    raise ValueError('Invalid data length!')
		self.data_vln_byday = {}
		self.data_klp_byday = {}
		for day_index in range(0, 7):
			vnl_list = []
			klp_list = []
			for list_item in range(*loop_list[day_index]):
				time_vln = self.data_vln_forecast[list_item]['forecastTimeUtc']
				airTemp_vln = self.data_vln_forecast[list_item]['airTemperature']
				feelTemp_vln = self.data_vln_forecast[list_item]['feelsLikeTemperature']
				time_klp = self.data_klp_forecast[list_item]['forecastTimeUtc']
				airTemp_klp = self.data_klp_forecast[list_item]['airTemperature']
				feelTemp_klp = self.data_klp_forecast[list_item]['feelsLikeTemperature']
				
				forecast_upload_time = datetime.datetime.now()
				forecast_time = forecast_upload_time.strftime('%Y/%m/%d %H:%M:%S')
				vln_dict = {'forecastTimeUtc': time_vln,
							'airTemperature': airTemp_vln,
							'feelsLikeTemperature': feelTemp_vln,
							'forecastDownloadTime': f"{forecast_time}",			
							}
				klp_dict = {'forecastTimeUtc': time_klp,
							'airTemperature': airTemp_klp,
							'feelsLikeTemperature': feelTemp_klp,
							'forecastDownloadTime': f"{forecast_time}",			
							}
				vnl_list.append(vln_dict)
				klp_list.append(klp_dict)
			self.data_vln_byday[f'Day {day_index + 1}'] = vnl_list
			self.data_klp_byday[f'Day {day_index + 1}'] = klp_list

		# Compare new forecast data with existing data an append with new
		self.vln = open('data/forecast_vln_db.json', 'r')
		self.klp = open('data/forecast_klp_db.json', 'r')
		self.old_data_vln = json.load(self.vln)
		self.old_data_klp = json.load(self.klp)
		self.items_added = 0
		self.items_skipped = 0
		for day_index in range(0, 7):
			for dict_vln in self.data_vln_byday[f'Day {day_index + 1}']:
				timestamp_vln = dict_vln['forecastTimeUtc']
				timestamp_vln_db_list = []
				for dict_item_index in range(len(self.old_data_vln[f'Day {day_index + 1}'])):
					timestamp_vln_db_list.append(self.old_data_vln[f'Day {day_index + 1}'][dict_item_index]['forecastTimeUtc'])
				if timestamp_vln in timestamp_vln_db_list:
					self.items_skipped += 1
					continue
				self.old_data_vln[f'Day {day_index + 1}'].append(dict_vln)
				self.items_added += 1
			for dict_klp in self.data_klp_byday[f'Day {day_index + 1}']:
				timestamp_klp = dict_klp['forecastTimeUtc']
				timestamp_klp_db_list = []
				for dict_item_index in range(len(self.old_data_klp[f'Day {day_index + 1}'])):
					timestamp_klp_db_list.append(self.old_data_klp[f'Day {day_index + 1}'][dict_item_index]['forecastTimeUtc'])
				if timestamp_klp in timestamp_klp_db_list:
					continue
				self.old_data_klp[f'Day {day_index + 1}'].append(dict_klp)
				
		self.vln.close()
		self.klp.close()
		
		self.terminal.fill_terminal(log_text_message=f"Forecast items added: {self.items_added}\n")
		self.terminal.fill_terminal(log_text_message=f"Forecast items skipped: {self.items_skipped}\n")

		
		# Write new forecast data to file
		self.new_data_vln = json.dumps(self.old_data_vln)
		self.new_data_klp = json.dumps(self.old_data_klp)
		self.vln = open('data/forecast_vln_db.json', 'w')
		self.klp = open('data/forecast_klp_db.json', 'w')
		self.vln.write(self.new_data_vln)
		self.klp.write(self.new_data_klp)
		self.vln.close()
		self.klp.close()

	def get_measured(self):
		"""Gets from MeteoLT API measured data from Vilnius and Klaipeda places, saves data to file"""

		# Make a list of required measured data to download by date
		list_required = []
		list_available = []
		self.vln_f = open('data/forecast_vln_db.json', 'r')
		self.klp_f = open('data/forecast_klp_db.json', 'r')
		self.vln_data_f = json.load(self.vln_f)
		self.klp_data_f = json.load(self.klp_f)
		self.vln_f.close()
		self.klp_f.close()
		today = datetime.date.today()
		stop = False
		for day_index in range(0, 7):
			for dict_vln in self.vln_data_f[f'Day {day_index + 1}']:
				data_date = dict_vln['forecastTimeUtc'][:10]
				if data_date in list_required:
					continue
				elif datetime.datetime.strptime(data_date, '%Y-%m-%d').date() >= today:
					continue
				list_required.append(data_date)
		
		# Check if measured data files contains required data
		self.vln_measured = open('data/measured_vln_db.json', 'r')
		vln_existing = json.load(self.vln_measured)
		self.vln_measured.close()
		existing_dates = []
		for key in vln_existing.keys():
			existing_dates.append(key)
		list_required_review = []
		for date_item in list_required:
			if date_item not in existing_dates:
				list_required_review.append(date_item)
				self.terminal.fill_terminal(log_text_message=f"Data for download: {date_item}\n")
		self.terminal.fill_terminal(log_text_message=f"List for download of measured data after review: {list_required_review}\n")

		# Check if measured data files require update
		if len(list_required_review) >= 1:

			# Make API request for measured and add to dictionary by date
			self.data_vln_bydate = {}
			self.data_klp_bydate = {}
			for date_measured in list_required_review:	
				self.url_vln_measured = f"https://api.meteo.lt/v1/stations/vilniaus-ams/observations/{date_measured}"
				self.url_klp_measured = f"https://api.meteo.lt/v1/stations/klaipedos-ams/observations/{date_measured}"
				self.get_data_vln = requests.get(self.url_vln_measured)
				self.get_data_klp = requests.get(self.url_klp_measured)
				self.data_vln_measured = self.get_data_vln.json()['observations']
				self.data_klp_measured = self.get_data_klp.json()['observations']
				self.data_vln_bydate[f'{date_measured}'] = self.data_vln_measured
				self.data_klp_bydate[f'{date_measured}'] = self.data_klp_measured

			# Take from entire measured data timestamp, airtemp, feelsliketemp and sort by measurement date
			self.data_vln_bydate_short = {}
			for key_date, value_observations in self.data_vln_bydate.items():
				list_vln = []
				for item_observations in value_observations:
					vln_time = item_observations["observationTimeUtc"]
					vln_airTemp = item_observations["airTemperature"]
					vln_feelTemp = item_observations["feelsLikeTemperature"]
					vln_dict_m = {"observationTimeUtc": vln_time,
								"airTemperature": vln_airTemp,
								"feelsLikeTemperature": vln_feelTemp,	
								}
					list_vln.append(vln_dict_m)
				self.data_vln_bydate_short[f"{key_date}"] = list_vln

			self.data_klp_bydate_short = {}
			items_m_adedd = 0
			for key_date, value_observations in self.data_klp_bydate.items():
				list_klp = []
				items_m_adedd += 1
				for item_observations in value_observations:
					klp_time = item_observations["observationTimeUtc"]
					klp_airTemp = item_observations["airTemperature"]
					klp_feelTemp = item_observations["feelsLikeTemperature"]
					klp_dict_m = {"observationTimeUtc": klp_time,
								"airTemperature": klp_airTemp,
								"feelsLikeTemperature": klp_feelTemp,	
								}
					list_klp.append(klp_dict_m)
				self.data_klp_bydate_short[f"{key_date}"] = list_klp

			self.terminal.fill_terminal(log_text_message=f"Measured data added : {items_m_adedd}\n")

			# Write measured data to a json file
			self.vln_measured = open('data/measured_vln_db.json', 'r')
			self.klp_measured = open('data/measured_klp_db.json', 'r')
			vln_to_update = json.load(self.vln_measured)
			klp_to_update = json.load(self.klp_measured)
			self.vln_measured.close()
			self.klp_measured.close()
			self.vln_measured = open('data/measured_vln_db.json', 'w')
			self.klp_measured = open('data/measured_klp_db.json', 'w')
			vln_to_update.update(self.data_vln_bydate_short)
			klp_to_update.update(self.data_klp_bydate_short)
			self.data_vln_measured = json.dumps(vln_to_update)
			self.data_klp_measured = json.dumps(klp_to_update)
			self.vln_measured.write(self.data_vln_measured)
			self.klp_measured.write(self.data_klp_measured)
			self.vln_measured.close()
			self.klp_measured.close()
		else:
			self.terminal.fill_terminal(log_text_message="Measured data are up to date\n")

	def create_csv(self):
		"""Combines forecast and measured data in one separate csv file for each of seven forecast days"""

		forecast_file_vln = open('data/forecast_vln_db.json', 'r')
		vln_forecast_data = json.load(forecast_file_vln)
		measured_file_vln = open('data/measured_vln_db.json', 'r')
		vln_measured_data = json.load(measured_file_vln)
		forecast_file_vln.close()
		measured_file_vln.close()
		forecast_file_klp = open('data/forecast_klp_db.json', 'r')
		klp_forecast_data = json.load(forecast_file_klp)
		measured_file_klp = open('data/measured_klp_db.json', 'r')
		klp_measured_data = json.load(measured_file_klp)
		forecast_file_klp.close()
		measured_file_klp.close()
		days_all = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7']
		today = datetime.date.today()
		yesterday = datetime.date.today()-datetime.timedelta(1)
		days = []
		for day in days_all:
			for forecast_day_item in vln_forecast_data[day]:
				if f"{yesterday}" in f"{forecast_day_item}":
					days.append(day)
					break
				else:
					continue
		for forecast_day in days:
			csv_list_vln = []
			csv_list_klp = []
			for forecast_day_item_vln in vln_forecast_data[forecast_day]:
				date_time_vln = forecast_day_item_vln["forecastTimeUtc"]
				forec_air_temp_vln = forecast_day_item_vln["airTemperature"]
				forec_feel_temp_vln = forecast_day_item_vln["feelsLikeTemperature"]
				str_date = date_time_vln[:10]
				find_date = datetime.datetime.strptime(str_date, '%Y-%m-%d').date()
				if find_date >= today:
					break
				data_list_vln = vln_measured_data[str_date]
				for measured_day_item_vln in data_list_vln:
					compare_time_vln = measured_day_item_vln["observationTimeUtc"]
					if date_time_vln == compare_time_vln:
						meas_air_temp_vln = measured_day_item_vln["airTemperature"]
						meas_feel_temp_vln = measured_day_item_vln["feelsLikeTemperature"]
						break
					else:
						continue
				csv_list_vln.append([date_time_vln, compare_time_vln, meas_air_temp_vln, forec_air_temp_vln, meas_feel_temp_vln, forec_feel_temp_vln])
			csv_file_fields_vln = ["Date and time", "Check time", "Measured air temperature", "Forecasted air temperature", "Feelslike temperature", "Forecasted feelslike temperature"]
			file_name_vln = f"data/csv_combined_vln_{forecast_day}.csv"
			self.terminal.fill_terminal(log_text_message=f"{file_name_vln} saved\n")
			csv_file_vln = open(file_name_vln, 'w', newline='')
			csv_writer_vln = csv.writer(csv_file_vln)
			csv_writer_vln.writerow(csv_file_fields_vln)
			csv_writer_vln.writerows(csv_list_vln)
			csv_file_vln.close()
			for forecast_day_item_klp in klp_forecast_data[forecast_day]:
				date_time_klp = forecast_day_item_klp["forecastTimeUtc"]
				forec_air_temp_klp = forecast_day_item_klp["airTemperature"]
				forec_feel_temp_klp = forecast_day_item_klp["feelsLikeTemperature"]
				str_date = date_time_klp[:10]
				find_date = datetime.datetime.strptime(str_date, '%Y-%m-%d').date()
				if find_date >= today:
					break
				data_list_klp = klp_measured_data[str_date]
				for measured_day_item_klp in data_list_klp:
					compare_time_klp = measured_day_item_klp["observationTimeUtc"]
					if date_time_klp == compare_time_klp:
						meas_air_temp_klp = measured_day_item_klp["airTemperature"]
						meas_feel_temp_klp = measured_day_item_klp["feelsLikeTemperature"]
						break
					else:
						continue
				csv_list_klp.append([date_time_klp, compare_time_klp, meas_air_temp_klp, forec_air_temp_klp, meas_feel_temp_klp, forec_feel_temp_klp])
			csv_file_fields_klp = ["Date and time", "Check time", "Measured air temperature", "Forecasted air temperature", "Feelslike temperature", "Forecasted feelslike temperature"]
			file_name_klp = f"data/csv_combined_klp_{forecast_day}.csv"
			self.terminal.fill_terminal(log_text_message=f"{file_name_klp} saved\n")
			csv_file_klp = open(file_name_klp, 'w', newline='')
			csv_writer_klp = csv.writer(csv_file_klp)
			csv_writer_klp.writerow(csv_file_fields_klp)
			csv_writer_klp.writerows(csv_list_klp)
			csv_file_klp.close()

	def analyze(self):
		"""Show csv files content in matplotlib graph"""
		filename = 'data/csv_combined_vln_Day 1.csv'
		with open(filename) as f:
		    reader = csv.reader(f)
		    header_row = next(reader)

		    # Get dates, and temperatures from  this file.
		    dates, measureds, forecasteds, feelslikeds, f_feelslikeds = [], [], [], [], []
		    for row in reader:
		        date = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
		        try:
		            measured = float(row[2])
		            forecasted = float(row[3])
		            feelsliked = float(row[4])
		            f_feelsliked =float(row[5])
		        except ValueError:
		            print(f"Missing data for {date}")
		        else:
		            dates.append(date)
		            measureds.append(measured)
		            forecasteds.append(forecasted)
		            feelslikeds.append(feelsliked)
		            f_feelslikeds.append(f_feelsliked)

		# Plot the measured and forecasted temperatures.
		plt.style.use('bmh')#('fivethirtyeight')('ggplot')('dark_background')
		fig, ax = plt.subplots()
		ax.plot(dates, measureds, c='red', alpha=0.5, label="Air temp measured")
		ax.plot(dates, forecasteds, c='orange', alpha=0.5, label="Forecasted air temp")
		ax.plot(dates, feelslikeds, c='green', alpha=0.5, label="Air temp feelslike")
		ax.plot(dates, f_feelslikeds, c='olive', alpha=0.5, label="Forecasted temp feelslike")
		ax.scatter(dates, measureds, c='red', s=8)
		ax.scatter(dates, forecasteds, c='orange', s=8)
		ax.scatter(dates, feelslikeds, c='green', s=8)
		ax.scatter(dates, f_feelslikeds, c='olive', s=8)
		plt.fill_between(dates, measureds, forecasteds, facecolor='red', alpha=0.1)
		plt.fill_between(dates, feelslikeds, f_feelslikeds, facecolor='green', alpha=0.1)
		ax.legend(loc="upper left")

		# Format plot.
		title = "Daily measured and forecasted temperatures\n2023 March, Vilnius, Lithuania"
		plt.title(title, fontsize=14)
		plt.xlabel('Date and time', fontsize=10)
		fig.autofmt_xdate()
		plt.ylabel("Temperature (C)", fontsize=10)
		plt.tick_params(axis='both', which='major', labelsize=6)
		fig.tight_layout()
		self.terminal.fill_terminal(log_text_message=f"Showing data csv Vilnius Day 1 in separate graph for review\n")
		plt.show()
