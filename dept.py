def In_Dept():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header(" 10. Comparsion Accoding Indebt " )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""ax = sns.countplot(x = 'indebt', data=df)
for i in ax.containers:
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    # Comparsion accoding Profession
    ax = sns.countplot(x = 'indebt', data=df)
    for i in ax.containers:
        ax.bar_label(i)

    st.pyplot(plt)

    st.code("# Comparsion between indebts and age : \n df.groupby(['indebt'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")
    
    st.write(# Comparsion between indebts and age :
df.groupby(['indebt'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))
        
    
    st.markdown("## Result : From above graph we see that the most of the most of the user not indebt" )