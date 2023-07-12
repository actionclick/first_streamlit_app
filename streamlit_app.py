import streamlit
import pandas

streamlit.title("My parents new healthy diner")
streamlit.header("🥣Breakfast menu")
streamlit.text("🥗 Omega 3 & blueberry oatmeal")
streamlit.text("🥑Kale, spinach and rocket smoothies")
streamlit.text("🐔Hard Boiled free range egg")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.

if (fruit_selected.size == 0) :
  fruit_to_show = my_fruit_list
else :
  fruit_to_show = my_fruit_list.loc[fruit_selected]
  
streamlit.dataframe(fruit_to_show)
