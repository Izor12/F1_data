import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
import fastf1 as ff1
import fastf1.plotting 
import pandas as pd
#%matplotlib inline
fastf1.plotting.setup_mpl(color_scheme="fastf1")
ff1.Cache.enable_cache(r"D:\fastf1_cache/")
class quali_two:
    def __init__(self,driver1,driver2,session):
        self.driver1 = driver1
        self.driver2 = driver2
        self.session = session
        self.quali = ff1.get_session(self.session[0],self.session[1],self.session[2])
        quali.load(telemetry=True,laps=True)
        self.laps_driver1 = quali.laps.pick_driver(self.driver1)
        self.laps_driver2 = quali.laps.pick_driver(self.driver2)

    
    def name_dri1(self):
        return quali.get_driver(self.driver1)["FullName"]
    def name_dri2(self):
        return quali.get_driver(self.driver2)["FullName"]
    def telemetery_driver1(self):
        driver1_fastest = self.laps_driver1.pick_fastest()
        tel_driver1 = driver1_fastest.get_car_data().add_distance()
        fig, ax = plt.subplots(3)
        fig.suptitle("Quali {}".format(self.name_dri1()))
        ax[0].plot(tel_driver1["Distance"],tel_driver1['Speed'], label = quali.get_driver(self.driver1)["FullName"])
        ax[0].set(ylabel=  "Speed")
        ax[1].plot(tel_driver1['Distance'], tel_driver1['Throttle'], label=quali.get_driver(self.driver1)["FullName"])
        ax[1].set(ylabel='Throttle')
        ax[2].plot(tel_driver1['Distance'], tel_driver1['Brake'], label=quali.get_driver(self.driver1)["FullName"])
        ax[2].set(ylabel='Brakes') 
        ax[2].set(xlabel = "Distance")
    def telemetery_driver2(self):
        driver2_fastest = self.laps_driver2.pick_fastest()
        tel_driver2 = driver2_fastest.get_car_data().add_distance()
        fig, ax = plt.subplots(3)
        fig.suptitle("Quali {}".format(self.name_dri1()))
        ax[0].plot(tel_driver2["Distance"],tel_driver2['Speed'], label = quali.get_driver(self.driver2)["FullName"])
        ax[0].set(ylabel=  "Speed")
        ax[1].plot(tel_driver2['Distance'], tel_driver2['Throttle'], label=quali.get_driver(self.driver2)["FullName"])
        ax[1].set(ylabel='Throttle')
        ax[2].plot(tel_driver2['Distance'], tel_driver2['Brake'], label=quali.get_driver(self.driver2)["FullName"])
        ax[2].set(ylabel='Brakes') 
        ax[2].set(xlabel = "Distance")
quali_two("RUS","HAM",[2024,12,"Q"]).telemetery_driver1()