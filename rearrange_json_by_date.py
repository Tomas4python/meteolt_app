import json
import datetime

def rearrange_json_data_by_date(terminal_instance_ref):
	"""Function for rearangement of data in json files by date""" 

	vln = open('data/forecast_vln_db.json', 'r')
	klp = open('data/forecast_klp_db.json', 'r')
	old_data_vln = json.load(vln)
	old_data_klp = json.load(klp)
	vln.close()
	klp.close()

	days_to_rearrange = ["Day 3", "Day 6"] #Add more days if necessary
	for day in days_to_rearrange:	
		
		# Take out the values of the Day [looped] from the main nested dictionary as a lists of dictionaries
		day_list_vln = old_data_vln[day]
		day_list_klp = old_data_klp[day]
		# Sort list by the forecast datetimestamp
		# Example of datetimestamp in dictionary: "forecastTimeUtc": "2023-03-07 16:00:00"
		day_list_vln.sort(key = lambda x: datetime.datetime.strptime(x["forecastTimeUtc"], "%Y-%m-%d %H:%M:%S"))
		day_list_klp.sort(key = lambda x: datetime.datetime.strptime(x["forecastTimeUtc"], "%Y-%m-%d %H:%M:%S"))
		# Return the value of the Day [looped] back to the main nested dictionary
		old_data_vln[day] = day_list_vln
		old_data_klp[day] = day_list_klp

	vln = open('data/forecast_vln_db.json', 'w')
	new_data_vln = json.dumps(old_data_vln)
	vln.write(new_data_vln)
	vln.close()
	terminal_instance_ref.fill_terminal(log_text_message="File 'forecast_vln_db.json' saved\n")

	klp = open('data/forecast_klp_db.json', 'w')
	new_data_klp = json.dumps(old_data_vln)
	klp.write(new_data_klp)
	klp.close()
	terminal_instance_ref.fill_terminal(log_text_message="File 'forecast_klp_db.json' saved\n")

	terminal_instance_ref.fill_terminal(log_text_message="Json data rearranged by date successfully...\n")
