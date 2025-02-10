import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title("🎈 Data Science app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.sidebar.title("data science")
st.image("cat.jpeg")
df = pd.read_csv("type of the Diamond new.csv")
app_mode = st.sidebar.selectbox('Select a page >>',  ["01 introduction", "02 Visualization"])
if app_mode == "01 introduction":

    st.write("Lets start")
    df = pd.read_csv("type of the Diamond new.csv")

    st.dataframe(df.head(5))

    st.markdown("### Statstics of the dataframe")
    st.dataframe(df.describe())
elif app_mode == "02 Visualization":
    st.write("Hello World")

    list = df.columns

    user_selection = st.selectbox ("Selct your variable", list )

    st.markdown("### Bar Chart")
    st.bar_chart(df[user_selection])

    st.markdown("### Line Chart")
    st.line_chart(df[user_selection])

    u= st.multiselect ("Selct your variable", list, ["carat", "price"] )
    fig, ax =  plt.subplots(figsize = (6,4))

    sns.barplot(x = u[0], y= u[1], data = df, palette = "Blues")
    st.pyplot(fig)