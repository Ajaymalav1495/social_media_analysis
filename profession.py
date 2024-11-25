def Profession():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header(" 9. Comparsion Accoding Profession " )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""# Comparsion accoding Profession
ax = sns.countplot(x = 'profession', data=df)
for i in ax.containers:
    ax.bar_label(i)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    # Comparsion accoding Profession
    ax = sns.countplot(x = 'profession', data=df)
    for i in ax.containers:
        ax.bar_label(i)

    st.pyplot(plt)

    st.code("# Comparsion between Profession and age : \n df.groupby(['profession'],as_index=False)['age'].sum().sort_values(by='age',ascending=False)")
    
    st.write(# Comparsion between Profession and age :
df.groupby(['profession'],as_index=False)['age'].sum().sort_values(by='age',ascending=False))
        
    
    st.markdown("## Result : From above graph we see that the most of the most of the users come for the marketing manager profession ")