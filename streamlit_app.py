import streamlit

streamlit.title("My Mom's New Healthy Diner")

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale ,Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

#lets put pick list here so they want to pick tht fruit they want to incude
streamlit.multiselect("Pick some Fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
