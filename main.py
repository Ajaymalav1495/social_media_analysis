import pandas as pd  # pandas
import numpy as np  # numpy
import seaborn as sns  # seaborn
import matplotlib.pyplot as plt  # plotting
import streamlit as st
from streamlit_option_menu import option_menu

from data_c import data_c
from gender import Gender
from time1 import Spending_Time
from platform1 import Social_Media_Platform
from interests import Interests
from states import States  
from income import Income_And_Age
from Demo import Demographics
from profession import Profession  
from dept import In_Dept
from home_own import Own_a_Home
from car_own import Own_a_Car  
from age import Age


# Sidebar menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",  # Required
        options=[
            "Home", "Age","Gender", "Spending Time", "Social Media Platform", "Interests",
            "States", "Income And Age", "Demographics", "Profession", "In Debt", 
            "Own a Home", "Own a Car"
        ],  # Required
        menu_icon="cast",  # Optional
        default_index=0,  # Optional
    )


if selected == "Home":
    data_c()
elif selected == "Gender":
    Gender()
elif selected == "Spending Time":
    Spending_Time()
elif selected == "Social Media Platform":
    Social_Media_Platform()
elif selected == "Interests":
    Interests()
elif selected == "States":
    States()
elif selected == "Income And Age":
    Income_And_Age()
elif selected == "Demographics":
    Demographics()
elif selected == "Profession":
    Profession()
elif selected == "In Debt":
    In_Dept()
elif selected == "Own a Home":
   Own_a_Home()
elif selected == "Own a Car":
    Own_a_Car()
elif selected == "Age":
    Age()
