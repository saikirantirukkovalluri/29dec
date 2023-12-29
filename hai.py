import streamlit as st
st.set_page_config(layout="wide")
st.title("Student management System")
st.sidebar.title("File management system")
#roll nuumber
#name
#fees
st.sidebar.subheader("Add Student")
rollnumber=st.sidebar.number_input("Roll Number")
name=st.sidebar.text_input("Nmae")
fees=st.sidebar.number_input("Fees")
add=st.sidebar.button("Add")
