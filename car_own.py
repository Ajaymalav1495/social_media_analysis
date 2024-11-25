def Own_a_Car():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header("12. Comparsion Accoding Owner a Car" )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""ax = sns.countplot(x = 'Owns_Car', data=df)
for i in ax.containers:
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    ax = sns.countplot(x = 'Owns_Car', data=df)
    for i in ax.containers:
        ax.bar_label(i)

    st.pyplot(plt)

    st.code("# Comparsion between Owns a car and gender : /n df.groupby(['Owns_Car'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")
    st.write(# Comparsion between Owns a car and gender :
df.groupby(['Owns_Car'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))
    
    st.markdown("## Result : From above graph we see that the most of the most of the user owns a car")
    