import streamlit as st
from PIL import Image
import cv2
import numpy as np

from models.easy_ocr.esay_ocr import perform_ocr_easyocr
from models.paddle_ocr.paddle_ocr import perform_ocr_paddleocr
from models.tesseract_ocr.tesseract_ocr import perform_ocr_tesseract


st.title("SIMPLE OCR")
st.write("**이미지를 업로드하면 한국어 글자를 인식하고 인식된 글자를 보여줍니다.**")

option = st.sidebar.selectbox(
    '선택된 OCR',
     ('EasyOCR', 'PaddleOCR', 'TesseractOCR'))


uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if st.button("OCR 실행"):
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        
        if option == 'EasyOCR': # 선택된 option에 따라 다른 OCR 실행
            st.write("## 인식 결과 (EasyOCR)")
            with st.spinner("EasyOCR 글자 인식 중..."):
                image_np = np.array(image)  # PIL 이미지를 NumPy 배열로 변환
                recognized_text = perform_ocr_easyocr(image_np) # easyocr_functions.py 함수 호출

                # 결과 출력
                st.text_area("", recognized_text, height=300)
        elif option == 'PaddleOCR': # 선택된 option에 따라 다른 OCR 실행
            st.write("## 인식 결과 (PaddleOCR)")
            with st.spinner("PaddleOCR 글자 인식 중..."):
                image_np = np.array(image)  # PIL 이미지를 NumPy 배열로 변환
                recognized_text = perform_ocr_paddleocr(image_np) # paddle_ocr_functions.py 함수 호출

                # 결과 출력
                st.text_area("", recognized_text, height=300)
        elif option == 'TesseractOCR': # 선택된 option에 따라 다른 OCR 실행
                st.write("## 인식 결과 (TesseractOCR)")
                with st.spinner("TesseractOCR 글자 인식 중..."):
                    image_np = np.array(image)  # PIL 이미지를 NumPy 배열로 변환
                    recognized_text = perform_ocr_tesseract(image_np) # paddle_ocr_functions.py 함수 호출

                    # 결과 출력
                    st.text_area("", recognized_text, height=300)


