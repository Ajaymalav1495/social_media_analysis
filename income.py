def Income_And_Age():
    import streamlit as st
    import pandas as pd  # pandas
    import numpy as np  # numpy
    import seaborn as sns  # seaborn
    import matplotlib.pyplot as plt  # plotting
    import streamlit as st
    st.header(" 7. Comparsion Between Income And Age " )
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.code("""ax = sns.pointplot(x = "age",y="income", data =df)""")
    df = pd.read_csv('dataset1.csv')  # read csv
    
    ax = sns.pointplot(x = "age",y="income", data =df)

    st.pyplot(plt)

    st.code("# Comparsion between age and income :\n a = df.groupby(['age'],as_index=False)['income'].sum().sort_values(by='income',ascending=False)\n a.head()")
    a = df.groupby(['age'],as_index=False)['income'].sum().sort_values(by='income',ascending=False)
    a.head()
    st.write(a.head())
        
    
    st.markdown("## Result : From above graph we see that the most of the maximum users earn between 14000 to 16000")