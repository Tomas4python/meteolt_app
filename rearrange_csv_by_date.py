import csv
import datetime
from pprint import pprint as pp


def rearrange_csv_data_by_date(terminal_instance_ref):
	"""Function for rearangement of data in csv files by date"""

	file_list = [
				'csv_combined_klp_Day 1.csv',
				'csv_combined_klp_Day 2.csv',
				'csv_combined_klp_Day 3.csv',
				'csv_combined_klp_Day 4.csv',
				'csv_combined_klp_Day 5.csv',
				'csv_combined_klp_Day 6.csv',
				'csv_combined_klp_Day 7.csv',
				'csv_combined_vln_Day 1.csv',
				'csv_combined_vln_Day 2.csv',
				'csv_combined_vln_Day 3.csv',
				'csv_combined_vln_Day 4.csv',
				'csv_combined_vln_Day 5.csv',
				'csv_combined_vln_Day 6.csv',
				'csv_combined_vln_Day 7.csv',
				]

	for file_name in file_list:
		with open("data/" + file_name, 'r') as file:
			reader = csv.reader(file)
			header_row = next(reader)
			datetime_stamps = []
			rows = []
			for row in reader:
				datetime_stamp = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
				rows.append((datetime_stamp, row))

		rows.sort(key=lambda x: x[0])

		with open("data/" + file_name, 'w', newline='') as file:
			terminal_instance_ref.fill_terminal(log_text_message="file: " + file_name + " saved\n")
			csv_writer = csv.writer(file)
			csv_writer.writerow(header_row)
			csv_writer.writerows(row[1] for row in rows)

	terminal_instance_ref.fill_terminal(log_text_message="Csv data rearranged by date successfully...\n")
