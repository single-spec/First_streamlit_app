import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My Parents new healthy Diner!')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥤🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#put a pick list for customers to choose fruits 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#display the dataframe on app page
streamlit.dataframe(fruits_to_show)

#new section to display fruitvice api response
streamlit.header('Fruityvice Advice!!!')
fruit_choice = streamlit.text_input('What fruit would you like the information about?', 'Kiwi')
streamlit.write('The user entered',fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)
#streamlit.text(fruityvice_response.json()) #writes data to screen

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

#snowflake connector python [having issues connecting to connector]
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#--my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * FROM fruit_load_list")
#my_data_row = my_cur.fetchone()
#--streamlit.text("Hello from Snowflake:")
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)

