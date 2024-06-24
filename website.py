from main import main
import json, streamlit as st

st.title("Who Are You?")

col1, col2 = st.columns(2)

with col1:
    # data = main()
    with open("data.json", "r") as file:
        data = json.load(file)

    st.html(f"""
    <b>IP Address:</b> {data["ip_address"]} <br>
    <b>City:</b>  {data["city"]}<br>
    <b>Region:</b>  {data["region"]}<br>
    <b>Postal Code:</b>  {data["postal_code"]}<br>
    <b>Country:</b>  {data["country"]}<br>
    <b>Continent</b> : {data["continent"]}<br>
    <b>Flag:</b>  {data["flag"]["emoji"]}<br>
    <b>Time Zone: {data["timezone"]["name"]}<br>
    <b>Current Time:</b>  {data["timezone"]["current_time"]}<br>
    <img src="{data["flag"]["png"]}" alt="flag">
    """)