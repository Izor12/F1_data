import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
import fastf1 as ff1
import fastf1.plotting 
import pandas as pd
from datetime import datetime

#%matplotlib inline
fastf1.plotting.setup_mpl(color_scheme="fastf1")
#ff1.Cache.enable_cache(r"D:\fastf1_cache/")
ff1.Cache.disabled()
st.set_page_config(page_title="F1 Data Analysis",
                   page_icon= ':racing_car:',)



st.header('F1 Data Analysis Qualifying',divider='gray')

def ret_drivers(year,race,sesh):
    session = fastf1.get_session(year,race,sesh)
    session.load()
    drivers = []
    driver_displ = []
    for i in session.drivers:
        drivers.append(session.get_driver(i)["Abbreviation"])
        driver_displ.append("-".join([session.get_driver(i)["Abbreviation"],session.get_driver(i)["FullName"]])) 
    return [drivers,driver_displ]
def ret_races(year):
    session = fastf1.get_event_schedule(year)
    return list(session["Location"])
class quali_two:
    def __init__(self,driver1,driver2,session):
        self.driver1 = driver1
        self.driver2 = driver2
        self.session = session
        quali = ff1.get_session(self.session[0],self.session[1],self.session[2])
        quali.load(telemetry=True,laps=True)
        self.quali = quali
        self.laps_driver1 = quali.laps.pick_driver(self.driver1)
        self.laps_driver2 = quali.laps.pick_driver(self.driver2)
        
        
    def data_fab(self):
        driver1_fastest = self.laps_driver1.pick_fastest()
        tel_driver1 = driver1_fastest.get_car_data().add_distance()
        tel_driver1["Time"] =(tel_driver1['Time'].dt.microseconds // 1000 + tel_driver1['Time'].dt.seconds * 1000)/1000
        
        driver2_fastest = self.laps_driver2.pick_fastest()
        tel_driver2 = driver2_fastest.get_car_data().add_distance()
        tel_driver2["Time"] =(tel_driver2['Time'].dt.microseconds // 1000 + tel_driver2['Time'].dt.seconds * 1000)/1000
        return [driver1_fastest,tel_driver1,driver2_fastest,tel_driver2]
    
    def name_dri1(self):
        return self.quali.get_driver(self.driver1)["FullName"]
    def name_dri2(self):
        return self.quali.get_driver(self.driver2)["FullName"]
   

    def telemetery_driver1(self):
        tel_driver1 = self.data_fab()[1]
        fig, ax = plt.subplots(3)
        fig.suptitle("Quali {}".format(self.name_dri1()))
        ax[0].plot(tel_driver1["Time"],tel_driver1['Speed'], label = self.quali.get_driver(self.driver1)["FullName"])
        ax[1].plot(tel_driver1['Time'], tel_driver1['Throttle'], label=self.quali.get_driver(self.driver1)["FullName"])
        ax[2].plot(tel_driver1['Time'], tel_driver1['Brake'], label=self.quali.get_driver(self.driver1)["FullName"])
        
        ax[1].legend(loc = "lower left")
        ax[0].set(ylabel=  "Speed")
        ax[1].set(ylabel='Throttle')
        ax[2].set(ylabel='Brakes') 
        ax[2].set(xlabel = "Time in Seconds")

        st.pyplot(fig)
    
    def telemetery_driver2(self):
        tel_driver2 = self.data_fab()[3]
        fig, ax = plt.subplots(3)
        
        fig.suptitle("Quali {}".format(self.name_dri2()))
        ax[0].plot(tel_driver2["Time"],tel_driver2['Speed'], label = self.quali.get_driver(self.driver2)["FullName"])
        ax[1].plot(tel_driver2['Time'], tel_driver2['Throttle'], label=self.quali.get_driver(self.driver2)["FullName"])
        ax[2].plot(tel_driver2['Time'], tel_driver2['Brake'], label=self.quali.get_driver(self.driver2)["FullName"])

        ax[1].legend(loc = "lower left")
        ax[0].set(ylabel=  "Speed")
        ax[1].set(ylabel='Throttle')
        ax[2].set(ylabel='Brakes') 
        ax[2].set(xlabel = "Time in Seconds")
        st.pyplot(fig)
        
        
        
    #CHANGE\/\/    
    def compare(self):
        temp_data = self.data_fab()
        tel_driver1 = temp_data[1]
        tel_driver2 = temp_data[3]
        fig, ax = plt.subplots(3)
        fig.suptitle("Quali {} VS {}".format(self.driver1,self.driver2))
        ax[0].plot(tel_driver1["Time"],tel_driver1['Speed'], label = self.quali.get_driver(self.driver1)["FullName"])
        ax[1].plot(tel_driver1['Time'], tel_driver1['Throttle'], label=self.quali.get_driver(self.driver1)["FullName"])
        ax[2].plot(tel_driver1['Time'], tel_driver1['Brake'], label=self.quali.get_driver(self.driver1)["FullName"])
        
        
        
        ax[0].set(ylabel=  "Speed")
        ax[1].set(ylabel='Throttle')
        ax[2].set(ylabel='Brakes') 
        ax[2].set(xlabel = "Time in Seconds")
        
        
        
        ax[0].plot(tel_driver2["Time"],tel_driver2['Speed'], label = self.quali.get_driver(self.driver2)["FullName"])
        ax[1].plot(tel_driver2['Time'], tel_driver2['Throttle'], label=self.quali.get_driver(self.driver2)["FullName"])
        ax[2].plot(tel_driver2['Time'], tel_driver2['Brake'], label=self.quali.get_driver(self.driver2)["FullName"])
        ax[1].legend(loc = "lower left")
        st.pyplot(fig)

year = st.slider("Select an year", 1950, 2024, datetime.now().year)

event = st.selectbox(
    "Select a Race",
    (ret_races(year)),
)

temp = ret_drivers(year,event,"Q")
drivers  = temp[0]
driver_disp = temp[1]


driver1 = st.selectbox(
    "Select a driver",
    (driver_disp),
)
driver2= st.selectbox(
    "Select a Race",
    (driver_disp),
)
spa = quali_two(driver1.split("-")[0],driver2.split("-")[0],[year,event,"Q"])

print(spa.quali.event)
spa.telemetery_driver1()
spa.telemetery_driver2()
spa.compare()