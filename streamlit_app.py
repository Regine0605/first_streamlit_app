import streamlit
import pandas

streamlit.title('My Moms New Healthy Diner')

streamlit.header('🥣 Breakfast Favorites')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text('🍞 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
default_selected_fruits = ['Avocado', 'Strawberry']

# Use st.multiselect with the default parameter
selected_fruits = st.multiselect("Pick some fruits:", list(my_fruit_list.index), default=default_selected_fruits)

# Do something with the selected fruits, if needed
st.write("Selected Fruits:", selected_fruits)
streamlit.dataframe(my_fruit_list)


