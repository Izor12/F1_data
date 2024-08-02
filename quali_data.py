import fastf1
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline
session  =fastf1.get_session(2024,12,"Q")
session.load()
# session  =fastf1.get_session(2024,12,"Q")
# session.load()
dic = {}

df = session.car_data["63"]
df['Date'] = pd.to_datetime(df['Date'])

# Calculate the time difference between consecutive rows
df['Time_Diff'] = df['Date'].diff()

# Shift the 'Time_Diff' column to align with the previous row
df['Time_Diff'] = df['Time_Diff'].shift(-1)



df[df['RPM']>0]
dic["GR"] = df[(df['Time'] >"0 days 01:21:35.888000")& (df["Time"]< "0 days 01:23:01.707000")]
dic["GR"]['Cumulative_Time_Diff'] = dic["GR"]['Time_Diff'].cumsum()

dic["GR"]['Time_Diff_Millis'] = dic["GR"]['Time_Diff'].dt.microse conds // 1000 + dic["GR"]['Time_Diff'].dt.seconds * 1000
dic["GR"]['Cumulative_Time_Diff_Millis'] = dic["GR"]['Time_Diff_Millis'].cumsum()/1000



fig, axes = plt.subplots(nrows=2, ncols=1)
axes[0].plot(dic["GR"]["Cumulative_Time_Diff_Millis"],dic["GR"]["Throttle"],'r')
axes[0].set_ylabel("Throttle")
axes[1].plot(dic["GR"]["Cumulative_Time_Diff_Millis"],dic["GR"]["nGear"],'purple')
axes[1].set_ylabel("Gears")
axes[1].set_xlabel("Time")