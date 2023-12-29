import os
import requests as rs
import streamlit as st

api_key = os.getenv('NASAAPI')
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


def get_pic():
    response = rs.get(url)
    content = response.json()
    print(content)
    titlle = content["title"]
    desc = content["explanation"]
    image_rsp = rs.get(content["url"])
    image = image_rsp.content

    st.header("Pic by: "+content["copyright"])
    st.subheader("Date : " + content["date"])
    st.header(titlle)
    st.image(image)
    st.write(desc)


st.title(body="Astronomical Picture of The Day")

st.button(label="Fetch", on_click=get_pic,use_container_width=True)
