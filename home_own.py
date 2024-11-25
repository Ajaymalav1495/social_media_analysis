def Own_a_Home():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header("11. Comparsion Accoding Owner a Home" )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""ax = sns.countplot(x = 'isHomeOwner', data=df)
for i in ax.containers:
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    ax = sns.countplot(x = 'isHomeOwner', data=df)
    for i in ax.containers:
        ax.bar_label(i)

    st.pyplot(plt)

    st.code("# Comparsion between owns a home and Age : \n df.groupby(['isHomeOwner'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")
    st.write(# Comparsion between owns a home and Age :
df.groupby(['isHomeOwner'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))
    
    st.markdown("## Result : From above graph we see that the most of the most of the user owns a home")