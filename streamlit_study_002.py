import streamlit as st
from PIL import Image, ImageEnhance

st.title("이미지 편집 앱")
st.text("빠르고 쉽게 이미지를 편집")
st.text("아주 쉽습니다.")
st.text("또한, 내가 직접 웹 개발을 합니다.")

activities = ["찾아줘", "나는 누구지"]
choice = st.sidebar.selectbox("할 일을 선택해주세요", activities)

if choice == "찾아줘":
    st.subheader("얼굴 인식")
    image_file = st.file_uploader("이미지 업로드")

    if image_file is not None:
        our_image = Image.open(image_file)
        st.text("원본 이미지")
        st.image(our_image)
