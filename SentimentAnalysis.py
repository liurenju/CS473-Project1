import csv
groupon_file = "resturant-feedback-1.csv"
	
def read_dataset(file_name):	
	data = []
	counter=0
	with open(file_name) as f:
		reader = csv.reader(f,delimiter='\n');
		for row in reader:
			if counter==0 or counter ==1:
				counter = counter + 1
				continue
			line = []
			content = row[0]
			line.append(content[1])
			line.append(content[2:].rstrip().lstrip())
			data.append(line)
			counter = counter + 1
	f.close()
	return data

data_list = read_dataset(groupon_file)
print data_list[0]

