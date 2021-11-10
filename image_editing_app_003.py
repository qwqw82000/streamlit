import streamlit as st
import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os

# 일반적인 프로그램의 경우 entry point
# C나 자바의 경우 main()이라는 함수가 그 예!

def main():
    st.title("이미지 편집 앱")
    st.text("빠르고 쉽게 이미지를 편집")

    activities = ["Detection", "About"]
    choice = st.sidebar.selectbox(
        "Activity를 선택해주세요",
        activities
    )

    if choice == "Detection":
        st.subheader("Face Detection")
        image_file = st.file_uploader(
            "이미지를 업로드 해주세요",
            type = ["jpg", "png", "jpeg"]
        )

        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("원본 이미지")
            st.image(our_image)

            enhance_type = st.sidebar.radio(
                "이미지 개선 방법들",
                ["원본", "Gray", "Contrast", "Brightness", "Blur", "Sharp"]
            )

            if enhance_type == "Gray":
                img = np.array(our_image.convert("RGB"))
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                st.image(gray)
            elif enhance_type == "Contrast":
                rate = st.sidebar.slider("Contrast", 0.5, 6.0)
                enhancer = ImageEnhance.Contrast(our_image)
                enhanced_image = enhancer.enhance(rate)
                st.image(enhanced_image)
            elif enhance_type == "Brightness":
                rate = st.sidebar.slider("Brightness", 0.0, 8.0)
                enhancer = ImageEnhance.Brightness(our_image)
                enhanced_image = enhancer.enhance(rate)
                st.image(enhanced_image)                
            elif enhance_type == "Blur":
                rate = st.sidebar.slider("Blur", 0.0, 7.0)
                enhanced_image = cv2.GaussianBlur(np.array(our_image), (15, 15), rate)
                st.image(enhanced_image)
            elif enhance_type == "Sharp":
                rate = st.sidebar.slider("Sharp", 0.0, 14.0)
                enhancer = ImageEnhance.Sharpness(our_image)
                enhanced_image = enhancer.enhance(rate)
                st.image(enhanced_image)
            elif enhance_type == "원본":
                st.image(our_image, width = 300)

    elif choice == "About":
        st.subheader("개발자를 소개합니다.")
        st.text("김영하입니다")
        st.markdown("자! 이제 ** [네이버](http://www.naver.com) ** 로 이동해보겠습니다!")


if __name__ == "__main__":
    main()
