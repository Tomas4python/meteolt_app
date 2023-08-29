import csv

def remove_duplicates_from_csv_data():

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
			rows = []
			datetime_stamps = []
			for row in reader:
				datetime_stamp = row[0]
				if datetime_stamp in datetime_stamps:
					print(datetime_stamp)
					continue
				datetime_stamps.append(datetime_stamp)
				rows.append(row)
		
		with open("data/" + file_name + "_reviewed", 'w', newline='') as file:
			csv_writer = csv.writer(file)
			csv_writer.writerow(header_row)
			csv_writer.writerows(rows)
