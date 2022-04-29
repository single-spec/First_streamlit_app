import streamlit
import pandas
streamlit.title('My Parents new healthy Diner!')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥤🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#put a pick list for customers to choose fruits 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
#display the dataframe on app page
streamlit.dataframe(my_fruit_list)


