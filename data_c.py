import pandas as pd # pandas
import numpy as np # numpy
import seaborn as sns # seaborn
import matplotlib.pyplot as plt # ploting 
def data_c():
    import streamlit as st
    st.header("Data cleaning")

    st.code("""import pandas as pd # pandas
import numpy as np # numpy
import seaborn as sns # seaborn
import matplotlib.pyplot as plt # ploting""")
    
    df = pd.read_csv('dataset1.csv')  # read csv
    st.code("df = pd.read_csv('dataset1.csv')  # read csv")
    st.dataframe(df)

    st.code("df.isnull().sum()  # check null values in csv file")
    st.write(df.isnull().sum())

    st.code("df.info()")
    buffer = pd.io.formats.format.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.code("df.describe() # given basic common values like maximun ,minimum , mean and count etc")
    st.write(df.describe())

    st.code("df.columns")
    st.write(df.columns)
    
    