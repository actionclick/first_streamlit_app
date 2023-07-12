import streamlit
import pandas

streamlit.title("My parents new healthy diner")
streamlit.header("🥣Breakfast menu")
streamlit.text("🥗 Omega 3 & blueberry oatmeal")
streamlit.text("🥑Kale, spinach and rocket smoothies")
streamlit.text("🐔Hard Boiled free range egg")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

