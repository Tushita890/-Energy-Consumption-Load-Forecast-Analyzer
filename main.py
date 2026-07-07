# following file tushi67.csv contains the data this particular code shous data visualization for energy consumption load forecast analyzer 

import pandas as pd 
df=pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")
print(df)

import pandas as pd

df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime column (recommended)
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Count valid datetime entries
count_datetime = df['Datetime'].count()

print("Count of Datetime entries:", count_datetime)


import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Calculate total consumption for each column
pc1 = df['PowerConsumption_Zone1'].sum()
pc2 = df['PowerConsumption_Zone2'].sum()
pc3 = df['PowerConsumption_Zone3'].sum()

# Total of all power consumption
total = pc1 + pc2 + pc3

# Calculate percentages
percentages = [
    (pc1 / total) * 100,
    (pc2 / total) * 100,
    (pc3 / total) * 100
]

labels = ['PowerConsumption_Zone1', 'PowerConsumption_Zone2', 'PowerConsumption_Zone3']

# Plot Pie Chart
plt.figure()
plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Percentage Contribution of Power Consumption')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV file
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")
min_zone1 = df['PowerConsumption_Zone1'].min()
min_zone2 = df['PowerConsumption_Zone2'].min()
min_zone3 = df['PowerConsumption_Zone3'].min()

print("Minimum values:")
print("Zone 1:", min_zone1)
print("Zone 2:", min_zone2)
print("Zone 3:", min_zone3)

# Maximum value in each column
max_zone1 = df['PowerConsumption_Zone1'].max()
max_zone2 = df['PowerConsumption_Zone2'].max()
max_zone3 = df['PowerConsumption_Zone3'].max()

print("Maximum values:")
print("Zone 1:", max_zone1)
print("Zone 2:", max_zone2)
print("Zone 3:", max_zone3)

# Average (mean) value for each column
avg_zone1 = df['PowerConsumption_Zone1'].mean()
avg_zone2 = df['PowerConsumption_Zone2'].mean()
avg_zone3 = df['PowerConsumption_Zone3'].mean()

print("Average values:")
print("Zone 1:", avg_zone1)
print("Zone 2:", avg_zone2)
print("Zone 3:", avg_zone3)

zones = ['Zone 1', 'Zone 2', 'Zone 3']

min_values = [min_zone1, min_zone2, min_zone3]
avg_values = [avg_zone1, avg_zone2, avg_zone3]
max_values = [max_zone1, max_zone2, max_zone3]

x = np.arange(len(zones))
width = 0.25

plt.figure()
plt.bar(x - width, min_values, width, label='Minimum')
plt.bar(x, avg_values, width, label='Average')
plt.bar(x + width, max_values, width, label='Maximum')

plt.xlabel('Zones')
plt.ylabel('Power Consumption')
plt.title('Minimum, Average, and Maximum Power Consumption by Zone')
plt.xticks(x, zones)
plt.legend()
plt.tight_layout()
plt.show()

import pandas as pd


# Load CSV
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract Hour
df['Hour'] = df['Datetime'].dt.hour

# Total Power Consumption
df['Total_Power'] = (
    df['PowerConsumption_Zone1'] +
    df['PowerConsumption_Zone2'] +
    df['PowerConsumption_Zone3']
)

# Classify Peak and Off-Peak based on time
df['Load_Type'] = df['Hour'].apply(
    lambda x: 'Peak' if 8 <= x < 22 else 'Off-Peak'
)

# Find Peak MAX and Off-Peak MIN
peak_max = df[df['Load_Type'] == 'Peak']['Total_Power'].max()
offpeak_min = df[df['Load_Type'] == 'Off-Peak']['Total_Power'].min()

print("Peak Load (Maximum):", peak_max)
print("Off-Peak Load (Minimum):", offpeak_min)


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV file
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract Hour
df['Hour'] = df['Datetime'].dt.hour

# Group by Hour and calculate mean power consumption
heatmap_data = df.groupby('Hour')[
    ['PowerConsumption_Zone1',
     'PowerConsumption_Zone2',
     'PowerConsumption_Zone3']
].mean()

# Convert to numpy array and transpose (Zones as rows)
data = heatmap_data.T.values

zones = ['Zone 1', 'Zone 2', 'Zone 3']
hours = heatmap_data.index

# Plot heatmap
plt.figure(figsize=(12, 4))
plt.imshow(data, aspect='auto')

# Add color bar
plt.colorbar(label='Average Power Consumption')

# Axis labels
plt.xlabel('Hour of Day')
plt.ylabel('Zones')
plt.title('Zone-wise Power Consumption Heatmap (Hour vs Zone)')

# Ticks
plt.xticks(np.arange(len(hours)), hours)
plt.yticks(np.arange(len(zones)), zones)

plt.tight_layout()
plt.show()


import pandas as pd

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract Hour
df['Hour'] = df['Datetime'].dt.hour

# Total Power Consumption
df['Total_Power'] = (
    df['PowerConsumption_Zone1'] +
    df['PowerConsumption_Zone2'] +
    df['PowerConsumption_Zone3']
)

# Classify Peak and Off-Peak
df['Load_Type'] = df['Hour'].apply(
    lambda x: 'Peak' if 8 <= x < 22 else 'Off-Peak'
)

# -----------------------------
# Peak MAX (with Hour)
# -----------------------------
peak_df = df[df['Load_Type'] == 'Peak']
peak_row = peak_df.loc[peak_df['Total_Power'].idxmax()]

# -----------------------------
# Off-Peak MIN (with Hour)
# -----------------------------
offpeak_df = df[df['Load_Type'] == 'Off-Peak']
offpeak_row = offpeak_df.loc[offpeak_df['Total_Power'].idxmin()]

