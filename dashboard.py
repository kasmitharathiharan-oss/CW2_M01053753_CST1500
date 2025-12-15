import streamlit as st
from App.incidents import get_all_cyber_incidents
from App.database import get_database_connection
from App.datasets import get_all_dataset_metadata
import pandas as pd

st.header("Home Page")
st.header("Welcome to the Home Page of the Application")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.button("Log in"):
    st.session_state["logged_in"] = True
    st.success("You are now logged in!")

st.session_state["logged_in"]

st.set_page_config(
    page_title = "Home Page" ,
    page_icon = "🏠" ,
    layout = "wide"
)

conn = get_database_connection()
data = get_all_cyber_incidents(conn)

with st.sidebar:
    st.header("Cyber Severity Overview")
    severity_ = st.selectbox("Severity", data["severity"].unique())

filtered_data = data[data["severity"] == severity_]

col1, col2 = st.columns(2)

with col1:
    st.subheader("Number of Catergories")
    st.bar_chart(filtered_data["category"].value_counts())

with col2:
    st.subheader("Filtered Cyber Incidents Data")
    st.line_chart(filtered_data, x="timestamp", y="incident_id")
st.dataframe(filtered_data)
    
st.bar_chart(filtered_data["category"].value_counts())
st.dataframe(filtered_data)


df = get_all_dataset_metadata(conn)
 
st.set_page_config(layout= "wide")
st.title( "Dashboard" )
 
with st.sidebar:
    year = st.selectbox("Year", [2025, 2019, 2021])
 
col1,col2 = st.columns(2)
 
with col1:
    st.subheader("1st Chart")
    st.bar_chart(x ="name", y="dataset_id", data=df)
 
with col2:
    st.subheader("2nd Chart")
    st.line_chart(x="uploaded_by", y= "columns", data = df)



        
