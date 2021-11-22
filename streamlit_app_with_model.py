import numpy as np
import streamlit as st
import cv2
from keras.models import load_model

model = load_model("dog_breed.h5")

CLASS_NAME = ["스카티시 디어하운트", "말티즈", "버네즈 마운틴 도그"]

st.title("반려견 구분하기")
st.markdown("반려견의 이미지를 업로드 해주세요")

dog_image = st.file_uploader("이미지 선택", type="png")
submit = st.button("구분하기")

if submit:
    if dog_image is not None:
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype = np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        st.image(opencv_image, channels="BGR")
        opencv_image = cv2.resize(opencv_image, (224, 224))
        opencv_image.shape = (1, 224, 224, 3)
        Y_pred = model.predict(opencv_image)

        st.title(str("이 반려견의 견종은 " + CLASS_NAME[np.argmax(Y_pred)]))
