import streamlit as st
st.set_page_config(
    page_title="Hello",
    page_icon="!!"
)

st.write("# Project Description:")
st.write("Developed an end-to-end machine learning project leveraging real estate data. This website aims at providing comprehensive insights and predictions for potential property buyers and sellers.")

st.write("**Price Predictor:**")
st.write("This page enables the users to input property details and receive predicted price estimates based on selected features.")

st.write("**Analytics:**")
st.write("This page offers various analytics and insights through interactive visualization plots, enhancing user engagement and understanding.")

st.write("**Recommend Appartments:**")
st.write("This page provides personalized property recommendations based on user-selected preferences and similar property features.")

st.sidebar.success("Select a demo above.")


