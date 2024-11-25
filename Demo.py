def Demographics():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header("8. Comparsion Accoding Demographics")
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""ax = sns.countplot(x='demographics',data=df)
for i in ax.containers:
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    ax = sns.countplot(x='demographics',data=df)
    for i in ax.containers:
        ax.bar_label(i)
    st.pyplot(plt)

    st.code# Comparsion between Demographics and age : \n df.groupby(['demographics'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")
    
    st.write(# Comparsion between Demographics and age :
df.groupby(['demographics'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))
        
    
    st.markdown("## Result : From above graph we see that the most of the most of the user come for rural areas")