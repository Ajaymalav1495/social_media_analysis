import pandas as pd  # pandas
import numpy as np  # numpy
import seaborn as sns  # seaborn
import matplotlib.pyplot as plt  # plotting
import streamlit as st
def Spending_Time():
    st.header("3 .Comparsion Accoding spenting time in social media" )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""sns.set(rc={'figure.figsize':(20,7.5)})
ax = sns.countplot(x = "time_spent", data =df)
for i in ax.containers: 
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    sns.set(rc={'figure.figsize':(20,7.5)})
    ax = sns.countplot(x = "time_spent", data =df)
    for i in ax.containers: 
        ax.bar_label(i)

    st.pyplot(plt)

    st.code(" # Comparsion between time_spent and gender : \n df.groupby(['gender'],as_index=False)['time_spent'].sum().sort_values(by='time_spent',ascending=False)")
    st.write(#Comparsion between time_spent and gender :
            df.groupby(['gender'],as_index=False)['time_spent'].sum().sort_values(by='time_spent',ascending=False))
    
    st.markdown("## Result : From above graph we see that the most of the ")