import pandas as pd
import mplfinance as mpf
import pytz

# Load the data from a CSV file
data = pd.read_csv('/data/sber_june_2_2023.csv', delimiter=';', header=None)

# Rename the columns for readability
data.columns = ['Ticker', 'Time', 'Open', 'Close', 'High', 'Low', 'Volume']

# Reorder the columns
data = data[['Time', 'Open', 'Close', 'High', 'Low', 'Volume']]

# Convert the 'time' column from UTC to Moscow time
utc_timezone = pytz.timezone('UTC')
moscow_timezone = pytz.timezone('Europe/Moscow')
data['Time'] = pd.to_datetime(data['Time'], unit='s').dt.tz_localize(utc_timezone).dt.tz_convert(moscow_timezone)

# Set the 'Time' column as the index
data.set_index('Time', inplace=True)

# First we set the kwargs that we will use for all of these examples:
kwargs = dict(type='candle',mav=(2,4,6),volume=True,figratio=(11,8),figscale=0.85,title='Market Chart', ylabel='Price', show_nontrading=False, style='charles')

# Create a Japanese candlestick chart
mpf.plot(data, **kwargs, savefig='/data/sber_may.png', datetime_format='%Y-%m-%d, %H:%M')
