import streamlit as st
from App.login import hash_password, valid_hash
from App.users import add_user, get_user
from App.database import get_database_connection

 
conn = get_database_connection()
 
st.header("Home Page")
st.write("Welcome to the home page of the application")
 
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
 
tab_login, tab_register = st.tabs(["Login", "Register"])
 
with tab_login:
    login_name = st.text_input("Username: ", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")
   
    if st.button("Log In", key="login_button"):
        id, name, hash = get_user(conn, login_name)
        if name == login_name and valid_hash(login_password, hash):
            st.session_state["logged_in"] = True
            st.success("You are now logged in.")
 
 
with tab_register:
    st.info("Registration: ")
    reg_name = st.text_input("Username: ", key="register_username")
    reg_password = st.text_input("Password", type="password", key="register_password")
   
    if st.button("Register", key="register_button"):
        hashed_psw = hash_password(reg_password)
        add_user(conn, reg_name, hashed_psw)
        st.success('Register !!!')
