import streamlit as st
import pandas as pd

st.title('My Mom\'s New Healthy Diner')

st.header('🥣 Breakfast Favorites')
st.text('🥗 Omega 3 & Blueberry Oatmeal')
st.text('🍞 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Using st.sidebar to display the multiselect widget
selected_fruits = st.sidebar.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberry'])

# Do something with the selected fruits, if needed
st.write("Selected Fruits:", selected_fruits)

# Display the DataFrame in the main content area
st.dataframe(my_fruit_list)



