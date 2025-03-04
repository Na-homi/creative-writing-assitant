import streamlit as st


# function for computing age

def get_age(year):
    return 2024 - year

# Create the application title
st.title(body = 'MY FIRST STREAMLIT APPLICATION')
st.divider()

# Side panel
st.sidebar.title(body = 'Appclick May')
st.sidebar.divider()


year = st.text_input(label = 'Year of birth')
if st.button(label = 'Enter', type = 'secondary'):
    year = int(year)
    age = get_age(year = year)
    st.success(f'Your age is {age} years')