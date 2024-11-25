import pandas as pd  # pandas
import numpy as np  # numpy
import seaborn as sns  # seaborn
import matplotlib.pyplot as plt  # plotting
import streamlit as st

def Age():
    st.write("hello")
    st.header("1. Comparison According to Ages")
    st.code("""
sns.set(rc={'figure.figsize':(20,10)}) 
ax = sns.countplot(x='age', data=df) 
for i in ax.containers: 
    ax.bar_label(i)
""")
    df = pd.read_csv('dataset1.csv')  # read csv
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    sns.set(rc={'figure.figsize': (20, 10)})
    ax = sns.countplot(x='age', data=df)
    for container in ax.containers:
        ax.bar_label(container)

    st.pyplot(plt)

    st.code("# Comparsion between age and gender : \n df.groupby(['gender'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")

    st.write(# Comparsion between age and gender : 
        df.groupby(['gender'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))

    st.markdown("## Result : From above graph we see that the most of Age male using social media under 18 - 64 year")