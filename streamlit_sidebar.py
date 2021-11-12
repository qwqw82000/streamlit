import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time
plt.style.use("ggplot")

data = {
    "num" : [x for x in range(1, 11)],
    "square" : [x**2 for x in range(1, 11)],
    "twice" : [x*2 for x in range(1, 11)],
    "thrice" : [x*3 for x in range(1, 11)],
}

df = pd.DataFrame(data = data)

rad = st.sidebar.radio(
    "내가 선택할 수 있는 것들", 
    ["Home", "나는 누구일까요?"], index=1
)

if rad == "Home":
    col1 = st.sidebar.selectbox(
        "컬럼을 선택해 주세요",
        df.columns
    )
    plt.plot(df["num"], df[col1])
    st.pyplot()

    col2 = st.sidebar.multiselect(
        "컬럼을 선택해 주세요",
        df.columns
    )
    plt.plot(df["num"], df[col2])
    st.pyplot()

elif rad == "나는 누구일까요?":
    st.sidebar.selectbox(
        "숫자를 선택해주세요",
        [1, 2, 3, 4, 5]
    )
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.error("에러")
    st.success("성공입니다")
    st.info("정보를 알려드립니다")
    st.exception(RuntimeError("이번에는 에러"))
    st.warning("경고입니다")