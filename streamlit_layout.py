from os import name
import streamlit as st

st.title("사용자 등록")

family_name, name = st.columns(2)

family_name.text_input("성")
name.text_input("이름")

email, phone = st.columns([3,1])
email.text_input("이메일")
phone.text_input("핸드폰")

user_id, pw, pw2 = st.columns(3)
user_id.text_input("사용자ID")
pw.text_input("패스워드",type = "password")
pw2.text_input("패스워드 확인",type = "password")

ch,bl,sub = st.columns(3)
ch.checkbox("동의")
sub.button("제출")