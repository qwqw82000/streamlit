import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns = ["a", "b", "c"]
)

chart = alt.Chart(data).mark_circle().encode(
    x = "a", y = "b", tooltip = ["a", "b"]
)

st.altair_chart(chart)

city = pd.DataFrame({
    "멋진 도시": ["서울", "수원"],
    "lat": [37.5642135, 37.1728],
    "lon": [127.0016985, 127.032]
})

st.map(city)

plt.scatter(data["a"], data["b"])
plt.title("scatter")
st.pyplot()

st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)

st.image("office_view.jpg")
st.audio("demo.wav")
st.video("office_view.mp4")
st.video("https://www.youtube.com/watch?v=e9VmlEqU7ZU")