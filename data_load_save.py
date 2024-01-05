import csv

# load the data from the orcl.csv file into a list of dictionaries
def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data


# a function to create the csv files
def write_to_csv(data, filename):
    # w for writing
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)