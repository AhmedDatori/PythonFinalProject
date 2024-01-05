import csv

# A function to calculate the SMA for each 5 days of the data
def calculate_sma(data, window=5):
    # load the data from the orcl.csv file into a list of dictionaries
    def load_data(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    data = load_data('orcl.csv')

    
    sma_values = []
    # for loop to each day of the data
    for i in range(len(data)):
        # strat calculating after day 4 
        if i >= window - 1:
            # alist of the values if each day of the last five days
            window_prices = [float(data[j]['Close']) for j in range(i - window + 1, i + 1)]
            # sum the values and devide them by 5
            sma = sum(window_prices) / window
            # add them to the sma list
            sma_values.append({'Date': data[i]['Date'], 'SMA': sma})
    return sma_values