import pandas
import streamlit as st
st.set_page_config(layout = "wide")
st.header("The Beat Company")
st.write("sjlkjdoienl;aksd;kpkpokvnlkdjfoijiojoigj")
st.subheader("Our Team")
col1,col2,col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col1:
    for index,row in df[:4].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
with col2:
    for index,row in df[4:8].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])
with col3:
    for index,row in df[8:].iterrows():
        st.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row["role"])
        st.image("images/" + row["image"])