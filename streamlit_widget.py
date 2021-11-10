import streamlit as st

st.title("위젯 학습")

if st.button("눌러보세요"):
    st.write("눌려졌군요")
else:
    st.write("")

name = st.text_input("이름 입력")
st.write(name)

address = st.text_area("주소 입력")
st.write(address)

st.date_input("날짜 입력")
st.time_input("시간 입력")

if st.checkbox("체크하면 무엇이 될까", value = True):
    st.write("감사합니다.")

v1 = st.radio("색상", ["r", "g", "b"], index = 1)
v2 = st.selectbox("색상", ["r", "g", "b"], index = 0)
st.write(v1, v2)