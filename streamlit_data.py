import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

a = [1, 2, 3, 4, 5, 6, 7, 8]
n = np.array(a) # numpy의 가장 기본 데이터형 ndarray를 생성
nd = n.reshape( (2, 4) )
dic = {
    "name": ["영하", "대한민국"],
    "age": [21, 32],
    "city": ["수원", "서울"]
}
data = pd.read_csv("Salary_Data.csv")

st.text("list")
st.dataframe(a)

st.text("numpy ndarray")
st.dataframe(n)

st.text("numpy ndarray reshape")
st.dataframe(nd)

st.text("파이썬 딕셔너리")
st.dataframe(dic)

st.text("CSV로 불러온 data")
st.dataframe(data, width = 500, height = 500)
st.table(data)
st.json(dic)
st.write(data)
st.text(data)

@st.cache
def ret_time():
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(ret_time())

if st.checkbox("2"):
    st.write(ret_time())
