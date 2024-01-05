from calculate_rsi import calculate_rsi
from calculate_sma import calculate_sma
import data_load_save as dls

# Load the data we are going to use
data = dls.load_data('orcl.csv')

# cCalculate the SMA based on the Data
sma_data = calculate_sma(data)

# Calculate the RSI based on the Data
rsi_data = calculate_rsi(data)

# Save both data as a csv files
dls.write_to_csv(sma_data, 'orcl-sma.csv')
dls.write_to_csv(rsi_data, 'orcl-rsi.csv')