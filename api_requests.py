import requests

class ApiRequests:
	"""All API rquests functions organized in one class"""
	
	def __init__(self):
		"""Initializes default variables of the class"""
		self.api_url_m_stations = "https://api.meteo.lt/v1/stations"
		self.api_url_f_places = "https://api.meteo.lt/v1/places"
		
	def get_stations(self):
		"""Returns a list of weather stations for which measured data is provided"""
		stations_list_json = requests.get(self.api_url_m_stations)
		stations_list = stations_list_json.json()
		return stations_list

	def get_places(self):
		"""Returns a list of locations for which weather forecast data is provided."""
		places_list_json = requests.get(self.api_url_f_places)
		places_list = places_list_json.json()
		return places_list

	def get_latest(self, station_code):
		"""Returns by the station code the latest data of observations measured by the station."""
		api_url_latest = f"https://api.meteo.lt/v1/stations/{station_code}/observations/latest"
		measured_latest_json = requests.get(api_url_latest)
		measured_latest = measured_latest_json.json()
		return measured_latest

	def get_measured(self, station_code, date):
		"""Returns by the station code and date data of observations measured by the station."""
		api_url_measured = f"https://api.meteo.lt/v1/stations/{station_code}/observations/{date}"
		measured_data_json = requests.get(api_url_measured)
		measured_data = measured_data_json.json()
		return measured_data

	def get_forecast(self, place_code):
		"""Returns by the the area code 7-day weather forecast for the area."""
		api_url_forecast = f"https://api.meteo.lt/v1/places/{place_code}/forecasts/long-term"
		forecast_data_json = requests.get(api_url_forecast)
		forecast_data = forecast_data_json.json()
		return forecast_data
