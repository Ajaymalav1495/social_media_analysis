def States():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header(" 6. Comparsion Accoding States " )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""sns.set(rc={'figure.figsize':(20,7.5)})
ax = sns.countplot(x = "location", data =df)
for i in ax.containers:
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    sns.set(rc={'figure.figsize':(20,7.5)})
    ax = sns.countplot(x = "location", data =df)
    for i in ax.containers:
        ax.bar_label(i)

    st.pyplot(plt)

    st.code("# Comparsion between states and age : \n df.groupby(['location'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")
    st.write(# Comparsion between states and age :
df.groupby(['location'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))
    
    st.markdown("## Result : From above graph we see that the most of the users live in Astralia")