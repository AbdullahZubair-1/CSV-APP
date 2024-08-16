import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title("CSV Data Explorer")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Dataframe:", df)
    st.write("Columns:", df.columns.tolist())
    st.write("Index:", df.index.tolist())

    selected_column = st.selectbox("Select a column to display statistical values", df.columns)
    if selected_column:
        st.write(df[selected_column].describe())

    plot_x = st.selectbox("Select column for X-axis", df.columns)
    plot_y = st.selectbox("Select column for Y-axis", df.columns)
    if plot_x and plot_y:
        fig, ax = plt.subplots()
        ax.scatter(df[plot_x], df[plot_y])
        ax.set_xlabel(plot_x)
        ax.set_ylabel(plot_y)
        st.pyplot(fig)

# streamlit run app.py

