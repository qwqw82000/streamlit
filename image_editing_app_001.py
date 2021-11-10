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

if __name__ == "__main__":
    main()
