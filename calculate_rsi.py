import csv

# Function to calculate the RSI on 14 days period
def calculate_rsi(data, periods=14):
    # load the data from the orcl.csv file into a list of dictionaries
    def load_data(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data

    data = load_data('orcl.csv')

    
    # initial our lists
    gain = []
    losse = []
    rsi_values = []

    # go throw every raw in the data
    for i in range(1, len(data)):
        # Calculate the change in Close price by each day 
        change = float(data[i]['Close']) - float(data[i - 1]['Close'])
        # if the change is in positive that means add it to the gain list otherwise add 0
        gain.append(max(change, 0))
        # if the change is in negative that means add it to the losse list otherwise add 0
        losse.append(abs(min(change, 0)))

        # start after the period day which is 14
        if i >= periods:
            # start calculating avrage in the gain and loss for each day deviding it by the period
            avg_gain = sum(gain[-periods:]) / periods
            avg_loss = sum(losse[-periods:]) / periods
            # the folrmula you gave in the pdf
            rs = avg_gain / avg_loss if avg_loss != 0 else 0
            rsi = 100 - (100 / (1 + rs))
            rsi_values.append({'Date': data[i]['Date'], 'RSI': rsi})

    return rsi_values