# Print results
print("Peak Load (Maximum):", peak_row['Total_Power'], 
      "at Hour:", peak_row['Hour'])

print("Off-Peak Load (Minimum):", offpeak_row['Total_Power'], 
      "at Hour:", offpeak_row['Hour'])


import pandas as pd

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract Hour and Date
df['Hour'] = df['Datetime'].dt.hour
df['Date'] = df['Datetime'].dt.date

# Total Power Consumption
df['Total_Power'] = (
    df['PowerConsumption_Zone1'] +
    df['PowerConsumption_Zone2'] +
    df['PowerConsumption_Zone3']
)

# Classify Peak and Off-Peak
df['Load_Type'] = df['Hour'].apply(
    lambda x: 'Peak' if 8 <= x < 22 else 'Off-Peak'
)

# -----------------------------
# Peak MAX (with Date & Hour)
# -----------------------------
peak_df = df[df['Load_Type'] == 'Peak']
peak_row = peak_df.loc[peak_df['Total_Power'].idxmax()]

# -----------------------------
# Off-Peak MIN (with Date & Hour)
# -----------------------------
offpeak_df = df[df['Load_Type'] == 'Off-Peak']
offpeak_row = offpeak_df.loc[offpeak_df['Total_Power'].idxmin()]

# Print results
print(
    "Peak Load (Maximum):", peak_row['Total_Power'],
    "| Date:", peak_row['Date'],
    "| Hour:", peak_row['Hour']
)

print(
    "Off-Peak Load (Minimum):", offpeak_row['Total_Power'],
    "| Date:", offpeak_row['Date'],
    "| Hour:", offpeak_row['Hour']
)


import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract day of week (0 = Monday, 6 = Sunday)
df['DayOfWeek'] = df['Datetime'].dt.dayofweek

# Classify Weekday / Weekend
df['Day_Type'] = df['DayOfWeek'].apply(
    lambda x: 'Weekend' if x >= 5 else 'Weekday'
)

# Total Power Consumption
df['Total_Power'] = (
    df['PowerConsumption_Zone1'] +
    df['PowerConsumption_Zone2'] +
    df['PowerConsumption_Zone3']
)

# Average consumption
weekday_avg = df[df['Day_Type'] == 'Weekday']['Total_Power'].mean()
weekend_avg = df[df['Day_Type'] == 'Weekend']['Total_Power'].mean()

print("Average Weekday Consumption:", weekday_avg)
print("Average Weekend Consumption:", weekend_avg)

labels = ['Weekday', 'Weekend']
values = [weekday_avg, weekend_avg]

plt.figure()
plt.bar(labels, values)
plt.xlabel('Day Type')
plt.ylabel('Average Power Consumption')
plt.title('Weekday vs Weekend Power Consumption')
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract Date and Hour
df['Date'] = df['Datetime'].dt.date
df['Hour'] = df['Datetime'].dt.hour

# Total Power Consumption
df['Total_Power'] = (
    df['PowerConsumption_Zone1'] +
    df['PowerConsumption_Zone2'] +
    df['PowerConsumption_Zone3']
)
# Define risk threshold (90% of max load)
risk_threshold = 0.9 * df['Total_Power'].max()

print("Peak Load Risk Threshold:", risk_threshold)
# Identify risky periods
df['Peak_Risk'] = df['Total_Power'].apply(
    lambda x: 'High Risk' if x >= risk_threshold else 'Normal'
)

# Show peak risk records
risk_periods = df[df['Peak_Risk'] == 'High Risk']

print("\nPeak Load Risk Periods:")
print(risk_periods[['Date', 'Hour', 'Total_Power']].head())
plt.figure()
plt.plot(df['Datetime'], df['Total_Power'], label='Total Power')
plt.axhline(risk_threshold, linestyle='--', label='Risk Threshold')

plt.xlabel('Datetime')
plt.ylabel('Total Power Consumption')
plt.title('Peak Load Risk Identification')
plt.legend()
plt.tight_layout()
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv(r"C:\Users\HP\Desktop\tushi67.csv")

# Convert Datetime
df['Datetime'] = pd.to_datetime(df['Datetime'], errors='coerce')

# Extract Date and Hour
df['Date'] = df['Datetime'].dt.date
df['Hour'] = df['Datetime'].dt.hour

# Total Power Consumption
df['Total_Power'] = (
    df['PowerConsumption_Zone1'] +
    df['PowerConsumption_Zone2'] +
    df['PowerConsumption_Zone3']
)
df['Load_Type'] = df['Hour'].apply(
    lambda x: 'Peak' if 8 <= x < 22 else 'Off-Peak'
)
peak_avg_original = df[df['Load_Type'] == 'Peak']['Total_Power'].mean()
offpeak_avg_original = df[df['Load_Type'] == 'Off-Peak']['Total_Power'].mean()

print("Original Peak Load:", peak_avg_original)
print("Original Off-Peak Load:", offpeak_avg_original)
shift_percentage = 0.20

shift_amount = peak_avg_original * shift_percentage

peak_balanced = peak_avg_original - shift_amount
offpeak_balanced = offpeak_avg_original + shift_amount

print("Balanced Peak Load:", peak_balanced)
print("Balanced Off-Peak Load:", offpeak_balanced)

labels = ['Peak', 'Off-Peak']

original = [peak_avg_original, offpeak_avg_original]
balanced = [peak_balanced, offpeak_balanced]

x = range(len(labels))

plt.figure()
plt.bar(x, original, label='Original Load')
plt.bar(x, balanced, bottom=original, label='Balanced Load')

plt.xticks(x, labels)
plt.xlabel('Load Type')
plt.ylabel('Average Power Consumption')
plt.title('Demand Balancing Simulation (Load Shifting)')
plt.legend()
plt.tight_layout()
plt.show()





